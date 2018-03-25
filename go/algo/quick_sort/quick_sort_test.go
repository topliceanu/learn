package main

import (
	"testing"
	"reflect"
)

func TestQuickSort(t *testing.T) {
	for i, tc := range []struct{
		A []int
		expected []int
	}{
		{[]int{4,3,2,1}, []int{1,2,3,4}},
		{[]int{1,2,3,4}, []int{1,2,3,4}},
		{[]int{4,2,3,1}, []int{1,2,3,4}},
		{[]int{1}, []int{1}},
		{[]int{1,1,1,1,1}, []int{1,1,1,1,1}},
		{[]int{1,2,3,4,-1,-2,-3,-4}, []int{-4,-3,-2,-1,1,2,3,4}},
		{[]int{3, -2, 1, 4, -5, 6}, []int{-5, -2, 1, 3, 4, 6}},
	}{
		QuickSort(tc.A)
		if !reflect.DeepEqual(tc.A, tc.expected) {
			t.Errorf("case %d: expected %v, got %v", i, tc.expected, tc.A)
		}
	}
}
