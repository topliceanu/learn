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

func Solution(N int, A []int) []int {
	counters := make([]int, N)
	var max int = 0
	var interimMax int = 0
	for _, x := range A {
		i := x - 1
		if 1 <= x && x <= N {
			if counters[i] < max {
				counters[i] = max
			}
			counters[i] += 1
			if counters[i] > interimMax {
				interimMax = counters[i]
			}
		} else if x == N + 1 {
			max = interimMax
		}
	}
	for i, c := range counters {
		if c < max {
			counters[i] = max
		}
	}
	return counters
}

func main() {}
