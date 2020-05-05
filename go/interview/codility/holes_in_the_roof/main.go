package main

# For the better version check out the ocaml recursive version.

func boards(A []int, k int) int {
	n := len(A)
	beg := 1
	end := n
	result := -1
	for beg <= end {
		mid = (beg + end) / 2
		if check(A, mid) <= k {
			end = mid - 1
			result = mid
		} else {
			beg = mid + 1
		}
	}
	return result
}

func check(A []int, k int) int {
	n := len(A)
	boards := 0
	last := -1
	for i := 0; i < n; i ++ {
		if A[i] == 1 && last < i {
			boards += 1
			last = i + k - 1
		}
	}
	return boards
}
