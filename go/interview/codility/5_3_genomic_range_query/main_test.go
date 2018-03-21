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
		S string
		P []int
		Q []int
		expected []int
	}{
		// test case
		{"CAGCCTA", []int{2, 5, 0}, []int{4, 5, 6}, []int{2, 4, 1}},
		// all same letter
		{"AAAAAAA", []int{2, 5, 0}, []int{4, 5, 6}, []int{1, 1, 1}},
		{"TTTTTTT", []int{2, 5, 0}, []int{4, 5, 6}, []int{4, 4, 4}},
		// only one measurement
		{"CAGCCTA", []int{5}, []int{5}, []int{4}},
		// end of the sequence
		{"CAGCCTA", []int{5}, []int{6}, []int{1}},
		// begining of the sequence
		{"CAGCCTA", []int{0}, []int{1}, []int{1}},
		// all measurements
		{"CAT", []int{0, 0, 0, 1, 1, 2}, []int{0, 1, 2, 1, 2, 2}, []int{2, 1, 1, 1, 1, 4}},
		{"ACGA", []int{1, 0}, []int{2, 2}, []int{2, 1}},
	}{
		actual := Solution(tc.S, tc.P, tc.Q)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("case %d: (%s, %v, %v) expected %v, got %v", i, tc.S, tc.P, tc.Q, tc.expected, actual)
		}
	}
}
