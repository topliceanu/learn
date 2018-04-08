package main

import "testing"

func TestSave(t *testing.T) {
	for i, tc := range []struct{
		D int
		P string
		expected int
	}{
		// their cases
		{1, "CS", 1},
		{2, "CS", 0},
		{1, "SS", -1},
		{6, "SCCSSC", 2},
		{2, "CC", 0},
		{3, "CSCSS", 5},
	}{
		actual := Save(tc.D, tc.P)
		if actual != tc.expected {
			t.Errorf("case %d (%d, %s): expected %d, got %d", i, tc.D, tc.P, tc.expected, actual)
		}
	}
}
