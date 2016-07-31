// or the fan-out pattern
package main

import (
	"fmt"
	"time"
	"sync"
)

func worker(name int, jobs <-chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for j := range jobs {
		fmt.Printf("Worker %d processing job %d\n", name, j)
		time.Sleep(100 * time.Millisecond)
	}
	fmt.Printf("Worker %d finished\n", name)
}

func pool(numJobs, numWorkers int, wg *sync.WaitGroup) {
	var out = make(chan int)
	go func() {
		for i := 0; i < numJobs; i += 1 {
			out<- i
		}
		close(out)
	}()

	for i := 1; i <= numWorkers; i += 1 {
		go worker(i, out, wg)
	}
}

func main() {
	numWorkers := 100
	numJobs := 1000
	wg := &sync.WaitGroup{}
	wg.Add(numWorkers)
	go pool(numJobs, numWorkers, wg)
	wg.Wait()
}
