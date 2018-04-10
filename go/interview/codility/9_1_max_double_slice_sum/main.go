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
	// idea: build B array, B[i] the largest sum leading to element i, excluding the edges.
	// build C array, C[i] the larget sum up to element i, excluding the edges.
	// find the i for which B[i-1] + C[i+1] is max.
	n := len(A)
	var B = make([]int, n)
	B[0] = 0
	B[1] = A[1]
	for i := 2; i < n; i ++ {
		B[i] = max(B[i-1] + A[i], A[i])
	}
	var C = make([]int, n)
	C[n - 1] = 0
	C[n - 2] = A[n - 2]
	for i := n - 3; i >= 0; i -- {
		C[i] = max(C[i+1] + A[i], A[i])
	}
	M := B[0] + C[2]
	for i := 1; i <= n - 2; i ++ {
		if M < B[i-1] + C[i+1] {
			M = B[i-1] + C[i+1]
		}
	}
	return M
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {}
