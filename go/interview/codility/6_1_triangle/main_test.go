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
		/*
		// their examples.
		{[]int{10, 2, 5, 1, 8, 20}, 1},
		{[]int{10, 50, 5, 1}, 0},
		// edge cases.
		{[]int{2, 3}, 0},
		*/
		{[]int{10, 50, 5, 1}, 0},
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}
