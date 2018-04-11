package main

/*
1. think of pre-processing steps: sort, arrange the data, index the data.
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
	_"fmt"
)

func Solution(A []int) int {
	// prefix sum
	prefix := make([]int, len(A))
	for i := 0; i < len(A); i++ {
		if A[i] == 0 {
			prefix[i] = 1
		}
		if i > 0 {
			prefix[i] += prefix[i-1]
		}
	}
	count := 0
	for i := len(A) - 1; i >= 0; i-- {
		if A[i] == 1 {
			count += prefix[i]
		}
	}
	if count > 1000000000 {
		return -1
	}
	return count
}

func main() {}
