package main

import "fmt"

func main() {
	for i, r := range "alexandru" {
		fmt.Printf("index=%d value=%v : %T\n", i, r, r)
	}
}
