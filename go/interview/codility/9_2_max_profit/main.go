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

func Solution(A []int) int {
	if len(A) == 0 {
		return 0
	}
	B := make([]int, len(A))
	B[0] = 0
	for i := 1; i < len(A); i ++ {
		B[i] = max(A[i] - A[i-1], B[i-1] - A[i-1] + A[i])
	}
	m := B[0]
	for i := 0; i < len(B); i ++ {
		if m < B[i] {
			m = B[i]
		}
	}
	return m
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {}
