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

func Solution(S string, P []int, Q []int) []int {
	pA := make([]int, len(S))
	pC := make([]int, len(S))
	pG := make([]int, len(S))
	for i, s := range S {
		switch s {
		case 'A':
			pA[i] = 1
		case 'C':
			pC[i] = 1
		case 'G':
			pG[i] = 1
		}
		if i > 0 {
			pA[i] += pA[i-1]
			pC[i] += pC[i-1]
			pG[i] += pG[i-1]
		}
	}
	out := make([]int, len(P))
	for i, q := range Q {
		p := P[i] - 1
		if p >= 0 {
			if pA[q] - pA[p] > 0 {
				out[i] = 1
			} else if pC[q] - pC[p] > 0 {
				out[i] = 2
			} else if pG[q] - pG[q] > 0 {
				out[i] = 3
			} else {
				out[i] = 4
			}
		} else {
			if pA[q] > 0 {
				out[i] = 1
			} else if pC[q] > 0 {
				out[i] = 2
			} else if pG[q] > 0 {
				out[i] = 3
			} else {
				out[i] = 4
			}
		}
	}
	return out
}

func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}

func main() {}
