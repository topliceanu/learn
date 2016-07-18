package main

import (
	"fmt"
	"math/rand"
	"time"
)

func init() {
	rand.Seed(time.Now().Unix())
}

type Item struct {
	GUID, Channel, Title string
}

type Fetcher interface {
	Fetch() (items []Item, next time.Time, err error)
}

type myFetcher struct {
	domain string
	cnt    int
}

func (f *myFetcher) Fetch() (items []Item, next time.Time, err error) {
	items = []Item{
		Item{rand.Intn(10000), f.domain, fmt.Sprintf("Item %d", f.cnt)},
		Item{rand.Intn(10000), f.domain, fmt.Sprintf("Item %d", f.cnt+1)},
		Item{rand.Intn(10000), f.domain, fmt.Sprintf("Item %d", f.cnt+2)},
	}
	f.cnt += 3
	next = time.Now().Add(time.Duration(60 * time.Second))
	return items, next, nil
}

// Fetches items from a domain.
func Fetch(domain string) Fetcher {
	return &myFetcher{domain, 0}
}

type Subscription interface {
	Updates() <-chan Item
	Close() error
}

func Subscribe(fetcher Fetcher) Subscription {
	s := &sub{
		fetcher: fetcher,
		updates: make(chan Item),
	}
	go s.loop()
	return s
}

// Implements the Subscription interface
type sub struct {
	closing chan chan error // request-response pattern
	err     error
	fetcher Fetcher
	updates chan Item
}

// periodically call Fetch.
// send fetched items on the Updates channel.
// exit when Close is called, reporting any error.
func (s *sub) loop() {
	// declare mutable state owned by the goroutine.
	var pending []Item
	var next time.Time
	var err error
	var seen = make(map[string]bool)

	for {
		// set up channels for the cases.
		var first Item
		var updates chan Item
		if len(pending) > 0 {
			first = pending[0]
			updates = s.updates
		}

		var fetchDaily time.Duration
		if now := time.Now(); next.After(now) {
			fetchDelay = next.Sub(now)
		}
		startFetch := time.After(fetchDelay)

		select {
		// read/write the state.
		case errc := <-s.closing:
			errc <- err
			close(s.updates)
			return
		case <-startFetch:
			var fetched []Item
			fetched, next, err = s.fetcher.Fetch()
			if err != nil {
				next = time.Now().Add(10 * time.Second)
				break
			}
			for _, item := range fetched {
				if !seen[item.GUID] {
					pending = append(pending, item)
					seen[item.GUID] = true
				}
			}
		case updates <- first:
			pending = pending[1:]
		}
	}
}

func (s *sub) Updates() <-chan Item {
	return s.updates
}

func (s *sub) Close() error {
	errc := make(chan error)
	s.closing <- errc
	return <-errc
}

func Merge(subs ...Subscription) Subscription {
	//TODO
}

func main() {
	merged := Merge(
		Subscribe(Fetch("blog.golang.org")),
		Subscribe(Fetch("googlebot.glogspot.com")),
		Subscribe(Fetch("googledevelopers.blogspot.com")),
	)

	time.AfterFunc(3*time.Second, func() {
		fmt.Println("Closed:", merged.Close())
	})

	for item := range merged.Updates() {
		fmt.Println(item.Channel, item.Title)
	}
	panic("show me the stacks")
}
