package main

func Solution(A []int) int {
	sum := 0
	nsum := len(A) + 1
	for i, a := range A {
		sum += a
		nsum += i + 1
	}
	return nsum - sum
}

func main() {
}
