package main

import (
	"fmt"
)

const subsidy = 10 // amount awarded for mining a block.

type Transaction struct {
	ID []byte
	Vin []TXInput
	Vout []TXOutput
}

type TXOutput struct {
	Value int
	ScriptPubKey string
}

type TXInput struct {
	TxID []byte
	Vout int
	ScriptSig string
}

func NewCoinbaseTx(to, data string) *Transaction {
	if data == "" {
		data = fmt.Sprintf("Reward to '%s'", to)
	}
	txin := TXInput{
		TxID: []byte{},
		Vout: -1,
		ScriptSig: data,
	}
	txout := TXOutput{
		Value: subsidy,
		ScriptPubKey: to,
	}
	tx := Transaction{
		ID: nil,
		Vin: []TXInput{txin},
		Vout: []TXOutput{txout},
	}
	tx.SetID()
	return tx
}
