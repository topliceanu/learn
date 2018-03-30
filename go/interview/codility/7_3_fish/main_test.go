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
		A, B []int
		expected int
	}{
		// their example
		{[]int{4, 3, 2, 1, 5}, []int{0, 1, 0, 0, 0}, 2},
		// edge case: every fish survives because they swim in the same direction
		{[]int{4, 3, 2}, []int{1, 1, 1}, 3},
		{[]int{4, 3, 2}, []int{0, 0, 0}, 3},
		// edge case: every fish has the same size, so they don't eat each other.
		{[]int{4, 4, 4, 4}, []int{1, 0, 1, 0}, 4},
		// tests
		{[]int{2, 1, 3, 2}, []int{1, 0, 1, 0}, 2},
		{[]int{3, 2, 1, 4}, []int{1, 1, 1, 0}, 1},
	}{
		actual := Solution(tc.A, tc.B)
		if actual != tc.expected {
			t.Errorf("case %d: (%v, %v) expected %d, got %d", i, tc.A, tc.B, tc.expected, actual)
		}
	}
}
