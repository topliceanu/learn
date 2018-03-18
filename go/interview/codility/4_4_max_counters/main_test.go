package main

import (
	"reflect"
	"testing"
)

/*
1. imagine the usual scenario
2. identify general edge cases
3. identify edge cases specific on the implementation
*/

func TestSolution(t *testing.T) {
	for i, tc := range []struct{
		N int
		A []int
		expected []int
	}{
		// one max
		{5, []int{3, 4, 4, 6, 1, 4, 4}, []int{3, 2, 2, 4, 2}},
		// no max
		{5, []int{3, 4, 4, 3, 1, 4, 4}, []int{1, 0, 2, 4, 0}},
		// multiple maxes
		{5, []int{3, 4, 4, 6, 1, 6, 4}, []int{3, 3, 3, 4, 3}},
		// only maxes
		{5, []int{6, 6,	6, 6}, []int{0, 0, 0, 0, 0}},
		// increments to inexistent indexes or wrong maxes don't do anything.
		{5, []int{-1, -2,	7, 10}, []int{0, 0, 0, 0, 0}},
	}{
		actual := Solution(tc.N, tc.A)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("case %d: (%d, %v) expected %v, got %v", i, tc.N, tc.A, tc.expected, actual)
		}
	}
}

/*
(0, 0, 1, 0, 0) 1
(0, 0, 1, 1, 0) 1
(0, 0, 1, 2, 0) 2
(2, 2, 2, 2, 2) 2
(3, 2, 2, 2, 2) 3
(4, 3, 2, 2, 2) 4
(4, 4, 4, 4, 4) 4
(4, 4, 4, 5, 4) 5
*/
