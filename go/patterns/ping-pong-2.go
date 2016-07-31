package main

import "fmt"
import "time"

func player(t chan int, index int) {
	for ball := range t {
		fmt.Printf("player %d received ball %d\n", index, ball)
		ball += 1
		time.Sleep(50 * time.Millisecond)
		t<- ball
	}
}

func main() {
	ball := 0
	table := make(chan int)

	for i := 1; i <= 100; i += 1{
		go player(table, i)
	}

	table<- ball
	time.Sleep(5 * time.Second)
	<-table
}
