package main

/*
1. imagine the usual scenario
2. identify general edge cases
3. identify edge cases specific on the implementation
*/

import (
	"testing"
)

func TestSolution(t *testing.T) {
	for i, tc := range []struct{
		N int
		expected int
	}{
		// their examples.
		{1213, 12},
		{123, 6},
		/*
		{100, 1},
		{0, 1},
		// edge case: one zero
		{1230, 18},
		{1200, },
		*/
	}{
		actual := Solution(tc.N)
		if actual != tc.expected {
			t.Errorf("case %d (%d): expected %d, got %d", i, tc.N, tc.expected, actual)
		}
	}
}

