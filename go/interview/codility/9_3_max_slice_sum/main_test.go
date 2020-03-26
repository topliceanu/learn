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
		{[]int{3, 2, -6, 4, 0}, 5},
		// edge case: one element
		{[]int{3}, 3},
		// edge case: all negative
		{[]int{-1, -2, -3, -4}, -1},
		// edge case: all increasing
		{[]int{1, 2, 3, 4}, 10},
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}
