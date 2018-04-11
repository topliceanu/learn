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
		// example test case
		{[]int{0, 1, 0, 1, 1}, 5},
		// all crossing each other
		{[]int{0, 0, 0, 1, 1, 1}, 9},
		// no intersection
		{[]int{1, 1, 1, 0, 0, 0}, 0},
		// same direction
		{[]int{1, 1, 1}, 0},
		{[]int{0, 0, 0}, 0},
		// one pair crossing
		{[]int{1, 1, 0, 1, 0, 0}, 1},
		// one element
		{[]int{1}, 0},
		// large tests
		{makeLargeTest(2000), 1000000},
		{makeLargeTest(200000), -1},
	}{
		actual := Solution(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: (%v) expected %d, got %d", i, tc.A, tc.expected, actual)
		}
	}
}

func makeLargeTest(size int) []int {
	out := make([]int, size)
	for i := 1; i <= size/2; i++ {
		out[i-1] = 0
		out[size-i] = 1
	}
	return out
}
