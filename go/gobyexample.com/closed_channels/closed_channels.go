// the main goroutine publishes three jobs then closes the channel.

package main

import "fmt"

func worker(jobs <-chan int, done chan<- bool) {
	for {
		job, more := <-jobs
		if more {
			fmt.Printf("Processing job %d\n", job)
		} else {
			done<-true
			return
		}
	}
}

func main() {
	jobs := make(chan int)
	done := make(chan bool)

	go worker(jobs, done)

	for i := 1; i <= 3; i += 1 {
		jobs <- i
	}
	close(jobs)

	<-done
	fmt.Println("Stopped the process")
}
