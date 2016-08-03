package main

import (
	"fmt"
	"time"
)

func worker(factor int, in <-chan int, out chan<- int) {
	var hasNext bool
	var next = make(chan int)

	for i := range in {
		if i < factor {
			panic("Should not get here")
		} else if i == factor {
			out<- i
		} else if i % factor == 0 {
			fmt.Printf("This is not a prime %d because %d devides it\n", i, factor)
		} else {
			if (!hasNext) {
				hasNext = true
				go worker(i, next, out)
			}
			next<- i
		}
	}
}

func generator(out chan<- int) {
	for i := 2; ; i += 1 {
		out<- i
	}
}

func main() {
	in := make(chan int)
	primes := make(chan int)

	go generator(in)
	go worker(2, in, primes)

	go func() {
		for i := range primes{
			fmt.Printf("Found a prime %d\n", i)
		}
	}()

	time.Sleep(100 * time.Millisecond)
	panic("show me the goroutines")
}
