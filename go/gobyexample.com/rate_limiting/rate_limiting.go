// alternative implementation https://github.com/golang/go/wiki/RateLimiting
package main

import (
	"fmt"
	"time"
)

func main() {
	requests := make(chan int, 5)
	for i := 1; i <= 5; i += 1 {
		requests <- i
	}
	close(requests)

	limiter := time.Tick(time.Millisecond * 200)
	for r := range requests {
		<-limiter
		fmt.Printf("handle request %d (%s)\n", r, time.Now())
	}

	// build a limiter which supports bursting.
	burstyLimiter := make(chan time.Time, 3)
	for i := 1; i <= 3; i += 1 {
		burstyLimiter <- time.Now()
	}

	go func() {
		for t := range time.Tick(time.Millisecond * 200) {
			burstyLimiter <- t
		}
	}()

	burstyRequests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		burstyRequests <- i
	}
	close(burstyRequests)

	for req := range burstyRequests {
		<-burstyLimiter
		fmt.Printf("Received request %d (at %s)\n", req, time.Now())
	}
}
