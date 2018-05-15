package main

import "testing"

func TestSolution(t *testing.T) {
	for i, tc := range []struct{
		A [][]int
		P float64
		expected float64
	}{
		// their cases
		{
			[][]int{
				[]int{1, 1},
			},
			7,
		},
		{
			[][]int{
				[]int{50, 120},
				[]int{50, 120},
			},
			920,
		},
		{
			[][]int{
				[]int{7, 4},
			},
			32,
		},
		{
			[][]int{
				[]int{10, 20},
				[]int{20, 30},
				[]int{30, 10},
			},
			240,
		},
	}{
		actual := Solution(tc.A, tc.R, tc.C, tc.H, tc.V)
		if actual != tc.expected {
			t.Errorf("case %d \n%d, %d, %d, %d\n%+v\nexpected %t, got %t", i, tc.R, tc.C, tc.H, tc.V, tc.A, tc.expected, actual)
		}
	}
}


