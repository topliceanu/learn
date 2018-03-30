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

func Solution(H []int) int {
	stack := end
	count := 0
	for i := 0; i < len(H); i ++ {
		if stack == end {
			stack = stack.push(H[i])
			count += 1
			continue
		}
		isEmpty, head := stack.peek()
		if isEmpty || H[i] > head {
			stack = stack.push(H[i])
			count += 1
			continue
		}
		for !isEmpty && head > H[i] {
			_, _, stack = stack.pop()
			isEmpty, head = stack.peek()
		}
		if isEmpty || H[i] != head {
			stack = stack.push(H[i])
			count += 1
		}
	}
	return count
}

// quick stack implementation.
type node struct {
	val int
	next *node
}

var end = &node{0, nil}

func (n *node) debug() string {
	if n == end {
		return "|"
	}
	return fmt.Sprintf("%d - %s", n.val, n.next.debug())
}

func (n *node) push(i int) *node {
	return &node{i, n}
}

func (n *node) pop() (isEmpty bool, val int, newHead *node) {
	if n == end {
		return true, 0, end
	}
	return false, n.val, n.next
}

func (n *node) peek() (isEmpty bool, val int) {
	if n == end {
		return true, 0
	}
	return false, n.val
}

func main() {}
