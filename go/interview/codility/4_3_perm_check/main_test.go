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
		// test example
		{[]int{4, 1, 3}, 0},
		{[]int{4, 1, 3, 2}, 1},
		// duplicates
		{[]int{1, 1, 1}, 0},
		// single value array is a permutation
		{[]int{1}, 1},
		// doesn't start from 1
		{[]int{5, 4, 6}, 0},
		// empty
		{[]int{}, 1},
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}
