package main

import (
	"fmt"
)

var foo_ch, bar_ch, done_ch chan struct{}

func init() {
	foo_ch = make(chan struct{})
	bar_ch = make(chan struct{})
	done_ch = make(chan struct{})
}

func foo() {
	for i := 0; i < 10; i ++ {
		<-foo_ch
		fmt.Println("foo", i)
		bar_ch<- struct{}{}
	}
}

func bar() {
	for i := 0; i < 10; i ++ {
		<-bar_ch
		fmt.Println("bar", i)
		foo_ch<- struct{}{}
	}
	close(done_ch)
}

func main() {
	go foo()
	go bar()
	foo_ch<- struct{}{}
	<-done_ch
	close(foo_ch)
	close(bar_ch)
}
