package main

import (
	"fmt"
	"time"
)

type Subscription interface {
	Updates() <-chan int // stream of Items
	Close()              // shuts down the stream
}

type S struct {
	id int
	ticker *time.Ticker
	updates chan int
}

func NewS(id int, interval time.Duration) Subscription {
	s := &S{
		id: id,
		ticker: time.NewTicker(interval),
		updates: make(chan int),
	}
	go func() {
		for _ = range s.ticker.C {
			s.updates<- s.id
		}
	}()
	return s
}

func (s *S) Updates() <-chan int {
	return s.updates
}

func (s *S) Close() {
	s.ticker.Stop()
}

type M struct {
	s1 Subscription
	s2 Subscription
	stop chan struct{}
}

func (m *M) Updates() <-chan int {
	out := make(chan int)
	c1 := m.s1.Updates()
	c2 := m.s2.Updates()

	go func() {
		for {
			select {
			case i1 := <-c1:
				out<- i1
			case i2 := <-c2:
				out<- i2
			case <-m.stop:
				return
			}
		}
	}()
	return out
}
func (m *M) Close() {
	m.s1.Close()
	m.s2.Close()
	m.stop<- struct{}{}
}

func Merge(subs ...Subscription) Subscription {
	if len(subs) == 1 {
		return subs[0]
	} else if len(subs) == 2 {
		return &M{subs[0], subs[1], make(chan struct{})}
	} else {
		m1 := Merge(subs[:len(subs)/2]...)
		m2 := Merge(subs[len(subs)/2:]...)
		return &M{m1, m2, make(chan struct{})}
	}
}

func main() {
	/*
	s := NewS(1, time.Second)
	go func() {
		for i := range s.Updates() {
			fmt.Println(i)
		}
	}()
	time.Sleep(10 * time.Second)
	s.Close()
	*/

	/*
	s1 := NewS(1, time.Second)
	s2 := NewS(2, time.Second)
	s := Merge(s1, s2)

	go func() {
		for i := range s.Updates() {
			fmt.Println(i)
		}
	}()

	time.Sleep(10 * time.Second)
	s.Close()
	*/


	s1 := NewS(1, time.Second)
	s2 := NewS(2, time.Second)
	s3 := NewS(3, time.Second)
	s4 := NewS(4, time.Second)
	s5 := NewS(5, time.Second)
	s6 := NewS(6, time.Second)
	s7 := NewS(7, time.Second)
	s8 := NewS(8, time.Second)

	s := Merge(s1, s2, s3, s4, s5, s6, s7, s8)

	go func() {
		for update := range s.Updates() {
			fmt.Println(update)
		}
	}()

	time.Sleep(10 * time.Second)
	s.Close()

}
