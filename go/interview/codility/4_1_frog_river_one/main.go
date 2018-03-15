package main

func Solution(X int, A []int) int {
	covered := make([]bool, X)
	numCovered := 0
	for time, pos := range A {
		if !covered[pos - 1] {
			covered[pos - 1] = true
			numCovered += 1
			if numCovered == X {
				return time
			}
		}
	}
	return -1
}

func main() {
}
