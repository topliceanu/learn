package main

import (
	"encoding/hex"
	"os"
	"fmt"

	bolt "go.etcd.io/bbolt"
)

const dbFile = "./blockchain.db"
const blocksBucket = "blocks"
const genesisCoinbaseData = "Genesis block"

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
	if !dbExists() {
		fmt.Println("no blockchain exists. create one first")
		os.Exit(1)
	}
	var tip []byte
	db, err := bolt.Open(dbFile, 0600, nil)
	if err != nil {
		panic(err)
	}
	err = db.Update(func(tx *bolt.Tx) error {
		bucket := tx.Bucket([]byte(blocksBucket))
		tip := b.Get([]byte{'1'})
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

func (bc *Blockchain) FindUnspentTransactions(address string) []Transaction {
	var unspentTXs []Transaction
	spentTXOs := make(map[string][]int)
	bci := bc.Iterator()

	for block := bci.Next(); block != nil; block = bci.Next() {
		for _, tx := range block.Transactions {
			txID := hex.EncodeToString(tx.ID)

			Outputs:
				for outIdx, out := range tx.Vout {
					// Was the output spent?
					if spentTXOs[txID] != nil {
						for _, spentOut := range spentTXOs[txID] {
							if spentOut == outIdx {
								continue Outputs
							}
						}
					}

					if out.CanBeUnlockedWith(address) {
						unspentTXs = append(unspentTXs, *tx)
					}
				}

				if tx.IsCoinbase() == false {
					for _, in := range tx.Vin {
						if in.CanUnlockOutputWith(address) {
							inTxID := hex.EncodeToString(in.Txid)
							spentTXOs[inTxID] = append(spentTXOs[inTxID], in.Vout)
						}
					}
				}
		}
	}

	return unspentTXs
}

func (bc *Blockchain) FindUTXO(address string) []TXOutput {
	var UTXO []TXOutput
	unspentTransactions := bc.FindUnspentTransactions(address)
	for _, tx := range unspentTransactions {
		for _, out := range tx.Vout {
			if out.CanBeUnlockedWith(address) {
				UTXO = append(UTXO, out)
			}
		}
	}
	return UTXO
}

// FindSpendableOutputs finds and returns unspent outputs to reference in inputs
func (bc *Blockchain) FindSpendableOutputs(address string, amount int) (int, map[string][]int) {
	unspentOutputs := make(map[string][]int)
	unspentTXs := bc.FindUnspentTransactions(address)
	accumulated := 0

	Work:
		for _, tx := range unspentTXs {
			txID := hex.EncodeToString(tx.ID)

			for outIdx, out := range tx.Vout {
				if out.CanBeUnlockedWith(address) && accumulated < amount {
					accumulated += out.Value
					unspentOutputs[txID] = append(unspentOutputs[txID], outIdx)

					if accumulated >= amount {
						break Work
					}
				}
			}
		}

	return accumulated, unspentOutputs
}

func dbExists() bool {
	if _, err := os.Stat(dbFile); os.IsNotExist(err) {
		return false
	}
	return true
}
