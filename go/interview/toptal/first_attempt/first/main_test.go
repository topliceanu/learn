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
		input []Point2D
		expected int
	}{
		{
			[]Point2D{{-1, -2}, {1, 2}, {2, 4}, {-3, 2}, {2, -2}},
			4,
		},
		// Edge case: all points are on the same line
		{
			[]Point2D{{1, 1}, {2, 2}, {3, 3}, {4, 4}},
			1,
		},
		// Edge case: there is only one point
		{
			[]Point2D{{1, 1}},
			1,
		},
		// Edge case: there are no statues
		{
			[]Point2D{},
			0,
		},
	}{
		actual := Solution(tc.input)
		if actual != tc.expected {
			t.Errorf("case %d, expected %v, got %v", i, tc.expected, actual)
		}
	}
}
