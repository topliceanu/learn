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
		{[]int{23171, 21011, 21123, 21366, 21013, 21367}, 356},
		// my example
		{[]int{2, 3, 10, 1, 2}, 8},
		// edge case: empty input
		{[]int{}, 0},
		// edge case: one element
		{[]int{1}, 0},
		// edge case: only increasing
		{[]int{1, 2, 3, 4, 5}, 4},
		// edge case: only decreasing
		{[]int{4, 3, 2, 1, 0}, 0},
		// decrease and then increase.
		{[]int{4, 3, 2, 1, 0, 1, 2, 3, 4}, 4},
		// increase then decrease.
		{[]int{0, 1, 2, 3, 4, 3, 2, 1, 0}, 4},
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
