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
		{[]int{6, 8, 4, 6, 8, 6, 6}, 6},
		{[]int{3, 4, 3, 2, 3, -1, 3, 3}, 7},
		{[]int{1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2}, -1},
		// for even length arrays.
		{[]int{1, 1, 1, 2, 3, 3}, -1},
		{[]int{1, 1, 1, 1, 3, 3}, 3},
		// for odd length array.
		{[]int{1, 1, 3, 3}, -1},
		{[]int{1, 1, 1, 3}, 2},
		// no leader
		{[]int{1, 1, 2, 2, 3, 3}, -1},
		// negative numbers give out the same value as when no leader is found?!
		{[]int{-1, -1, -1, -2, -3}, 2},
		// edge cases
		{[]int{}, -1},
		{[]int{1}, 0},
		{[]int{1, 1, 1, 1, 1}, 4},
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}
