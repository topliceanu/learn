// start 10 goroutines which atomically populate a hash table.
// start 10 goroutines which read atomically from the hash table and sum the values.
// wait a second and print the number of operations and the sum.

package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"sync"
	"sync/atomic"
	"time"
)

func main() {
	var data = make(map[int]int)
	var mutex = &sync.Mutex{}
	var numOps uint64 = 0
	var numWriters uint8 = 10
	var numReaders uint8 = 10
	var sum int = 0
	var i uint8

	// 10 writers
	for i = 1; i <= numWriters; i += 1 {
		go func() {
			for {
				key := rand.Intn(5)
				val := rand.Intn(100)
				mutex.Lock()
				data[key] = val
				mutex.Unlock()
				atomic.AddUint64(&numOps, 1)
				runtime.Gosched()
			}
		}()
	}

	// 10 Readers
	for i = 1; i <= numReaders; i += 1 {
		go func() {
			for {
				key := rand.Intn(5)
				mutex.Lock()
				sum += data[key]
				mutex.Unlock()
				atomic.AddUint64(&numOps, 1)
				runtime.Gosched()
			}
		}()
	}

	time.Sleep(time.Second)
	numOpsSnapshot := atomic.LoadUint64(&numOps)
	fmt.Printf("Number of ops %d and total sum %d\n", numOpsSnapshot, sum)

	mutex.Lock()
	fmt.Printf("Data %+v\n", data)
	mutex.Unlock()
}
