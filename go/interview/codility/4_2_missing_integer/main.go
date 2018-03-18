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

func Solution(A []int) int {
	counts := make([]bool, 0)
	for _, a := range A {
		if a >= 0 {
			counts = count(counts, a)
		}
	}
	var i int
	for i = 1; i < len(counts); i ++ {
		if !counts[i] {
			return i
		}
	}
	return i
}

func count(c []bool, a int) []bool {
	for len(c) - 1 < a {
		c = append(c, false)
	}
	c[a] = true
	return c
}

func main() {}
