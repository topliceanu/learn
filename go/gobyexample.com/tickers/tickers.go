// create a goroutine which periodically prints a message.
// In main we simply sleep then stop the ticker.

package main

import (
	"fmt"
	"time"
)

func ticker(tick <-chan time.Time) {
	for t := range tick {
		fmt.Println("Tick at ", t)
	}
}

func main() {
	t := time.NewTicker(time.Millisecond * 500)
	go ticker(t.C)

	time.Sleep(time.Second * 5)
	t.Stop()
	fmt.Println("Ticker stopped")
}
