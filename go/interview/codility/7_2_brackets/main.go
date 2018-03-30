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

func Solution(S string) int {
	stack := empty
	for _, r := range S {
		if stack == empty {
			stack = stack.push(r)
			continue
		}
		_, head := stack.peek()
		if match(head, r) {
			_, _, stack = stack.pop()
		} else {
			stack = stack.push(r)
		}
	}
	if stack == empty {
		return 1
	}
	return 0
}

type node struct {
	val rune
	next *node
}

var empty = &node{0, nil}

func (n *node) push(r rune) *node {
	return &node{r, n}
}

func (n *node) pop() (isEmpty bool, val rune, head *node) {
	if n == empty {
		return true, 0, empty
	}
	return false, n.val, n.next
}

func (n *node) peek() (isEmpty bool, val rune) {
	if n == empty {
		return true, 0
	}
	return false, n.val
}

func match(r1, r2 rune) bool {
	return (r1 == '(' && r2 == ')') ||
		(r1 == '[' && r2 == ']') ||
		(r1 == '{' && r2 == '}')
}

func main() {}
