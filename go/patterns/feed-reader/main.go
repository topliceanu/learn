package main

import (
	"fmt"
	"time"
)

type Item struct {
	Title, Channel, GUID string
}

// What I have.
type Fetcher interface {
	Fetch() (items []Item, next time.Time, err error)
}

// What I want.
type Subscription interface {
	Updates() <-chan Item
	Close() error
}

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
