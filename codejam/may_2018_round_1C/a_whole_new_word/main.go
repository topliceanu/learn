package main

import "fmt"
import "os"

func main() {
	var (
		T, N, L int
		line string
		A []string
		err error
		word string
		i, j int
	)
	if _, err = fmt.Fscanln(os.Stdin, &T); err != nil {
		panic(err)
	}
	//fmt.Fprintln(os.Stderr, ">>>> T=", T)
	for i = 1; i <= T; i ++ {
		if _, err := fmt.Fscanf(os.Stdin, "%d%d", &N, &L); err != nil {
			panic(err)
		}
		//fmt.Fprintln(os.Stderr, ">>>> N, L", N, L)
		A = make([]string, N)
		for j = 0; j < N; j ++ {
			if _, err = fmt.Fscan(os.Stdin, &line); err != nil {
				panic(err)
			}
			A[j] = line
		}
		word = Solution(A)
		if _, err = fmt.Fprintf(os.Stdout, "Case #%d: %s", i, word); err != nil {
			panic(err)
		}
	}
}

func Solution(A []string) string {
	layers := parseGraph(A)
	soFar := ""
	for i, l := range layers {
		if i + 1 < l - 1 {
			next := layers[i + 1]
		} else {
			next := []*Node{}
		}
		for _, n := range l {
			available := diff(next, n.children)
			if len(available) != 0 {
				soFar += n.letter
				return depthFirst(soFar, available[0])
			}
		}
	}
	return "-"
}

type Node struct {
	letter string
	children []*Node
}

type Layer []*Node

func parseGraph(A []string) []Layer {
	N := len(A)
	L := len(A[0])
	layers := make([]Layer, L)
	for i := L-1; i >= 0 ; i -- {
		l := Layer{}
		for j := 0; j < N; j ++ {
			children := make(
			n := &Node{
				letter: A[j][i],
				children: children,
			}
			l = append(l, n)
		}
		layers[i] = l
	}
	return layers
}

func diff(set, subset []*Node) []*Node {
	index := make(map[string]struct{}, len(subset))
	for _, s := range subset {
		index[s.letter] = struct{}{}
	}
	out := []*Node{}
	for _, s := range set {
		if _, found := index[s.letter]; !found {
			out = append(out, s)
		}
	}
	return out
}

func depthFirst(soFar string, n *Node) string {
	if n == nil {
		return soFar
	}
	if len(n.children) == 0 {
		return soFar + n.letter
	}
	return depthFirst(soFar + n.letter, n.children[0])
}

