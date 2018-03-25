package main

// MergeSort returns a new array with the elements from A but sorted.
func MergeSort(A []int) []int {
	return mergeSort(A)
}

func mergeSort(A []int) []int {
	if len(A) <= 1 {
		return A
	}
	m := int(len(A) / 2)
	left := mergeSort(A[:m])
	right := mergeSort(A[m:])
	return merge(left, right)
}

func merge(left, right []int) []int {
	out := make([]int, len(left) + len(right))
	i, j, k := 0, 0, 0
	for i < len(left) && j < len(right) {
		if left[i] < right[j] {
			out[k] = left[i]
			i += 1
		} else {
			out[k] = right[j]
			j +=1
		}
		k += 1
	}
	for ; i < len(left); i++ {
		out[k] = left[i]
		k += 1
	}
	for ; j < len(right); j++ {
		out[k] = right[j]
		k += 1
	}
	return out
}
