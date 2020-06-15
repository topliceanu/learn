package main

import (
	bolt "go.etcd.io/bbolt"
)

const dbFile = "./blockchain.db"

const blocksBucket = "blocks"

type Blockchain struct {
	tip []byte // hash of the latest block in the chain.
	db *bolt.DB
}

func (bc *Blockchain) MineBlock(transactions []*Transaction) {
	var lastHash []byte

	err := bc.db.View(func(tx *bolt.Tx) error {
		bucket := tx.Bucket([]byte(blocksBucket))
		lastHash = bucket.Get([]byte{'l'})
		return nil
	})
	if err != nil {
		panic(err)
	}

	newBlock := NewBlock(transactions, lastHash)

	err = bc.db.Update(func(tx *bolt.Tx) error {
		bucket := tx.Bucket([]byte(blocksBucket))
		if err := bucket.Put(newBlock.Hash, newBlock.Serialize()); err != nil {
			return err
		}
		if err := bucket.Put([]byte{'l'}, newBlock.Hash); err != nil {
			return err
		}
		bc.tip = newBlock.Hash
		return nil
	})
	if err != nil {
		panic(err)
	}
}

func NewBlockchain() *Blockchain {
	var tip []byte
	db, err := bolt.Open(dbFile, 0600, nil)
	if err != nil {
		panic(err)
	}
	err = db.Update(func(tx *bolt.Tx) error {
		bucket := tx.Bucket([]byte(blocksBucket))
		if bucket == nil {
			genesis := NewGenesisBlock()
			bucket, err := tx.CreateBucket([]byte(blocksBucket))
			if err != nil {
				return err
			}
			if err = bucket.Put(genesis.Hash, genesis.Serialize()); err != nil {
				return err
			}
			if err = bucket.Put([]byte{'l'}, genesis.Hash); err != nil {
				return err
			}
			tip = genesis.Hash
		} else {
			tip = bucket.Get([]byte{'l'})
		}
		return nil
	})
	if err != nil {
		panic(err)
	}
	return &Blockchain{
		tip: tip,
		db: db,
	}
}

type BlockchainIterator struct {
	currentHash []byte
	db *bolt.DB
}

func (bci *BlockchainIterator) Next() *Block {
	if len(bci.currentHash) == 0 {
		return nil
	}
	var block *Block
	err := bci.db.View(func(tx *bolt.Tx) error {
		bucket := tx.Bucket([]byte(blocksBucket))
		encodedBlock := bucket.Get(bci.currentHash)
		block = DeserializeBlock(encodedBlock)
		return nil
	})
	if err != nil {
		panic(err)
	}
	bci.currentHash = block.PrevBlockHash
	return block
}

func (bc *Blockchain) Iterator() *BlockchainIterator {
	return &BlockchainIterator{
		currentHash: bc.tip,
		db: bc.db,
	}
}



