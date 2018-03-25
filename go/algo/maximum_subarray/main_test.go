package main

import (
	"testing"
	"reflect"
)

func TestMaxSubarray(t *testing.T) {
	for _, tc := range []struct{
		input []int
		expected []int
	} {
		{[]int{10, 11, 7, 10, 6}, []int{7, 10}},
		{[]int{100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97}, []int{86, 81, 101}},
	} {
		actual := MaxSubArray(tc.input)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("expected %v but got %v", tc.expected, actual)
		}
	}
}
