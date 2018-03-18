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
		{[]int{1, 3, 6, 4, 1, 2}, 5},
		{[]int{1, 2, 3}, 4},
		{[]int{-1, -3}, 1},
		{[]int{4, 3, 2}, 1},
		{[]int{4, 3, 2}, 1},
		{[]int{1, 1, 1, 1}, 2},
		{[]int{1, -1, 0, 1, -2, 3}, 2},
		{[]int{3, 4, 5}, 1},
		{[]int{1}, 2},
		{[]int{2}, 1},
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}
