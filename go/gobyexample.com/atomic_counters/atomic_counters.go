// start 50 goroutines that increment the same counter, wait a second then print the counter.
package main

import (
	"fmt"
	"runtime"
	"time"
	"sync/atomic"
)

func main() {
	var x uint64 = 1

	for i := 1; i <= 10; i += 1 {
		go func() {
			for {
				atomic.AddUint64(&x, 1)
				runtime.Gosched()
			}
		}()
	}

	time.Sleep(time.Second)
	value := atomic.LoadUint64(&x)
	fmt.Printf("The incremented value is %d\n", value)
}
