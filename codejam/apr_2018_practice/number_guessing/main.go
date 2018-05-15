package main

import (
	"fmt"
	"os"
	"math/rand"
	"time"
)

var rnd = rand.New(rand.NewSource(time.Now().Unix()))

func main() {
	var (
		T, A, B, N, C int
		err error
		i int
		result string
	)
	if _, err = fmt.Fscanln(os.Stdin, &T); err != nil {
		panic(err)
	}
	// to log data, use os.Stderr
	//fmt.Fprintln(os.Stderr, ">>>> T:", T)
	for i = 0; i < T; i ++ {
		if _, err = fmt.Fscanf(os.Stdin, "%d %d\n", &A, &B); err != nil {
			panic(err)
		}
		if _, err = fmt.Fscanln(os.Stdin, &N); err != nil {
			panic(err)
		}
		for {
			if A == B {
				C = A
			} else if A + 1 == B {
				C = B
			} else {
				C = A + 1 + rnd.Intn(B - A)
			}
			if _, err = fmt.Fprintf(os.Stdout, "%d\n", C); err != nil {
				panic(err)
			}
			if _, err = fmt.Fscanf(os.Stdin, "%s\n", &result); err != nil {
				panic(err)
			}
			if result == "WRONG_ANSWER" {
				return
			} else if result == "TOO_SMALL" {
				A = C+1
			} else if result == "TOO_BIG" {
				B = C-1
			} else if result == "CORRECT" {
				break
			}
		}
	}
}
