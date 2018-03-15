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
		input []int
		expected int
	}{
		{[]int{3, 1, 2, 4, 3}, 1},
		{[]int{2, 1, 1, 2}, 0},
		{[]int{1, 2, 3, 4, 5, 6}, 1},
	}{
		actual := Solution(tc.input)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %v, got %v", i, tc.input, tc.expected, actual)
		}
	}
}


