package main

import "fmt"

func f(left, right chan int) {
	val := <-right
	left <- val + 1
}

func main() {
	const n = 100000
	leftmost := make(chan int)

	left := leftmost
	var right chan int
	for i := 0; i < n; i += 1 {
		right = make(chan int)
		go f(left, right)
		left = right
	}

	go func(c chan int) {
		c <- 1
	}(right)
	fmt.Println(<-leftmost)
}
