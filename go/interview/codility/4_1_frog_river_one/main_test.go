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
		x int
		A []int
		expected int
	}{
		{5, []int{1, 3, 1, 4, 2, 3, 5, 4}, 6},
		{5, []int{1, 3, 1, 4, 2, 3, 2, 4}, -1},
	}{
		actual := Solution(tc.x, tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%d, %v) expected %v, got %v", i, tc.x, tc.A, tc.expected, actual)
		}
	}
}


