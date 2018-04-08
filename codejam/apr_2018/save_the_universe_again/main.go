package main

import "fmt"
import "os"

type state struct {
	damage, power int
}

func Save(D int, P string) int {
	n := len(P)
	x := make([][]state, n+1)
	for i := 0; i <= n; i ++ {
		x[i] = make([]state, n)
	}
	// initial state
	for i := 0; i <= n; i ++ {
		x[0][i] = state{0, 1}
	}
	for i := 1; i <= n; i ++ {
		for j := 0; j <= n; j ++ {
			minDamage, power := 10000000, 0
			for k := 0; k <= j; k ++ {
				actualDamage =
				if P[i] == 'C' {
					power
				}
				x[i-1][k].damage
				if minDamage > x[i-1][k].damage {
					minDamage = x[i-1][k].damage
				}
			}
			x[i][j].damage = minDamage
			x[i][j].power = power
		}
	}
	return 0
}

func main() {
	var T, D int
	var P string
	if _, err := fmt.Fscanln(os.Stdin, &T); err != nil {
		panic(err)
	}
	for i := 1; i <= T; i ++ {
		if _, err := fmt.Fscanln(os.Stdin, &D); err != nil {
			panic(err)
		}
		if _, err := fmt.Fscanln(os.Stdin, &P); err != nil {
			panic(err)
		}
		sol := Save(D, P)
		if sol == -1 {
			fmt.Fprintf(os.Stdout, "Case #%d: IMPOSSIBLE\n", i)
		} else {
			fmt.Fprintf(os.Stdout, "Case #%d: %d\n", i, sol)
		}
	}
}

