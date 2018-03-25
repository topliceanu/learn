package main

// CountInversions piggybacks on mergeSort
func CountInversions(A []int) int {
	_, count := countInversions(A)
	return count
}

func countInversions(A []int) (sorted []int, count int) {
	if len(A) <= 1 {
		return A, 0
	}
	m := int(len(A)/2)
	left, lCount := countInversions(A[:m])
	right, rCount := countInversions(A[m:])
	all, xCount := mergeAndCount(left, right)
	return all, lCount + rCount + xCount
}

func mergeAndCount(left, right []int) (sorted []int, count int) {
	sorted = make([]int, len(left) + len(right))
	i, j, k := 0, 0, 0
	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			sorted[k] = left[i]
			i += 1
		} else {
			sorted[k] = right[j]
			j += 1
			// When you find an element in right which is smaller than the i'th element in left,
			// it means you will have len(left) - i inversions formed with the curent element in right.
			count += len(left) - i
		}
		k += 1
	}
	for ; i < len(left); i ++ {
		sorted[k] = left[i]
		k += 1
	}
	for ; j < len(right); j ++ {
		sorted[k] = right[j]
		k += 1
	}
	return sorted, count
}
