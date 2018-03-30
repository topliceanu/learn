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

func Solution(A []int, B []int) int {
	// Maintain a stack of fish going downstream: when a fish is going downstream, push it to the stack.
	// When a fish goes upstream:
	// - pop all the fish in the stack it will eat.
	// - if the stack ends up empty, then the upstream fish will survive, so increment the count
	// Add to the count the length of the stack, ie all fish going downstream which haven't been eaten.
	count := 0
	downstream := empty
	for i := 0; i < len(A); i ++ {
		size := A[i]
		isDownstream := B[i] == 1
		if isDownstream {
			downstream = downstream.push(i)
			continue
		}
		var isEmpty bool
		var j int
		for {
			isEmpty, j = downstream.peek()
			if isEmpty || A[j] >= size {
				break
			}
			isEmpty, _, downstream = downstream.pop()
		}
		if isEmpty || A[j] == size {
			count += 1
		}
	}
	return count + downstream.size()
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

func (n *node) size() int {
	if n == empty {
		return 0
	}
	return 1 + n.next.size()
}

func main() {}
