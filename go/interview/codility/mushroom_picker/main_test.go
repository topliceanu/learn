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
		A []int
		k int
		m int
		expected int
	}{
		{[]int{2, 3, 7, 5, 1, 3, 9}, 4, 6, 25},
	}{
		actual := Solution(tc.A, tc.k, tc.m)
		if actual != tc.expected {
			t.Errorf("case %d: (%v, %d, %d) expected %v, got %v", i, tc.A, tc.k, tc.m, tc.expected, actual)
		}
	}
}

