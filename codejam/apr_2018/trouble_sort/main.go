package main

import "fmt"
import "os"
import "sort"

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

func TroubleSort(L []int) {
	var done = false
	for !done {
		done = true
		for i := 0; i < len(L) - 2; i ++ {
			if L[i] > L[i+2] {
				done = false
				L[i], L[i+2] = L[i+2], L[i]
			}
		}
	}
}

func CheckTroubleSort(V []int) (bool, int) {
	// copy V
	N := len(V)
	Vcopy := make([]int, N)
	for i, v := range V {
		Vcopy[i] = v
	}
	sort.Ints(Vcopy)
	TroubleSort(V)
	for i := 0; i < N; i++ {
		if V[i] != Vcopy[i] {
			return false, i
		}
	}
	return true, 0
}

func main() {
	var T, N int
	if _, err := fmt.Fscanln(os.Stdin, &T); err != nil {
		panic(err)
	}
	for i := 1; i <= T; i ++ {
		if _, err := fmt.Fscanln(os.Stdin, &N); err != nil {
			panic(err)
		}
		var V = make([]int, N)
		var v int
		for j := 0; j < N; j ++ {
			if _, err := fmt.Fscan(os.Stdin, &v); err != nil {
				panic(err)
			}
			V[j] = v
		}
		isSorted, index := CheckTroubleSort(V)
		if isSorted {
			fmt.Fprintf(os.Stdout, "Case #%d: OK\n", i)
		} else {
			fmt.Fprintf(os.Stdout, "Case #%d: %d\n", i, index)
		}
	}
}
