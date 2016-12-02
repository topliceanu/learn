package main

import (
	"errors"
	"fmt"
	"io"
	"strconv"
	"time"
)

// Fetcher is an interface for a thing that know how to fetch Items from a feed.
type Fetcher interface {
	Fetch() (items []Item, next time.Time, err error)
}

func NewFetcher(domain string) Fetcher {
	return &fetcher{domain, 0}
}

type fetcher struct {
	domain  string
	counter int
}

func (f *fetcher) Fetch() (items []Item, next time.Time, err error) {
	next = time.Now().Add(5 * time.Second)
	items = make([]Item, 5)
	for i := 1; i <= 5; i += 1 {
		guid := f.counter + i
		items[i-1] = Item{
			GUID:    strconv.Itoa(guid),
			Channel: fmt.Sprintf("Channel-%s", f.domain),
			Title:   fmt.Sprintf("Item(%d) in feed %s", guid, f.domain),
		}
	}
	f.counter += 5
	return items, next, err
}

func (f *fetcher) charsetReader(charset string, r io.Reader) (io.Reader, error) {
	if charset == "ISO-8859-1" || charset == "iso-8859-1" {
		return r, nil
	}
	return nil, errors.New("Unsupported character set encoding: " + charset)
}
