package main

import (
	"time"
)

const maxPending = 10

type Item struct {
	Title, Channel, GUID string
}

type Subscription interface {
	Updates() <-chan Item
	Close() error
}

// Takes a Fetcher and returns a Subscription.
func NewSubscription(fetcher Fetcher) Subscription {
	s := &sub{
		fetcher: fetcher,
		updates: make(chan Item),
		closing: make(chan chan error),
	}
	go s.loop()
	return s
}

// implements Subscription.
type sub struct {
	fetcher Fetcher
	updates chan Item
	closing chan chan error
}


func (s *sub) Updates() <-chan Item {
	return s.updates
}

func (s *sub) Close() error {
	// Make loop exit.
	errc := make(chan error)
	s.closing<- errc
	// Wait for the loop to finish handling the Close signal and return any error.
	return <-errc
}

type fetchResult struct{
	fetched []Item
	next time.Time
	err error
}

func (s *sub) loop() {
	var err error
	var next = time.Now()
	var pending []Item
	var seen = make(map[string]bool)
	var fetchDone chan fetchResult // if non-nil, Fetch is running.

	for {
		// handle fetching after a predefined interval.
		var fetchDelay time.Duration
		if now := time.Now(); next.After(now) {
			fetchDelay = next.Sub(now)
		}
		startFetch := time.After(fetchDelay)
		// make sure we only fetch when we have space in our pending queue.
		if fetchDone == nil && len(pending) < maxPending {
			startFetch = time.After(fetchDelay)
		}

		// handle reading from the updates channel.
		var first Item
		var updates chan Item // default to nil.
		if len(pending) > 0 {
			first = pending[0]
			updates = s.updates // enable send case.
		}

		select {
		case <-startFetch:
			// fetching data from the feed.
			fetchDone = make(chan fetchResult, 1)
			go func() {
				fetched, next, err := s.fetcher.Fetch()
				fetchDone<- fetchResult{fetched, next, err}
			}()
		case f := <-fetchDone:
			fetchDone = nil
			for _, item := range f.fetched {
				if !seen[item.GUID] {
					pending = append(pending, item)
					seen[item.GUID] = true
				}
			}
		case errc := <-s.closing:
			// closing the loop.
			close(s.updates)
			errc<- err
			return
		case updates<- first:
			pending = pending[1:]
		}
	}
}
