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
		A, B, K int
		expected int
	}{
		// example test case
		{6, 11, 2, 3},
		// edge cases
		{0, 0, 11, 1},
		{1, 1, 11, 0},
		{10, 10, 5, 1},
		{10, 10, 20, 0},
		{11, 345, 17, 20},
	}{
		actual := Solution(tc.A, tc.B, tc.K)
		if actual != tc.expected {
			t.Errorf("case %d: (%d, %d, %d) expected %d, got %d", i, tc.A, tc.B, tc.K, tc.expected, actual)
		}
	}
}
