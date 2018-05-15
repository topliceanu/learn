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

import "fmt"
import "os"
import "math"

func main() {
	var T, R, C, H, V int
	var line string
	if _, err := fmt.Fscanln(os.Stdin, &T); err != nil {
		panic(err)
	}
	//fmt.Fprintln(os.Stderr, ">>>> T=", T)
	for i := 1; i <= T; i ++ {
		if _, err := fmt.Fscanf(os.Stdin, "%d%d%d%d", &R, &C, &H, &V); err != nil {
			panic(err)
		}
		//fmt.Fprintln(os.Stderr, ">>>> R, C, H, V", R, C, H, V)
		A := make([][]int, R)
		for j := 0; j < R; j ++ {
			if _, err := fmt.Fscan(os.Stdin, &line); err != nil {
				panic(err)
			}
			A[j] = make([]int, C)
			for k := 0; k < C; k ++ {
				a := line[k]
				//fmt.Fprintln(os.Stderr, ">>>>", a)
				if a == '@' {
					A[j][k] = 1
				} else {
					A[j][k] = 0
				}
			}
		}
		//fmt.Fprintln(os.Stderr, ">>>>", A)
		s := Solution(A, R, C, H, V)
		var output string
		if s {
			output = "POSSIBLE"
		} else {
			output = "IMPOSSIBLE"
		}
		if _, err := fmt.Fprintf(os.Stdout, "Case #%d: %s", i+1, output); err != nil {
			panic(err)
		}
	}
}

func Solution(A [][]int, R, C, H, V int) bool {
	if float64(R * C) / float64(H + 1) / float64(V + 1) != math.Floor(float64(R * C) / float64(H + 1) / float64(V + 1)) {
		return false
	}
	return true
}
