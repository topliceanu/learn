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
		H []int
		expected int
	}{
		// their example
		{[]int{8, 8, 5, 7, 9, 8, 7, 4, 8}, 7},
		// simple example
		{[]int{4, 4, 4, 4, 4, 4, 4, 4}, 1},
		// increasing heights
		{[]int{1, 2, 3, 4, 5, 6}, 6},
		// alternating heights
		{[]int{1, 2, 1, 2, 1, 2, 1}, 4},
		// edge cases
		{[]int{}, 0},
		{[]int{7}, 1},
	}{
		actual := Solution(tc.H)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.H, tc.expected, actual)
		}
	}
}
