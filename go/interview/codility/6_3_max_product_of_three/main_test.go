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
		// their example
		{[]int{-3, 1, 2, -2, 5, 6}, 60},
		// negative numbers
		{[]int{-3, -2, -1, 0}, 0},
		{[]int{-3, -2, -1, 0, 1}, 6},
		{[]int{-3, -2, 0, 1, 2}, 12},
		{[]int{-3, -2, 0, 1, 2, 3}, 18},
		{[]int{-3, -2, 0, 1, 2, 3, 4}, 24},
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}
