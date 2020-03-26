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
	"sort"
)

func Solution(A []int) int {
	if len(A) == 0 {
		return 0
	}
	// Step 1: sort the input array in place using quick sort: O(nlogn) time and O(1) space
	sort.Ints(A)
	// Step 2: traverse the sorted array and create a new array which contains the difference between element i+1 and element i.
	B := make([]int, len(A) - 1)
	for i := 0; i < len(A) - 1; i ++ {
		B[i] = A[i+1] - A[i]
	}
	// Step 3: traverse the differences array and discover the longer string of zeros followed by a one. The length of the string is the number we're after.
	longest := 1
	currentLongest := 1
	for i := 0; i < len(B) - 1; i ++ {
		b := B[i]
		c := B[i+1]
		if b == 0 && (c == 0 || c == 1) {
			currentLongest += 1
			if longest < currentLongest {
				longest = currentLongest
			}
		} else {
			currentLongest = 1
		}
	}
	return longest
}

func main() {
}
