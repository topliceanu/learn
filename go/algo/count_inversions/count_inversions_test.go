package main

import (
	"testing"
)

func TestCountInversions(t *testing.T) {
	for i, tc := range []struct{
		A []int
		expected int
	}{
		// inverted array
		{[]int{2, 1}, 1},
		{[]int{4,3,2,1}, 6},
		// array with a single element.
		{[]int{1}, 0},
		// array of identical elements.
		{[]int{1,1,1,1,1}, 0},
		// already sorted array
		{[]int{1,2,3,4,5,6}, 0},
		// random cases
		{[]int{1, 3, 5, 2, 4, 6}, 3},
		{[]int{3, 2, 1, 6, 5, 4}, 6},
	}{
		actual := CountInversions(tc.A)
		if actual != tc.expected {
			t.Errorf("case %d: expected %d, got %d", i, tc.expected, actual)
		}
	}
}

