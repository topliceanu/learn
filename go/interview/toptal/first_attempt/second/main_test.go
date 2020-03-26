package main

import (
	"testing"
)

/*
1. imagine the usual scenario
2. identify general edge cases
3. identify edge cases specific on the implementation
*/

func TestFunction(t *testing.T) {
	for i, tc := range []struct{
		input []int
		expected int
	}{
		{
			[]int{6, 10, 6, 9, 7, 8},
			3,
		},
		// empty
		{
			[]int{},
			0,
		},
		// no progression
		{
			[]int{1,2,3,4,5,6,7,8,9,10},
			1,
		},
		// steps of 2
		{
			[]int{2,4,6,8,10},
			1,
		},
	}{
		actual := Solution(tc.input)
		if actual != tc.expected {
			t.Errorf("case %d, expected %v, got %v", i, tc.expected, actual)
		}
	}
}
