package main

import (
	"io"
	"log"
	"net"
)

const address = "0.0.0.0:4000"

func handler(c net.Conn) {
	io.Copy(c, c)
}

func main() {
	l, err := net.Listen("tcp", address)
	if err != nil {
		log.Fatal(nil)
	}

	for {
		c, err := l.Accept()
		if err != nil {
			log.Fatal(err)
		}
		go handler(c)
	}
}
