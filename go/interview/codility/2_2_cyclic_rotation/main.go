package main

import (
)

func Solution(xs []int, k int) []int {
	n := len(xs)
	out := make([]int, n)
	for i := 0; i < n; i ++ {
		j := (i + k) % n
		out[j] = xs[i]
	}
	return out
}

func main() {}
