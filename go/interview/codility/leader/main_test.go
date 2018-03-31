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
		found bool
		expected int
	}{
		// their example.
		{[]int{6, 8, 4, 6, 8, 6, 6}, true, 6},
		// for even length arrays.
		{[]int{1, 1, 1, 2, 3, 3}, false, 0},
		// no leader
		{[]int{1, 1, 2, 2, 3, 3}, false, 0},
		// negative numbers
		{[]int{-1, -1, -1, -2, -3}, true, -1},
	}{
		found, actual := Leader(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %t(%d), got %t(%d)", i, tc.A, tc.found, tc.expected, found, actual)
		}
	}
}
