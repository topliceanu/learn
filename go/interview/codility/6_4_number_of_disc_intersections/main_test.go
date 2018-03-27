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
		{[]int{1, 5, 2, 1, 4, 0}, 11},
		// one circle covering all of them
		{[]int{0, 0, 3, 0, 0}, 4},
		// two large circles
		{[]int{2, 0, 0, 0, 2}, 5},
		// everyone with everyone else
		{[]int{3, 2, 2, 3}, 6},
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}
