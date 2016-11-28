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
	time.AfterFunc(3 * time.Second, func() {
		merged.Close()
		fmt.Println("closed!")
	})
	for i := range merged.Updates() {
		fmt.Println(i.Channel, i.Title)
	}
	panic("Show me the stacks!")
}
