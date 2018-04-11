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
	sort.Ints(A)
	n := len(A)
	// last three numbers.
	x := A[n-1] * A[n-2] * A[n-3]
	if A[0] < 0 && A[1] < 0 {
		y := A[0] * A[1] * A[n-1]
		if y > x {
			return y
		}
	}
	return x
}

/*
// if all numbers are positive
func Solution(A []int) int {
	if len(A) <= 2 {
		panic("should give an array of at least 3 elements")
	}
	x, y, z := A[0], A[1], A[2]
	for i := 2; i < len(A); i ++ {
		a := A[i]
		if a > x {
			z = y
			y = x
			x = a
		} else if a > y {
			z = y
			y = a
		} else if a > z {
			z = a
		}
	}
	return x * y * z
}
*/

func main() {}
