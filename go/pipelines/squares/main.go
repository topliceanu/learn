package main

import (
	"fmt"
	"sync"
)

// gen takes a list of ints and returns channel which produces these numbers.
func gen(nums ...int) <-chan int {
	var (
		out = make(chan int)
		n   int
	)
	go func() {
		for _, n = range nums {
			out <- n
		}
		close(out)
	}()
	return out
}

// sq takes a channel of ints and return a channel which outputs the squares of the inputs.
func sq(nums <-chan int) <-chan int {
	var (
		out = make(chan int)
		n   int
	)
	go func() {
		for n = range nums {
			out <- n * n
		}
		close(out)
	}()
	return out
}

// consume is a helper method for merge. It reads values from c and writes them to out, until c is closed, calling Done the input WaitGroup.
func consume(wg *sync.WaitGroup, c <-chan int, out chan<- int) {
	for n := range c {
		out<- n
	}
	wg.Done()
}

// merge will read from two channels and produce a single output channel
func merge(cs ...<-chan int) <-chan int {
	var (
		out chan int
		wg  sync.WaitGroup
		c   <-chan int
	)
	out = make(chan int)
	wg = sync.WaitGroup{}
	wg.Add(len(cs))
	for _, c = range cs {
		go consume(&wg, c, out)
	}
	go func() {
		wg.Wait()
		close(out)
	}()
	return out
}

func main() {
	var (
		c1, c2, c3, c4 <-chan int
		n              int
	)
	c1 = gen(1, 2, 3, 4, 5)
	c2 = sq(c1)
	c3 = sq(c2)
	c4 = gen(1, 2, 3, 4, 4, 5)
	for n = range merge(c3, c4) {
		fmt.Println(n)
	}
}

//// merge alternative version only for two channels without the use of a WaitGroup.
//func merge(c1, c2 <-chan int) <-chan int {
//	var (
//		out chan int
//	)
//	out = make(chan int)
//	go func() {
//		var (
//			n int
//			open1, open2 bool
//		)
//		for {
//			select {
//			case n, open1 = <-c1:
//				if open1 == false && open2 == false {
//					close(out)
//					return
//				} else if open1 == false {
//					continue
//				} else {
//					out <- n
//				}
//			case n, open2 = <-c2:
//				if open1 == false && open2 == false {
//					close(out)
//					return
//				} else if open2 == false {
//					continue
//				} else {
//					out <- n
//				}
//			}
//		}
//	}()
//	return out
//}
