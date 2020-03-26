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
import "strconv"

func Solution(N int) int {
	n, k := digits(N)
	fmt.Println(">>>>>", N, n, k)
	if k == 0 {
		return Perm(n)
	}
	return int(float64(Perm(n) * Perm(n-1+k)) / float64(Perm(k)))
}

func digits(N int) (nonZeros, zeros int) {
	s := strconv.Itoa(N)
	nz := make(map[rune]struct{})
	for _, c := range(s) {
		if c == '0' {
			zeros += 1
		} else {
			nz[c] = struct{}{}
		}
	}
	return len(nz), zeros
}

var memo map[int]int

func init() {
	memo = make(map[int]int)
}

func Perm(n int) int {
	if val, ok := memo[n]; ok {
		return val
	}
	if n == 0 {
		return 1
	}
	val := n * Perm(n-1)
	memo[n] = val
	return val
}

func Arange(n, k int) int {
	return int(float64(Perm(n)) / float64(Perm(n-k)))
}

func Comb(n, k int) int {
	return int(float64(Perm(n)) / float64(Perm(n-k)))
}

func main() {}
