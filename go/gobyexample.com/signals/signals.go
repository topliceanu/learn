package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	signals := make(chan os.Signal)
	done := make(chan bool)

	signal.Notify(signals, syscall.SIGINT, syscall.SIGTERM)

	go func() {
		sig := <-signals
		fmt.Printf("Received signal %v\n", sig)
		done <- true
	}()

	fmt.Println("Awaiting signal")
	<-done
	fmt.Println("Exiting")
}
