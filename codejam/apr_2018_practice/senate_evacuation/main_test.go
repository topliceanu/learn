package main

import (
	"testing"
	"reflect"
)

func TestSenateEvacuation(t *testing.T) {
	for i, tc := range []struct{
		A []int
		expected []string
	}{
		// their cases
		{[]int{2, 2}, []string{"AB", "BA"}},
		//{[]int{3, 2, 2}, []string{"AA", "BC", "C", "BA"}},
		//{[]int{1, 1, 2}, []string{"C", "C", "AB"}},
		//{[]int{2, 3, 1}, []string{"BA", "BB", "CA"}},
	}{
		actual := SenateEvacuation(tc.A)
		if !reflect.DeepEqual(actual, tc.expected) {
			t.Errorf("case %d (%+v): expected %+v, got %+v", i, tc.A, tc.expected, actual)
		}
	}
}
