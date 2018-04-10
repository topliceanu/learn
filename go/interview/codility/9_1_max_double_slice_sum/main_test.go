package main

import (
	"testing"
)

/*
1. imagine the usual scenario
2. identify general edge cases
3. identify edge cases specific on the implementation
*/

func TestSolution(t *testing.T) {
	for i, tc := range []struct{
		A []int
		expected int
	}{
		// their examples.
		{[]int{3, 2, 6, -1, 4, 5, -1, 2}, 17},
		// edge case: array with three elements.
		{[]int{1, 2, 3}, 0},
		// edge case: array with four elements.
		{[]int{1, 2, 3, 4}, 3},
		// use negative elements
		{[]int{-1, -2, -3, -4, -5}, -3},
		{generateRange(-3, 3), 2},
		{generateRange(-4, 4), 5},
		{generateRange(-1000, 1000), 499499},
		{generateRange(-10, 10), 44},
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}

func generateRange(l, r int) []int {
	n := r - l + 1
	out := make([]int, n)
	for i := 0; i < n; i ++ {
		out[i] = l + i
	}
	return out
}
