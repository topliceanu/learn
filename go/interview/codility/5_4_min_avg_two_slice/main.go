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

import "fmt"

func Solution(A []int) int {
	pref := prefixes(A)
	_, minp := recur(pref, 0, len(A) - 1)
	return minp
}

func recur(pref []int, p, q int) (min float64, minp int) {
	if p + 1 == q {
		return avg(pref, p, q), p
	}
	all := avg(pref, p, q)
	left := avg(pref, p, q - 1)
	right := avg(pref, p + 1, q)
	fmt.Println(">>>>>", p, q, all, left, right)
	if all < minimum(left, right) {
		return all, p
	} else if left < minimum(all, right) {
		return recur(pref, p, q - 1)
	} else if right < minimum(all, left) {
		return recur(pref, p + 1, q)
	} else { // all equal
		return all, p
	}
}

func prefixes(A []int) []int {
	prefixes := make([]int, len(A))
	for i, a := range A {
		prefixes[i] = a
		if i > 0 {
			prefixes[i] += prefixes[i-1]
		}
	}
	return prefixes
}

func avg(pref []int, p, q int) float64 {
	if p == 0 {
		return float64(pref[q]) / float64(q + 1)
	}
	return float64(pref[q] - pref[p-1]) / float64(q - p + 1)
}

func minimum(l, r float64) float64 {
	if l < r {
		return l
	}
	return r
}

/*
func Solution(A []int) int {
	prefixes := make([]int, len(A))
	for i, a := range A {
		prefixes[i] = a
		if i > 0 {
			prefixes[i] += prefixes[i-1]
		}
	}
	p, q := 0, len(A) -1
	min := prefixes(q)
	minp := 0
	for p < q {
		avg := (prefixes[q] - prefixes[p]) / (q - p + 1)
		if avg < min {
			min = avg
			minp = p
		}
		lavg :=
		ravg :=
	}
	return 0
}
*/

func main() {}
