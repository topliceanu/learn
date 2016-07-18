package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Result string

type Search func(query string) Result

func fakeSearch(kind string) Search {
	return func(query string) Result {
		time.Sleep(time.Duration(rand.Intn(100)) * time.Millisecond)
		return Result(fmt.Sprintf("%s result for %q\n", kind, query))
	}
}

// These are all functions that receive a query string and return a Result.
var (
	Web1   = fakeSearch("web")
	Web2   = fakeSearch("web")
	Image1 = fakeSearch("image")
	Image2 = fakeSearch("image")
	Video1 = fakeSearch("video")
	Video2 = fakeSearch("video")
)

func First(query string, replicas ...Search) Result {
	c := make(chan Result)
	for i := range replicas {
		go func(i int) {
			c <- replicas[i](query)
		}(i)
	}
	return <-c
}

func Google(query string) []Result {
	c := make(chan Result)

	go func() { c <- First(query, Web1, Web2) }()
	go func() { c <- First(query, Image1, Image2) }()
	go func() { c <- First(query, Video1, Video2) }()

	results := make([]Result, 3)
	timeout := time.After(80 * time.Millisecond)

	for i := 0; i < 3; i += 1 {
		select {
		case result := <-c:
			results = append(results, result)
		case <-timeout:
			fmt.Println("time out")
		}
	}
	return results
}

func main() {
	rand.Seed(time.Now().Unix())

	start := time.Now()
	results := Google("golang")
	elapsed := time.Since(start)
	fmt.Println(results, elapsed)
}
