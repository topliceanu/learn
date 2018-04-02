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
		{[]int{4, 3, 4, 4, 4, 2}, 2},
		// edge case: no leader
		{[]int{1, 3}, 0},
		{[]int{1, 1, 1, 2, 2, 2}, 0},
		// edge case: every index is an equileader.
		{[]int{1, 1, 1, 1}, 3},
		// edge case: have a leader but no equileader
		{[]int{1, 1, 1, 2, 2}, 0},
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}
