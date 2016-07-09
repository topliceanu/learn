package main

import (
	"fmt"
	"time"
)

func pinger(pongs <-chan bool, pings chan<- bool) {
	for {
		<-pongs
		fmt.Println("Received pong!")
		time.Sleep(1000)
		pings<- true
	}
}

func ponger(pings <-chan bool, pongs chan<- bool) {
	for {
		<-pings
		fmt.Println("Received ping!")
		time.Sleep(1000)
		pongs<- true
	}
}

func main() {
	pings := make(chan bool, 1)
	pongs := make(chan bool, 1)

	go pinger(pongs, pings)
	go ponger(pings, pongs)

	pings<-true

	var input string
	fmt.Scanln(&input)
	fmt.Println("Stopped")
}
