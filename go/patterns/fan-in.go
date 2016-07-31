package main

import (
	"fmt"
	"time"
)

func producer(name int) <-chan string {
	out := make(chan string)
	ticker := time.NewTicker(time.Duration(name * 100) * time.Millisecond)
	i := 0
	go func() {
		for _ = range ticker.C {
			out<- fmt.Sprintf("%d:%d", name, i)
			i += 1
		}
	}()
	return out
}

func fanIn(c ...<-chan string) chan string {
	out := make(chan string)
	go func() {
		for {
			select {
			case v1 := <-c1:
				out<- v1
			case v2 := <-c2:
				out<- v2
			}
		}
	}()
	return out
}

func main() {
	c1 := producer(1)
	c2 := producer(2)
	c3 := producer(3)
	c4 := producer(4)
	r1 := fanIn(c1, c2)

	for r := range(r1) {
		fmt.Printf("%s\n", r)
	}
}
