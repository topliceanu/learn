package main

import (
	"context"
	"fmt"
	"sync"
)

// gen takes a list of ints and returns channel which produces these numbers.
func gen(ctx context.Context, nums ...int) <-chan int {
	var (
		out = make(chan int)
		n   int
	)
	go func() {
		for _, n = range nums {
			select {
			case out <- n:
			case <-ctx.Done():
				fmt.Println("gen closed")
				close(out)
				return
			}
		}
		close(out)
	}()
	return out
}

// sq takes a channel of ints and return a channel which outputs the squares of the inputs.
func sq(ctx context.Context, nums <-chan int) <-chan int {
	var (
		out = make(chan int)
		n   int
	)
	go func() {
		for n = range nums {
			select {
			case out <- n * n:
			case <-ctx.Done():
				fmt.Println("sq closed")
				close(out)
				return
			}
		}
		close(out)
	}()
	return out
}

// consume is a helper method for merge. It reads values from c and writes them to out, until c is closed, calling Done the input WaitGroup.
func consume(ctx context.Context, wg *sync.WaitGroup, c <-chan int, out chan<- int) {
	defer wg.Done()
	for n := range c {
		select {
		case out <- n:
		case <-ctx.Done():
			fmt.Println("consume closed")
			return
		}
	}
}

// merge will read from two channels and produce a single output channel
func merge(ctx context.Context, cs ...<-chan int) <-chan int {
	var (
		out chan int
		wg  sync.WaitGroup
		c   <-chan int
	)
	out = make(chan int)
	wg = sync.WaitGroup{}
	wg.Add(len(cs))
	for _, c = range cs {
		go consume(ctx, &wg, c, out)
	}
	go func() {
		wg.Wait()
		fmt.Println("merge closed")
		close(out)
	}()
	return out
}

func main() {
	var (
		c1, c2, c3, c4, c5 <-chan int
		ctx                context.Context
		cancel             context.CancelFunc
		n, i               int
	)
	ctx, cancel = context.WithCancel(context.Background())

	c1 = gen(ctx, 1, 2, 3, 4, 5)
	c2 = sq(ctx, c1)
	c3 = sq(ctx, c2)
	c4 = gen(ctx, 1, 2, 3, 4, 4, 5)
	c5 = merge(ctx, c3, c4)

	i = 0
	for n = range c5 {
		i += 1
		fmt.Println(n)
		if i == 3 {
			fmt.Println("main closed")
			cancel()
		}
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
