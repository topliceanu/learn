package main

import "fmt"

func main() {
	var a []int = []int{1,2,3}

	var b []int = make([]int, len(a))
	copy(b, a)

	fmt.Println(b)
	fmt.Println(a)
}
