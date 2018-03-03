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
		{[]int{9}, 9},
		{[]int{9, 3, 9, 3, 9, 7, 9}, 7},
		{[]int{9, 9, 9, 9, 9}, 9},
		{[]int{1, 2, 3, 4, 2, 3, 4}, 1},
		{[]int{1, 2, 3, 3, 2, 1, 4}, 4},
	}{
		actual := Solution(tc.input)
		if actual != tc.expected {
			t.Errorf("case %d: %v, expected %v, got %v", i, tc.input, tc.expected, actual)
		}
	}
}
