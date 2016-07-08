package main

import (
	"net/http"
	"log"
)

type State struct {
	url string
	status string
}

type Resource struct {
	url string
	errCount int
}

func (r *Resource) Poll() string {
	resp, err := http.Head(r.url)
	if err != nil {
		log.Println("error ", r.url, err)
		r.errCount += 1
		return err.Error()
	}
	r.errCount = 0
	return resp.Status
}

func Poller(in <-chan *Resource, out chan<- *Resource, status chan<- State) {
	for r := range in {
		s := r.Poll()
		status <- State{r.url, s}
		out <- r
	}
}

func logState(s map[string]string) {
	log.Println("Current state:")
	for k, v := range s {
		log.Printf(" %s %s", k, v)
	}
}

func StateMonitor(updateInterval time.Duration) chan<- State {
	updates := make(chan State)
	urlStatus := make(map[string]string)

	ticker := time.NewTicker(updateInterval)
	go func() {
		for {
			select {
				select {
				case <-ticker.C:
					logState(urlStatus)
				case s := <-updates:
					urlStatus[s.url] = s.status
				}
			}
		}
	}()
	return updates
}

func main() {
	pending := make(chan *Resource)
	complete := make(chan *Resource)

	status := StateMonitor
}
