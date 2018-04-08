package main

import "testing"

/*
1. imagine the usual scenario
2. identify general edge cases
3. identify edge cases specific on the implementation
*/

func TestCheckTroubleSort(t *testing.T) {
	for i, tc := range []struct{
		V []int
		expectedSorted bool
		expectedIndex int
	}{
		// their cases
		{[]int{5, 6, 8, 4, 3}, true, 0},
		{[]int{8, 9, 7}, false, 1},
		// edge cases: already sorted
		{[]int{1, 2, 3, 4, 5}, true, 0},
		// edge case: reverse sorted
		{[]int{5, 4, 3, 2, 1}, false, 0},
		// four elements
		{[]int{4, 3, 2, 1}, false, 0},
		{[]int{1, 2, 4, 3}, false, 2},
	}{
		actualSorted, actualIndex := CheckTroubleSort(tc.V)
		if actualSorted != tc.expectedSorted && actualIndex != tc.expectedIndex {
			t.Errorf("case %d (%+v): expected sorted %t and index %d, got sorted %t and index %d", i, tc.V, tc.expectedSorted, tc.expectedIndex, actualSorted, actualIndex)
		}
	}
}

