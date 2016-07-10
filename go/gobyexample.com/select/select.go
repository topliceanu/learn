package main

import (
	"fmt"
	"time"
)

func printer(seconds int64, out chan<- bool) {
	for {
		time.Sleep(time.Second * time.Duration(seconds))
		out <- true
	}
}

func main() {
	c1 := make(chan bool)
	c2 := make(chan bool)

	go printer(1, c1)
	go printer(2, c2)

	for i := 1; i < 10; i += 1 {
		select {
		case <-c1:
			fmt.Println("Message received from c1")
		case <-c2:
			fmt.Println("Message received from c2")
		}
	}
}
