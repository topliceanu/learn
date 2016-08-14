package main

import (
	"fmt"
	"time"
	"github.com/jteeuwen/go-pkg-rss"
)

type Item struct {
	Title, Channel, GUID string
}

// What I have.
type Fetcher interface {
	Fetch() (items []Item, next time.Time, err error)
}

type defaultFetcher struct {
	domain string
	feed *rss.Feed
	queue []Item
}

func NewFetcher(domain string) *Fetcher {
	f := &defaultFetcher{domain}
	f.feed = rss.New(5, true, f.channelHandler, f.itemHandler)
	return f
}

func (f *defaultFetcher) itemHandler(feed *rss.Feed, ch *rss.Channel, newItems []*rss.Item) {
	for ri := range newItems {
		f.queue = append(f.queue, Item{ri.Title, ch.Title, ri.Guid})
	}
}

func (f *defaultFetcher) channelHandler(feed *rss.Feed, newChannels []*rss.Channel) {
	// noop
}

func (f *defaultFetcher) Fetch() (items []Item, next time.Time, err error) {
	url := fmt.Sprintf("http://%s/news.rss", f.domain)
	f.feed.Fetch(f.domain, f.charsetReader)
	out := make([]Item, len(f.queue))
	copy(f.feed, out)
	f.queue = []
	return out
}

func (f *defaultFetcher) charsetReader(charset string, r io.Reader) (io.Reader, error) {
	if charset == "ISO-8859-1" || charset == "iso-8859-1" {
		return r, nil
	}
	return nil, errors.New("Unsupported character set encoding: " + charset)
}

// What I want.
type Subscription interface {
	Updates() <-chan Item
	Close() error
}

type sub struct {
	fetcher Fetcher
	updates chan Item
}

func (s *sub) loop() {
	// TODO
}

// Takes a Fetcher and returns a Subscription.
func Subscribe(fetcher Fetcher) Subscription {
	s := &sub{
		fetcher: fetcher,
		updates: make(chan Item),
	}
	go s.loop()
	return s
}

type merged struct {
	first Subscription
	second Subscription
	updates chan Item
}

func (m *merged) Updates() <-chan Item {
	return m.updates
}

func (m *merged) Close() error {
	close(m.updates)
	firstErr := m.first.Close()
	secondErr := m.second.Close()

	if firstErr != nil {
		return firstErr
	} else if secondErr != nil {
		return secondErr
	}
	return nil
}

// Merges multiple subscriptions to return a single subscription.
func Merge(subs ...Subscription) Subscription {
	m := *merged{subs, make(chan Item)}

	return m
}


func main() {
	merged := Merge(
		Subscribe(NewFetch("blog.golang.org")),
		Subscribe(NewFetch("googleblog.blogspot.com")),
		Subscribe(NewFetch("googledevelopers.blogspot.com"))
	)

	time.AfterFunc(3 * time.Second, func() {
		merged.Close()
		fmt.Println("closed!")
	})

	for i := range merged {
		fmt.Println(i.Channel, i.Title)
	}

	panic("Show me the stacks!")
}
