package main

import (
	"fmt"
	"time"
)

func main() {
	merged := Merge(
		NewSubscription(NewFetcher("blog.golang.org")),
		NewSubscription(NewFetcher("highscalability.com")),
		NewSubscription(NewFetcher("spectruum.iee.com")),
	)
	time.AfterFunc(3*time.Second, func() {
		err := merged.Close()
		fmt.Printf("closed with error: %v\n", err)
	})
	for i := range merged.Updates() {
		fmt.Println(i.Channel, i.Title)
	}
	panic("Show me the stacks!")
}
