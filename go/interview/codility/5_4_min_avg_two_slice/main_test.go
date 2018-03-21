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
		{[]int{10, 10, -1, 2, 4, -1, 2, -1}, 5},
		/*
		// example
		{[]int{4, 2, 2, 5, 1, 5, 8}, 1},
		// edge cases
		{[]int{1, 2}, 0},
		{[]int{1, 1, 1, 1, 1}, 0},
		{[]int{9, 9, 9, 1, 1}, 3},
		{[]int{9, 1, 1, 9, 9, 1, 1, 1}, 1},
		{[]int{1, 1, 2, 1}, 0},
		// their extra tests
		{[]int{10, 10, -1, 2, 4, -1, 2, -1}, 2},
		*/
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}
