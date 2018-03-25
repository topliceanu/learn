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

import "sort"

// Solution from here: https://stackoverflow.com/a/4801275/993508
func Solution(A []int) int {
	cs := make(circles, len(A))
	for c, r := range A {
		cs[c] = &circle{
			left: max(0, c - r),
			right: min(c + r, len(A) - 1),
		}
	}
	sort.Sort(cs) // O(NlogN)
	lefts := cs.lefts()
	count := 0
	for i, c := range cs {
		k := sort.SearchInts(lefts, c.right)
		add := k - i - 1
		count += add
	}
	return count
}

type circle struct {
	left, right int
}

type circles []*circle

func (c circles) Len() int {
	return len(c)
}

func (c circles) Less(i, j int) bool {
	if c[i].left < c[j].left {
		return true
	}
	if c[i].left == c[j].left && c[i].right < c[j].right {
		return true
	}
	return false
}

func (c circles) Swap(i, j int) {
	c[i], c[j] = c[j], c[i]
}

func (c circles) lefts() []int {
	out := make([]int, len(c))
	for i, j := range c {
		out[i] = j.left
	}
	return out
}

func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}

func min(i, j int) int {
	if i > j {
		return j
	}
	return i
}

func main() {}
