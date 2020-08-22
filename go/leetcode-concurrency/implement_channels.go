package main

/* Resources:
- https://www.youtube.com/watch?v=KBZlN0izeiY&feature=youtu.be
- https://docs.google.com/document/d/1yIAYmbvL3JxOKOjuCyon7JhW4cSv1wy5hC0ApeGMV9s/pub
-	https://stackoverflow.com/questions/19621149/how-are-go-channels-implemented
*/

import (
	"sync"
)

/*
type Chan struct {
	mu sync.Mutex
	isClosed bool
	senders []interface{}
	receivers []interface{}
}

func (c *Chan) Send(data interface{}, block bool) { // for non-buffered channels, block is always false.
	if c.isClosed {
		panic("closed")
	}
	if (!block && len(c.receivers) == 0) {
		return false // not closed but no receivers!
	}
	c.mu.Lock() // wait to aquire the lock then check again if the channels was closed in the meantime.
	if (c.isClosed) {
		c.mu.Unlock()
		panic("closed")
	}
	if len(c.receivers) != 0 {
		sg, receivers := receivers[0], receivers[1:]
		c.mu.Unlock()

	}
}
*/


import (
	"fmt"
	"sync"
)

type Chan struct {
	mu sync.Mutex
	data interface{}
}

func (ch *Chan) Write(data interface{}) {
	ch.wr.Lock()
	ch.data = data
	ch.rd.Lock()
	ch.wr.Unlock()
}

func (ch *Chan) Read() (data interface{}) {
	ch.rd.Unlock()
	ch.wr.Lock()
	return ch.data
	ch.wr.Unlock()
}


func main() {
	var ch = new(Chan)
	var done = new(Chan)
	go func(ch *Chan) {
		fmt.Printf("write\n")
		ch.Write("bla")
	}(ch)
	go func(ch *Chan) {
		data, isClosed := ch.Read()
		fmt.Printf("read %v %t\n", data, isClosed)
		done.Close()
	}(ch)
	done.Read()
}
