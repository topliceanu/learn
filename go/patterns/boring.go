package main

import (
	"fmt"
	"math/rand"
	"time"
)

func boring(msg string, quit chan string) <-chan string {
	c := make(chan string)
	go func() {
		for i := 0; ; i += 1 {
			select {
			case c <- fmt.Sprintf("%s: %d", msg, i):
			case <-quit:
				fmt.Println("Boring cleanup")
				quit <- "See you"
				return
			}
		}
	}()
	return c
}

func main() {
	rand.Seed(time.Now().Unix())
	quit := make(chan string)
	c := boring("Joe", quit)
	for i := rand.Intn(10); i >= 0; i-- {
		fmt.Println(<-c)
	}
	quit <- "Bye!"
	fmt.Printf("Joe says %q\n", <-quit)
}
