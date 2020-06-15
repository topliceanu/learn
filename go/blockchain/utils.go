package main

import (
	"bytes"
	"encoding/binary"
)

func IntToHex(val int64) []byte {
	buff := new(bytes.Buffer)
	if err := binary.Write(buff, binary.BigEndian, val); err != nil {
		panic(err)
	}
	return buff.Bytes()
}

