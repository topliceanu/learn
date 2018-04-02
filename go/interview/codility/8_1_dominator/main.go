package main

/*
1. think of pre-processing steps: sort, arrange the data, index the data, prefix sums!
2. split into small functions which you will implement later
3. solution scanning and offer alternatives (always talk about complexity in space and time)
	1. pattern matching (find similar problems)
	2. simplify and generalize (start with a simpler problem)
	3. iterate through programming paradigms (greedy, divide and conquer, dynamic programming)
	4. iterate through all data structures (lists, arrays, stacks, queues, heap, hash, tree, trie, bloom filter, union_find)
	5. try free primitive and see if you make progress (sorting, bfs, dfs, strongly connected components, shortest path)
4. BUD optimisation:
	1. bottleneck
	2. unnecessary work
	3. duplicate work
5. identify pain points: array indices, loop termination conditions.
*/

import "fmt"
import "math"

func Solution(A []int) int {
	stack := empty
	for _, a := range A {
		stack = stack.push(a)
		isPartial, b, c := stack.doublePeek()
		if !isPartial && b != c {
			_, _, stack = stack.pop()
			_, _, stack = stack.pop()
		}
	}
	isEmpty, candidate := stack.peek()
	if isEmpty {
		return -1
	}
	count := 0
	index := 0
	for i, a := range A {
		if a == candidate {
			count += 1
			index = i
		}
	}
	if count >= int(math.Floor(float64(len(A)) / 2)) + 1 {
		return index
	}
	return -1
}

type node struct {
	val int
	next *node
}

var empty = &node{0, nil}

func (n *node) debug() string {
	if n == empty {
		return "|"
	}
	return fmt.Sprintf("%d->%s", n.val, n.next.debug())
}

func (n *node) peek() (isEmpty bool, val int) {
	if n == empty {
		return true, 0
	}
	return false, n.val
}

func (n *node) pop() (isEmpty bool, val int, head *node) {
	if n == empty {
		return true, 0, empty
	}
	return false, n.val, n.next
}

func (n *node) push(val int) *node {
	return &node{val, n}
}

func (n *node) doublePeek() (isPartial bool, h1, h2 int) {
	isEmpty, h1 := n.peek()
	if isEmpty {
		return true, 0, 0
	}
	isEmpty, h2 = n.next.peek()
	if isEmpty {
		return true, h1, 0
	}
	return false, h1, h2
}

func main() {}
