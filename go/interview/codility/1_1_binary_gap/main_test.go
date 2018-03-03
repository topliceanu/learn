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
		input int
		expected int
	}{
		{9, 2}, // 1001
		{529, 4}, // 1000010001
		{20, 1}, // 10100
		{15, 0}, // 1111
		{1041, 5}, // 100000100001
	}{
		actual := Solution(tc.input)
		if actual != tc.expected {
			t.Errorf("case %d: %v(%b), expected %v, got %v", i, tc.input, tc.input, tc.expected, actual)
		}
	}
}
