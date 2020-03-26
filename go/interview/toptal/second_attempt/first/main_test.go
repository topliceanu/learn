package main

/*
1. imagine the usual scenario
2. identify general edge cases
3. identify edge cases specific on the implementation
*/

import (
	"testing"
)

func TestSolution(t *testing.T) {
	for i, tc := range []struct{
		t *Tree
		expected int
	}{
		// their examples.
		{
			t: &Tree{
				X: 4,
				L: &Tree{
					X: 5,
					L: &Tree{
						X: 4,
						L: &Tree{X: 5},
					},
				},
				R: &Tree{
					X: 6,
					L: &Tree{X: 1},
					R: &Tree{X: 6},
				},
			},
			expected: 3,
		},
		// edge case: one node tree
		{
			t: &Tree{
				X: 3,
			},
			expected: 1,
		},
		// edge case: all values are the same
		{
			t: &Tree{
				X: 4,
				L: &Tree{
					X: 4,
					L: &Tree{
						X: 4,
						L: &Tree{X: 4},
					},
				},
				R: &Tree{
					X: 4,
					L: &Tree{X: 4},
					R: &Tree{X: 4},
				},
			},
			expected: 1,
		},
		// edge case: all values are distinct
		{
			t: &Tree{
				X: 1,
				L: &Tree{
					X: 2,
					L: &Tree{
						X: 4,
					},
					R: &Tree{
						X: 5,
					},
				},
				R: &Tree{
					X: 3,
					L: &Tree{
						X: 6,
					},
					R: &Tree{
						X: 7,
						R: &Tree{
							X: 8,
						},
					},
				},
			},
			expected: 4,
		},
	}{
		actual := Solution(tc.t)
		if actual != tc.expected {
			t.Errorf("case %d: expected %d, got %d", i, tc.expected, actual)
		}
	}
}
