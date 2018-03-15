package main

import (
	"math"
)

func Solution(X int, Y int, D int) int {
	return int(math.Ceil(math.Abs(float64(Y - X)) / float64(D)))
}

func main() {
}
