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
	var T, N, P int
	var line string
	if _, err := fmt.Fscanln(os.Stdin, &T); err != nil {
		panic(err)
	}
	//fmt.Fprintln(os.Stderr, ">>>> T=", T)
	for i := 1; i <= T; i ++ {
		if _, err := fmt.Fscanf(os.Stdin, "%d%d", &N, &P); err != nil {
			panic(err)
		}
		//fmt.Fprintln(os.Stderr, ">>>> N, P", N, P)
		A := make([][]int, N)
		for j := 0; j < N; j ++ {
			var W, H int
			if _, err := fmt.Fscanf(os.Stdin, "%d %d", &W, &H); err != nil {
				panic(err)
			}
			A[j] = make([]int, 2)
			A[j][0] = W
			A[j][1] = H
		}
		//fmt.Fprintln(os.Stderr, ">>>>", A)
		s := Solution(A, P)
		//fmt.Fprintln(os.Stderr, ">>>>", s)
		if _, err := fmt.Fprintf(os.Stdout, "Case #%d: %.6f", i+1, s); err != nil {
			panic(err)
		}
	}
}

type per struct {
	min, max float64
}

func Solution(A [][]int, P float64) float64 {
	var N = len(A)
	var cp float64 // current perimeter
	var B = make([]*per, N)
	for i := 0; i < N; i ++ {
		cp += float64(A[i][0] * A[i][1])
		B[i] = &per{
			min: minimum(A[i][0], A[i][1]),
			max: math.Sqrt(A[i][0]*A[i][0] + A[i][1]*A[i][1]),
		}
	}
	target = P - cp
	if target < 0 {
		return cp
	}
	// knapsack
	var V = make([][]float64, N+1)
	for i := 0; i <= N; i ++ {
		V[i] = make([]float64, int(math.Floor(target)))
	}
	for i := 1, i <= N; i ++ {
		for x := 0; x <= math.Floor(target); x ++ {
			if B[i].min >= x {
				V[i][x] = V[i-1][x]
			} else if B[i].min < x && x <= B[i].max {
				V[i][x] = x
			} else if B[i].min < x && B[i].max < x {
				V[i][x] = B[i].max
			}
		}
	}
	return 0
}

