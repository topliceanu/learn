package main

import (
	"fmt"
	"net"
)

func logger(logs <-chan string) {
	for i := 1; i <= 10; i += 1 {
		go func(i int) {
			for l := range logs {
				fmt.Printf("Logger %d prints %s\n", i, l)
			}
		}(i)
	}
}

func handler(c net.Conn, logs chan<- string) {
	logs<- fmt.Sprintf("New client connected from %s", c.RemoteAddr())
	c.Write([]byte("ok"))
	c.Close()
}

func server(l net.Listener, logs chan<- string) {
	for {
		c, err := l.Accept()
		if err != nil {
			continue
		}
		go handler(c, logs)
	}
}

func main() {
	l, err := net.Listen("tcp", "0.0.0.0:5000")
	if err != nil {
		panic(err)
	}

	logs := make(chan string)
	go logger(logs)

	server(l, logs)
}
