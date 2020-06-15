package main

import (
	"time"
	"bytes"
	"encoding/gob"
)

type Block struct {
	Timestamp int64
	Transactions []*Transaction
	PrevBlockHash []byte
	Hash []byte
	Nonce int
}

// TODO data should really be []byte
func NewBlock(transactions []*Transaction, prevBlockHash []byte) *Block {
	block := &Block{
		Timestamp: time.Now().Unix(),
		Transactions: transactions,
		PrevBlockHash: prevBlockHash,
	}
	pow := NewProofOfWork(block)
	nonce, hash := pow.Run()
	block.Hash = hash[:]
	block.Nonce = nonce
	return block
}

func NewGenesisBlock(coinbase *Transaction) *Block {
	return NewBlock([]byte{coinbase}, []byte{})
}

func (b *Block) Serialize() []byte {
	var result bytes.Buffer
	encoder := gob.NewEncoder(&result)
	if err := encoder.Encode(b); err != nil {
		panic(err)
	}
	return result.Bytes()
}

func DeserializeBlock(blob []byte) *Block {
	var block Block
	decoder := gob.NewDecoder(bytes.NewReader(blob))
	if err := decoder.Decode(&block); err != nil {
		panic(err)
	}
	return &block
}

func (b *Block) HashTransactions() []byte {
	var txHashes [][]byte
	for _, tx := range b.Transactions {
		txHashes = append(txHashes,	tx.ID)
	}
	txHash := sha256.Sum256(bytes.Join(txHashes, []byte{}))
	return txHashes[:]
}
