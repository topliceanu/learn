package main

import (
	"fmt"
	"sort"
)

// Define a type which implements the sort.Interface
type ByLength []string

func (b ByLength) Len() int {
	return len(b)
}

func (b ByLength) Swap(i, j int) {
	b[i], b[j] = b[j], b[i]
}

func (b ByLength) Less(i, j int) bool {
	return len(b[i]) < len(b[j])
}

func main() {
	a := []int{3, 2, 1, 6, 5, 4}
	fmt.Printf("Initial array: %v, is sorted: %t\n", a, sort.IntsAreSorted(a))
	sort.Ints(a)
	fmt.Printf("After sort: %v, is sorted: %t\n", a, sort.IntsAreSorted(a))

	var b ByLength = ByLength([]string{"abcd", "efg", "hi", "j"})
	sort.Sort(b)
	fmt.Printf("After sort: %v, is sorted %t\n", b, sort.IsSorted(b))
}
