package main

import "testing"

func TestSolution(t *testing.T) {
	for i, tc := range []struct{
		A []string
		expected string
	}{
		// their examples:
		{[]string{"CAKE", "TORN", "SHOW"}, "CORN"},
		{[]string{"AA", "AB", "BA", "BB"}, "-"},
		{[]string{"A", "B", "C", "D"}, "-"},
		{[]string{"WW", "AA", "SS", "DD"}, "WA"},
		{[]string{"HELPIAM", "TRAPPED", "INSIDEA", "CODEJAM", "FACTORY"}, "HOLIDAY"},
		// my examples
		{[]string{"AA", "AB", "BA", "BB", "BC"}, "AC"},
		{[]string{"ABA", "ACB", "ACA"}, "ABB"},
	}{
		actual := Solution(tc.A)
		if tc.expected == "-" && actual != "-" {
			t.Errorf("case %d: %+v expected -, but got %s", i, tc.A, actual)
		}
		if tc.expected != "-" && actual == "-" {
			t.Errorf("case %d: %+v expected not to get -, but got %s", i, tc.A, actual)
		}
	}
}
