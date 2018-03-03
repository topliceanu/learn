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
	"fmt"
)

func Solution(n int) int {
	var (
		i int
		b string // string representation of the binary n
		c int // counter of zeros.
		s bool // whether the current bit is true or false.
		mc int // max count of zeros so far.
	)
	b = fmt.Sprintf("%b", n)
	for i = 0; i < len(b); i ++ {
		s = b[i] == '1'
		if s == true {
			if c > mc {
				mc = c
			}
			c = 0
		} else {
			c++
		}
		fmt.Printf("i:%d, s: %t, c: %d, mc: %d\n", i, s, c, mc)
	}
	return mc
}

func main() {
}
