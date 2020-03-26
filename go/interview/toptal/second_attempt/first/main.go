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

type Tree struct {
	X int
	L *Tree
	R *Tree
}

func Solution(T *Tree) int {
	set := make(map[int]struct{})
	set[T.X] = struct{}{}
	return bfs(T, set)
}

func bfs(t *Tree, values map[int]struct{}) int {
	if t.L == nil && t.R == nil {
		return len(values)
	}
	values[t.X] = struct{}{}
	if t.L == nil {
		return bfs(t.R, values)
	}
	if t.R == nil {
		return bfs(t.L, values)
	}
	maxL := bfs(t.L, values)
	maxR := bfs(t.R, values)
	if maxL > maxR {
		return maxL
	}
	return maxR
}

func main() {}
