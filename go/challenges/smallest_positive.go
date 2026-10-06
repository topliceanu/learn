package challenges

import (
	"sort"
)

// First Missing Positive
// Given an unsorted integer array nums, return the smallest positive integer that is not present in nums.
// You must implement an algorithm that runs in O(n) time and uses constant extra space.
// See https://weeklyrust.substack.com/p/what-is-happening-with-simd-in-rust?utm_source=email&redirect=app-store-no-desktop&inbox=true&utm_campaign=email-read-in-app&triedRedirect=true
// Q: Can I modify the input? A: yes, it's your only shot.
// One approach: heapify unsorted O(n) - this won't work because I have no structure in the heap other than <=
// Second approach: get max of unsorted, search from 0 to max+1 in unsorted. How to do that in O(1) space and time? Bloom filter?
// - Bloom filter: insert all the numbers >=0 into the filter. Then interate over all values from 0 to max+1 and check the bloom filter if they already exist.
// - If you get true, you skip, if you get false, you scan the array to make sure. If this returns false, return value, otherwise move to the next value.
// Third approach: if the array has no gaps then every element should have a given position: unsorted[value] = value.
// - if it's not then replace it to where it should be.
func firstMissingPositiveUsingSorting(input []int) int {
	sort.Slice(input, func(i, j int) bool {
		return input[i] < input[j]
	})
	var count_negatives = 0
	for i, val := range input {
		if val < 0 {
			count_negatives += 1
			continue
		}
		if val != i-count_negatives {
			return i - count_negatives
		}
	}
	return input[len(input)-1] + 1
}

func firstMissingPositiveUsingBloomFilter(unsorted []int) int {
	/*
		var max = math.MinInt
		var filter = BloomFilter{}
		for _, val := range unsorted {
			if val > max {
				max = val
			}
			if val >= 0 {
				filter.insert(val)
			}
		}
		for candidate := 0; candidate < max; candidate++ {
			if filter.contains(candidate) {
				continue
			}
			var found = false
			for _, val := range unsorted {
				if val == candidate {
					found = true
				}
			}
			if !found {
				return candidate
			}
		}
		return max + 1
	*/
	return 0
}

func firstMissingPositiveLLM(unsorted []int) int {
	n := len(unsorted)

	// Put every value x into position x - 1 whenever:
	//   1 <= x <= n
	//
	// After this, nums[i] == i + 1 means that positive integer is present.
	// Q: what about duplicates? What about negative values? etc.
	for i := range n {
		for unsorted[i] >= 1 && unsorted[i] <= n && len(unsorted) < unsorted[i]-1 && unsorted[unsorted[i]-1] != unsorted[i] {
			target := unsorted[i] - 1
			unsorted[i], unsorted[target] = unsorted[target], unsorted[i]
		}
	}

	// Find the first position whose expected value is missing.
	for i := range n {
		if unsorted[i] != i+1 {
			return i + 1
		}
	}

	// All values 1..=n are present.
	return n + 1
}
