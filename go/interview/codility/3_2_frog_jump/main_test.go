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
		x int
		y int
		d int
		expected int
	}{
		{x: 10, y: 85, d: 30, expected: 3},
		{x: 1, y: 100, d: 1, expected: 99},
		{x: 1, y: 1, d: 100, expected: 0},
	}{
		actual := Solution(tc.x, tc.y, tc.d)
		if actual != tc.expected {
			t.Errorf("case %d: (%d, %d, %d) expected %v, got %v", i, tc.x, tc.y, tc.d, tc.expected, actual)
		}
	}
}

