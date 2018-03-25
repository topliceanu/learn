package main


/*
Given a set of integers, not sorted, find the smallest positive integer that's missing in the sorted version.
Time complexity must be O(n) and space complexity must be O(n).
*/

type set map[int]struct{}

func Find(a []int) int {
	// 1. index all the values
	s := make(set)
	min := 0
	for _, i := range a {
		s[i] = struct{}{}
		if i > min {
			min = i
		}
	}
	// 2. find minimum.
	for i := 1; i < len(a); i ++ {
		if a[i] < -1 {
			continue
		}
		if _, found := s[a[i]+1]; !found && min > a[i]+1 {
			min = a[i]+1
		}
	}
	return min
}
