package main

import (
	"testing"
)

func TestMinMaxDivision(t *testing.T) {
	tests := []struct{
		data []int
		minMax int
		start int
		stop int
	}{
		// Problem test case
		{
			data: []int{2, 1, 5, 1, 2, 2, 2},
			minMax: 6,
			start: 2,
			stop: 4,
		},
		// Edge test cases
		{
			data: []int{},
			minMax: 0,
			start: 0,
			stop: 0,
		},
		{
			data: []int{1},
			minMax: 1,
			start: 0,
			stop: 0,
		},
		{
			data: []int{1, 2},
			minMax: 2,
			start: 0,
			stop: 1,
		},
		// Test cases with negative values
		{
			data: []int{1, 2, -1},
			minMax: 1,
			start: 0,
			stop: 1,
		},
		{
			data: []int{1, 2, -3, 5},
			minMax: 2,
			start: 1,
			stop: 2,
		},
	}
	for _, test := range tests {
		sum, start, stop := MinMaxDivision(test.data)
		expected := test.minMax
		if sum != expected || start != test.start || stop != test.stop {
			t.Fatalf("for data=%v, expected sum %d, got %d; expected start=%d, got %d, expectd stop=%d, got %d",
			test.data, test.minMax, sum, test.start, start, test.stop, stop)
		}
	}
}
