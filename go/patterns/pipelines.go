package main

import (
	"sync"
	"fmt"
)

// generates a channel of numbers from an array of numbers.
func gen(nums ...int) <-chan int {
	out := make(chan int)
	go func() {
		for _, n := range nums {
			out<- n
		}
		close(out)
	}()
	return out
}

// generates a sequence of squared numbers.
func sq(done <-chan struct{}, in <-chan int) <-chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for n := range in {
			select {
			case out<- n*n:
			case <-done:
				return
			}
		}
	}()
	return out
}

/* // simple piping example
func main() {
	for o := range sq(sq(gen(1,2,3,4,5))) {
		fmt.Println(o)
	}
}
*/


// my own implementation of WaitGroup
type MyWG interface {
	Done()
	Wait()
	Add(i int)
}

type StandardWg struct {
	counter int
	done bool
	blocker chan bool
}
func (s *StandardWg) Done() {
	if s.done == true {
		return
	}
	s.counter -= 1
	if s.counter == 0 {
		s.done = true
		s.blocker <- true
	}
}
func (s *StandardWg) Wait() {
	if s.done == true {
		return
	}
	<-s.blocker
}
func (s *StandardWg) Add(i int) {
	if s.done == true {
		return
	}
	s.counter += i
}


// fan-in multiple channels into a single channel.
func merge(done <-chan struct{}, cs ...<-chan int) <-chan int {
	var wg sync.WaitGroup
	out := make(chan int)

	output := func(c <-chan int) {
		defer wg.Done()
		for n := range c {
			select {
			case out<- n:
			case <-done:
				return
			}
		}
	}

	wg.Add(len(cs))
	for _, c := range cs {
		go output(c)
	}

	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}

/* // simple fan-in example
func main() {
	in := gen(1,2,3,4,5,6)
	done := make(chan struct{})
	defer close(done)

	c1 := sq(done, in)
	c2 := sq(done, in)

	fmt.Println(<-c1)
	fmt.Println(<-c2)
	//for n := range merge(done, c1, c2) {
	//	fmt.Println(n)
	//}
}
*/

func main() {

}
