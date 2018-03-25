package main

import "testing"
import "reflect"

func TestHeapSort(t *testing.T) {
	for i, tc := range []struct{
		A []int
		expected []int
	}{
		{[]int{1,3,5,2,4,6}, []int{1,2,3,4,5,6}},
		{[]int{3,2,1,6,5,4}, []int{1,2,3,4,5,6}},
	}{
		actual := HeapSort(tc.A)
		if !reflect.DeepEqual(tc.expected, actual) {
			t.Errorf("case %d (%v): expected %v, got %v", i, tc.A, tc.expected, actual)
		}
	}
}

