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
	for _, tc := range []struct{
		input []int
		expected int
	}{
		{
			[]int{},
			5,
		},
		{
			[]int{},
			0,
		},
	}{
		actual := 1
		if actual != tc.expected {
			t.Errorf("expected %v, got %v", tc.expected, actual)
		}
	}
}
