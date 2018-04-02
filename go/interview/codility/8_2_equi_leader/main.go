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

import (
	"math"
	"fmt"
)

// First step: find the leader of the array. The equileader can only be the leader of the array.
// Second: prefix count of occurances of the leader at each index in the array.
// Third and last: find indexes where the number of occurances is larger than half the elements on the both sides of the array.
func Solution(A []int) int {
	exists, l := leader(A) // O(N)
	if !exists {
		return 0
	}
	p := prefixes(A, l) // O(N)
	count := 0
	for i := 0; i < len(A) - 1; i ++ {
		if p[i] == 0 { // no occurances
			continue
		}
		if p[i] < int(math.Ceil(float64(i)/2)) + 1 { // not a leader
			continue
		}
		c := p[len(A)-1] - p[i]
		if c == 0 { // no occurances
			continue
		}
		if c < int(math.Floor(float64(len(A) - i - 1)/2)) + 1 { // not a leader
			continue
		}
		count += 1
	}
	return count
}

// computes the leader of A.
func leader(A []int) (bool, int) {
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
		return false, 0
	}
	count := 0
	for _, a := range A {
		if a == candidate {
			count++
		}
	}
	return (count >= int(math.Floor(float64(len(A))/2)) + 1), candidate
}

// counts occurances of l in A.
func prefixes(A []int, l int) []int {
	pref := make([]int, len(A))
	for i := 0; i < len(A); i ++ {
		if A[i] == l {
			pref[i] = 1
		}
		if i > 0 {
			pref[i] += pref[i-1]
		}
	}
	return pref
}

// a simple stack implementation.
type node struct {
	val int
	next *node
}

var empty = &node{0, nil}

func (n *node) push(val int) (newHead *node) {
	return &node{val, n}
}

func (n *node) pop() (isEmpty bool, val int, newHead *node) {
	if n == empty {
		return true, 0, empty
	}
	return true, n.val, n.next
}

func (n *node) peek() (isEmpty bool, val int) {
	if n == empty {
		return true, 0
	}
	return false, n.val
}

func (n *node) doublePeek() (isPartial bool, val1, val2 int) {
	if n == empty {
		return true, 0, 0
	}
	if n.next == empty {
		return true, n.val, 0
	}
	return false, n.val, n.next.val
}

func (n *node) debug() string {
	if n == empty {
		return "|"
	}
	return fmt.Sprintf("%d-%s", n.val, n.next.debug())
}

func main() {}
