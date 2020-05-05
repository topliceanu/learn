package main

/* MinMaxDivision computes the division in three of data that yields the
 * smallest max sum of the three subarrays.
 *
 * Solution: build aux arrays with sums from left to right and right to left from the data.
 * Complexity: O(n^2) in time and O(n) in space
 *
 * Convention for encoding the solution when subarrays are empty and at the edge.
 * [][][...] -> [[0,0), [0,0), [0,n)]
 * [][...][] -> [[0,0), [0,n), [n,n)]
 * [...][][] -> [[0,n), [n,n), [n,n)]
 * Where n is the size of the input data array
 * And [x,y) is a subarray that start from index x and ends at index y-1, inclusive.
 * It does not contain y!
 *
 * data   |  2  1  5  1  2  2  2  _
 * index  |  0  1  2  3  4  5  6  7
 * sumL2R |  0  2  3  8  9 11 13 15
 * sumR2L | 15 13 12  7  6  4  2  0
 * min sum is 6, with indices [2, 4)
 **/
func MinMaxDivision(data []int) (minMaxSum, minMaxStart, minMaxStop int) {
	n := len(data)
	if n == 0 {
		return 0, 0, 0
	}
	sumL2R := make([]int, n+1)
	sumR2L := make([]int, n+1)

	sumL2R[0] = 0
	sumL2R[n] = 0
	total := 0
	for i := 1; i <= n; i ++ {
		sumL2R[i] = sumL2R[i-1] + data[i-1]
		sumR2L[n-i] = sumR2L[n-i+1] + data[n-i]
		total += data[i-1]
	}

	minMaxSum = 100000000
	minMaxStart = 0
	minMaxStop = 0
	for i := 0; i <= n; i ++ {
		for j := i; j <= n; j ++ {
			left := sumL2R[i]
			right := sumR2L[j]
			center := total - left - right
			localMax := max(max(left, right), center)
			if localMax < minMaxSum {
				minMaxSum = localMax
				minMaxStart = i
				minMaxStop = j
			}
		}
	}
	return minMaxSum, minMaxStart, minMaxStop
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
