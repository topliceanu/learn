package main

import (
	"testing"
)

func TestFind(t *testing.T) {
	for _, tc := range []struct{
		input []int
		expected int
	}{
		{[]int{6,7,8,9,1,2,3,4}, 5},
		{[]int{-1, -3, 1}, 0},
	}{
		actual := Find(tc.input)
		if actual != tc.expected {
			t.Errorf("expected %d, got %d", tc.expected, actual)
		}
	}
}

