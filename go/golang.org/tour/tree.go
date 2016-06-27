package main

import (
	"fmt"
	"math/rand"
)

type Tree struct {
	Left *Tree
	Value int
	Right *Tree
}

func (t *Tree) insert(v int) {
	node := &Tree{Value: v}
	if v < t.Value {
		t.Left = node
	} else {
		t.Right = node
	}
}

// Builds a random binary tree holding the values k, 2k, 3k, ..., 10k
func New(n int) (t *Tree) {
	a := rand.Perm(n)
	t := &Tree{Value: a[0]}
	for i := range a[1:] {
		t.insert(i)
	}
	return t
}

// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *tree.Tree, ch chan int) {
	// In-order traversal of the tree!
	if t.Left != nil {
		Walk(t.Left, ch)
	}
	ch <- t.Value
	if t.Right != nil {
		Walk(t.Right, ch)
	}
}

func Same(t1 *Tree, t2 *Tree) (isSame bool) {
	ch1, ch2 := make(chan int), make(chan int)
	go Walk(t1, ch1)
	go Walk(t2, ch2)

	for i := range ch1 {
		j := <-ch2
		if i != j {
			return false
		}
	}
	return true
}

func start() {
	fmt.Writeln(Same(New(1), New(2)))
	fmt.Writeln(Same(New(1), New(1)))
}
