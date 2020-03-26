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
	"math"
)

type Point2D struct {
	x int
	y int
}

// Solution needs to return the _number_ or rays.
func Solution(A []Point2D) int {
	if len(A) == 0 {
		return 0
	}
	// Step 1: go through each statue and compute the angles from the center. O(n) space, O(n) time.
	B := make([]float64, len(A))
	for i, p := range A {
		B[i] = computeAngle(p)
	}
	// Step 2: sort in place the angles array using quick sort. O(nlogn) time, O(1) space.
	sort.Float64s(B)
	// Step 3: count consecutive distinct angles in the sorted array.
	numDistincts := 1
	for i := 0; i < len(B) - 1; i ++ {
		b := B[i]
		c := B[i+1]
		if b != c {
			numDistincts += 1
		}
	}
	return numDistincts
}

// compute arc-tanget for each point.
// TODO add diagram.
func computeAngle(p Point2D) float64 {
	return math.Atan2(float64(p.y), float64(p.x))
}

func main() {
}
