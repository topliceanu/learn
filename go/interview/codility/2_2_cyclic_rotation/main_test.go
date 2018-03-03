package main

import (
	"testing"
	"reflect"
)

/*
1. imagine the usual scenario
2. identify general edge cases
3. identify edge cases specific on the implementation
*/

func TestSolution(t *testing.T) {
	for i, tc := range []struct{
		input []int
		k int
		expected []int
	}{
		{[]int{3, 8, 9, 7, 6}, 3, []int{9, 7, 6, 3, 8}},
		{[]int{0, 0, 0}, 1, []int{0, 0, 0}},
		{[]int{1, 2, 3, 4}, 4, []int{1, 2, 3, 4}},
		{[]int{3, 4, 5}, 10, []int{5, 3, 4}},
		{[]int{1}, 10, []int{1}},
	}{
		actual := Solution(tc.input, tc.k)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("case %d: (%v,%d) expected %v, got %v", i, tc.input, tc.k, tc.expected, actual)
		}
	}
}

