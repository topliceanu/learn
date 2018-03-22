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

import "sort"

func Solution(A []int) int {
	if len(A) < 3 {
		return 0
	}
	sort.Ints(A)
	for i := 0; i < len(A) - 2; i ++ {
		if isTriangular(A, i, i + 1, i + 2) {
			return 1
		}
	}
	return 0
}

func isTriangular(A []int, i, j, k int) bool {
	return (A[i] + A[j] > A[k]) &&
		(A[i] + A[k] > A[j]) &&
		(A[j] + A[k] > A[i])
}

func main() {}
