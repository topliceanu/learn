package main

import "testing"

func TestSolution(t *testing.T) {
	for i, tc := range []struct{
		R, C, H, V int
		A [][]int
		expected bool
	}{
		// their cases
		{
			3, 6, 1, 1,
			[][]int{
				[]int{0, 1, 1, 0, 0, 1},
				[]int{0, 0, 0, 0, 0, 1},
				[]int{1, 0, 1, 0, 1, 1},
			},
			true,
		},
		{
			4, 3, 1, 1,
			[][]int{
				[]int{1, 1, 1},
				[]int{1, 0, 1},
				[]int{1, 0, 1},
				[]int{1, 1, 1},
			},
			false,
		},
		{
			4, 5, 1, 1,
			[][]int{
				[]int{0, 0, 0, 0, 0},
				[]int{0, 0, 0, 0, 0},
				[]int{0, 0, 0, 0, 0},
				[]int{0, 0, 0, 0, 0},
			},
			true,
		},
		{
			4, 4, 1, 1,
			[][]int{
				[]int{0, 0, 1, 1},
				[]int{0, 0, 1, 1},
				[]int{1, 1, 0, 0},
				[]int{1, 1, 0, 0},
			},
			false,
		},
		{
			3, 4, 2, 2,
			[][]int{
				[]int{1, 0, 1, 1},
				[]int{1, 1, 0, 1},
				[]int{1, 0, 1, 1},
			},
			true,
		},
		{
			3, 4, 1, 2,
			[][]int{
				[]int{0, 1, 0, 1},
				[]int{1, 0, 1, 0},
				[]int{0, 1, 0, 1},
			},
			false,
		},
	}{
		actual := Solution(tc.A, tc.R, tc.C, tc.H, tc.V)
		if actual != tc.expected {
			t.Errorf("case %d \n%d, %d, %d, %d\n%+v\nexpected %t, got %t", i, tc.R, tc.C, tc.H, tc.V, tc.A, tc.expected, actual)
		}
	}
}

