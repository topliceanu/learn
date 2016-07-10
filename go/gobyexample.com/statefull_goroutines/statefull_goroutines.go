package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Utilizes the Request-Response pattern: you send a
type Read struct {
	key  int
	resp chan int
}

type Write struct {
	key, val int
	resp     chan bool
}

type Result struct {
	data   map[int]int
	sum    int
	numOps int
}

type Response struct {
	C chan *Result
}

// Receives requests on the reads and writes channels and uses the response
// channels to reply to the requestor goroutine.
func coordinator(reads <-chan *Read, writes <-chan *Write, response <-chan *Response) {
	var data = make(map[int]int)
	var sum int = 0
	var numOps int = 0

	for {
		select {
		case r := <-reads:
			sum += data[r.key]
			numOps += 1
			r.resp <- data[r.key]
		case w := <-writes:
			data[w.key] = w.val
			numOps += 1
			w.resp <- true
		case res := <-response:
			res.C <- &Result{data, sum, numOps}
		}
	}
}

func reader(reads chan<- *Read) {
	for {
		key := rand.Intn(5)
		resp := make(chan int)
		r := &Read{key, resp}
		reads <- r
		<-r.resp
	}
}

func writer(writes chan<- *Write) {
	for {
		key := rand.Intn(5)
		val := rand.Intn(100)
		resp := make(chan bool)
		w := &Write{key, val, resp}
		writes <- w
		<-w.resp
	}
}

func main() {
	var reads = make(chan *Read)
	var writes = make(chan *Write)
	var response = make(chan *Response)

	go coordinator(reads, writes, response)
	for i := 1; i <= 100; i += 1 {
		go reader(reads)
	}
	for i := 1; i <= 10; i += 1 {
		go writer(writes)
	}

	time.Sleep(time.Second)
	rc := make(chan *Result)
	response <- &Response{C: rc}
	result := <-rc
	fmt.Printf("Number of ops %d and total sum %d\n", result.numOps, result.sum)
	fmt.Printf("Data %+v\n", result.data)
}

/*
// Uses a struct to comunicate

type State struct {
	data map[int]int
	numOps uint64
	sum int
}

func reader(in <-chan *State, out chan<- *State) {
	for state := range in {
		key := rand.Intn(5)
		state.sum += state.data[key]
		state.numOps += 1
		out<- state
	}
}

func writer(in <-chan *State, out chan<- *State) {
	for state := range in {
		key := rand.Intn(5)
		val := rand.Intn(100)
		state.data[key] = val
		state.numOps += 1
		out<- state
	}
}

func main() {
	var in = make(chan *State)
	var out = make(chan *State)
	var numWriters int = 10
	var numReaders int = 10
	var i int

	for i = 1; i <= numWriters; i += 1 {
		go writer(in, out)
	}

	for i = 1; i <= numReaders; i += 1 {
		go reader(out, in)
	}

	state := &State{}
	state.data = make(map[int]int)
	in<-state

	time.Sleep(time.Second)
	fmt.Printf("Number of ops %d and total sum %d\n", state.numOps, state.sum)
	fmt.Printf("Data %+v\n", state.data)
}
*/
