package main

import (
	"math/rand"
)

func QuickSort(A []int) {
	quicksort(A, 0, len(A) - 1)
}

// quicksort sorts the input A array in place.
func quicksort(A []int, l, r int) {
	if l >= r {
		return
	}
	if l + 1 == r {
		if A[l] > A[r] {
			A[l], A[r] = A[r], A[l]
		}
		return
	}
	p := pickPivot(l, r)
	newP := partition(A, l, r, p)
	quicksort(A, l, newP-1)
	quicksort(A, newP+1, r)
}

func pickPivot(l, r int) int {
	return l + rand.Intn(r - l + 1)
}

func partition(A []int, l, r, p int) int {
	A[p], A[l] = A[l], A[p]
	p = l+1
	for i := l+1; i <= r; i ++ {
		if A[i] <= A[l] {
			A[p], A[i] = A[i], A[p]
			p++
		}
	}
	A[l], A[p-1] = A[p-1], A[l]
	return p-1
}
