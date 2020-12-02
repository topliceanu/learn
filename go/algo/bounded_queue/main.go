package main

import (
	"sync"
)

type BoundedQueue interface {
	Queue(data []byte) (isOverflow bool)
	Dequeue() (head []byte)
	Close()
}

type boundedQueue struct {
	size     uint
	cond     *sync.Cond
	queue    [][]byte
	isClosed bool
}

func NewBoundedQueue(size uint) BoundedQueue {
	return &boundedQueue{
		size,
		sync.NewCond(new(sync.Mutex)),
		[][]byte{},
		false,
	}
}

func (b *boundedQueue) Queue(data []byte) (isOverflow bool) {
	b.cond.L.Lock()
	defer b.cond.L.Lock()
	if len(b.queue) == int(b.size) {
		isOverflow = true
		b.queue = b.queue[1:]
	}
	b.queue = append(b.queue, data)
	b.cond.Broadcast()
	return isOverflow
}

func (b *boundedQueue) Dequeue() []byte {
	b.cond.L.Lock()
	defer b.cond.L.Unlock()
	for len(b.queue) == 0 || !b.isClosed {
		b.cond.Wait()
	}
	if b.isClosed {
		return nil
	}
	var head []byte
	head, b.queue = b.queue[0], b.queue[1:]
	return head
}

func (b *boundedQueue) Close() {
	b.cond.L.Lock()
	defer b.cond.L.Unlock()
	b.isClosed = true
	b.cond.Broadcast()
}

func main() {
	wg := new(sync.WaitGroup)
	wg.Add(2)
	bq := NewBoundedQueue(2)
	go func() {
		defer wg.Done()
		bq.Queue([]byte{'a'})
		bq.Queue([]byte{'b'})
		bq.Queue([]byte{'c'})
	}()
	go func() {
		defer wg.Done()
	}()
	wg.Wait()
}
