package main

import (
	"fmt"
	"math/rand"
)

const (
	win = 100
	gamesPerSeries = 10
)

// A general feature of the functional approach to programming is a global state
// object which gets passed arround from function to function. This makes things
// so much easier to reason about, given that there are no hidden state values.
type state struct {
	player int // Score for the current player.
	opponent int // Score for the other player.
	thisTurn int // Points accumulated by current player in the current turn.
}

type action func(current state) (result state, turnIsOver bool)

// Updates the current state of the game with the result of a random dice roll.
func roll(s state) (state, bool) {
	var outcome int = rand.Intn(6) + 1
	if outcome == 1 {
		return state{s.opponent, s.player, 0}, true
	}
	return state{s.player, s.opponent, outcome + s.thisTurn}, false
}

// A player has the option to stay and keep the value it has earned so far,
// ceeding the turn to the other player.
func stay(s state) (state, bool) {
	return state{s.opponent, s.player + s.thisTurn, 0}, true
}

// A strategy is a function that returns an action to take against the state of the game.
type strategy func(state) action

// Produces a strategy which returns a stay action if the current player
// reached a given number of points this turn. Alternatively, it return roll,
// untill the player hits the given barrier.
func stayAtK(k int) strategy {
	return func(s state) action {
		if s.thisTurn >= k {
			return stay
		}
		return roll
	}
}

// Simulate a play of the game where the first player uses strategy0 and the
// second player uses strategy1.
func play(strategy0, strategy1 strategy) int {
	var strategies []strategy = []strategy{strategy0, strategy1}
	var s state
	var turnIsOver bool
	var currentPlayer int = rand.Intn(2)
	for s.player + s.thisTurn < win {
		action := strategies[currentPlayer](s)
		s, turnIsOver = action(s) // override game state s after each action!
		if turnIsOver { // turn is over for the first player.
			currentPlayer = (currentPlayer + 1) % 2
		}
	}
	return currentPlayer
}

// We're interested in finding out the best strategy out of the input strategies.
// To do this, we record the number of wins for each strategy given that each combination of available strategies is played for 10 times.
func roundRobin(strategies []strategy) ([]int, int) {
	wins := make([]int, len(strategies))
	for i := 0; i < len(strategies); i += 1 {
		for j := i + 1; j < len(strategies); j += 1 {
			for k := 0; k < gamesPerSeries; k ++ {
				winner := play(strategies[i], strategies[j])
				if winner == 0 {
					wins[i] += 1
				} else {
					wins[j] += 1
				}
			}
		}
	}
	gamesPerStrategy := gamesPerSeries * (len(strategies) - 1)
	return wins, gamesPerStrategy
}

func ratioString(vals ...int) string {
	total := 0
	for _, val := range vals {
		total += val
	}
	s := ""
	for _, val := range vals {
		if s != "" {
			s := ", "
		}
		pct := 100 * float64(val) / float64(total)
		s += fmt.Sprintf("%d/%d (%0.1f%%)", val, total, pct)
	}
	return s
}

// Play all strategies with each other, and record the number of wins versus failures.
func main() {
	strategies := make([]strategy, win)
	for k := range strategies {
		strategies[k] =  stayAtK(k + 1)
	}
	wins, games := roundRobin(strategies)

	for k := range strategies {
		fmt.Println("Wins, losses staying at k = %4d: %s\n", k+1, ratioString(wins[k], games - wins[k]))
	}
}
