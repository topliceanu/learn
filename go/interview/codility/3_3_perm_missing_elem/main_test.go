package main

import (
	"testing"
)

/*
1. imagine the usual scenario
2. identify general edge cases
3. identify edge cases specific on the implementation
4. create large inputs
*/

func TestSolution(t *testing.T) {
	for i, tc := range []struct{
		input []int
		expected int
	}{
		{input: []int{2, 3, 1, 5}, expected: 4},
		{input: []int{1, 2, 3, 4, 5, 6, 8}, expected: 7},
		{input: []int{1, 2, 3, 4, 5, 6, 7}, expected: 8},
		{input: []int{2, 3, 4, 5, 6, 7, 8}, expected: 1},
	}{
		actual := Solution(tc.input)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %v, got %v", i, tc.input, tc.expected, actual)
		}
	}
}

