package main

func Solution(A []int, k int, m int) int {
	prefixes := make([]int, len(A))
	for i, a := range A {
		prefixes[i] = a
		if i > 0 {
			prefixes[i] += prefixes[i-1]
		}
	}
	max := 0
	for l := 1; l <= m; l ++ {
		r := k - l*2
		ls := leftSum(prefixes, k, l)
		rs := rightSum(prefixes, k, r)
		cs :=	ls + rs + A[k]
		if max < cs {
			max = cs
		}
	}
	return max
}

func leftSum(prefixes []int, k, l int) int {
	if k < 1 {
		return 0
	}
	if k - l < 1 {
		return 0
	}
	return prefixes[k-1] - prefixes[k-l]
}

func rightSum(prefixes []int, k, r int) int {
	n := len(prefixes)
	return prefixes[max(k+r, n-1)] - prefixes[max(k+1, n-1)]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
}
