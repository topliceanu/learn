package main

import (
	"fmt"
	"time"
)

func main() {
	done := make(chan bool)

	fmt.Println("Start the timer")
	timer := time.NewTimer(time.Second * 2)
	stopper := time.NewTimer(time.Second * 1)

	go func() {
		<-stopper.C
		fmt.Println("Stop the timer")
		timer.Stop()
		done<- true
	}()

	<-done
	fmt.Println("fin!")
}
