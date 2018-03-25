package main

import (
	"fmt"
)

/*
# The Maximum Subarray Problem

Given an array of integers, find the subarray where the difference of the two
limits is maximum.
*/

func MaxSubArray(a []int) []int {
	// build a difference array.
	b := make([]int, len(a) - 1)
	for i := 0; i < len(a) - 1; i ++ {
		b[i] = a[i+1] - a[i]
	}
	fmt.Println(b)

	left, right = recMaxSubArray(a, 0, len(a) - 1)

	return a[left:right]
}

func recMaxSubArray(a, left, right) (int, int) {
	if left == right {
		return left, right
	}

}
