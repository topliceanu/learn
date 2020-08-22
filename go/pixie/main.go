package main

import (
	"math/rand"
)

type board struct {
	id uint64
	pins map[uint64]*pin
}

type user struct {
	id uint64
	history *pinLRU
}

type pin struct {
	id uint64
	boards map[uint64]*board
	weight float64
}

func basicRandomWalk(query *pin, alpha float64, maxSteps uint16 /*N*/) map[int64]uint32 {
	totSteps := 0
	pinVisits := make(map[uint64]uint32) // V
	currPin := query
	for totSteps < maxSteps {
		currSteps := sampleWalkLength(alpha)
		for i := 0; i < currSteps; i ++ {
			currBoard := pickRandBoard(currPin.boards)
			currPin := pickRandPin(currBoard.pins)
			incrVisit(pinVisits, currPin.id)
		}
		totSteps += currSteps
	}
	return pinVisists
}

func pixieRandomWalk(query *pin, usr *user, alpha float64, maxSteps uint64 /*N*/, nv, np uint32) map[uint64]uint32 {
	totSteps := 0
	pinVisits := make(map[uint64]uint32) // V
	nHighVisited := 0
	currPin := query
	for totSteps < maxSteps || nHighVisited > np{
		currSteps := sampleWalkLength(alpha)
		for i := 0; i < currSteps; i ++ {
			currBoard := pickPersonalisedBoard(currPin.boards, usr)
			currPin := pickPersonalisedPin(currBoard.pins, usr)
			incrVisit(pinVisits, currPin.id)
			if pinVisits[currPin.id] == nv {
				nHighVisited += 1
			}
		}
		totSteps += currSteps
	}
	return pinVisits
}

func pixieRandomWalkMultiple(query []*pin, usr *User, alpha float64, maxSteps uint64 /*N*/) {
	pinVisits := make(map[uint64]uint32)
	for i := 0; i < len(query); i ++ {
		q := query[i]
		interimVisits := pixieRandomWalk(q, usr, alpha, nv, np)
		pinVisits = mergeVisits(pinVisits, interimVisits)
	}
}


// Helpers

func pickRandBoard(boards map[uint64]*board) *board {
	// ..
}

func pickRandPins(pins map[uint64]*pins) *pins {
	// ..
}

func pickPersonalisedBoard(boards map[uint64]*board, _ *user) *board {
	// ...
	return pickRandBoard(boards)
}

func pickPersonalisedPin(pins map[uint64]*pin, _ *user) *pin {
	// ...
	return pickRandPin(pins)
}

func inrcVisit(visits map[uint64]uint32, pinId uint64) {
	// ..
}

func mergeVisits(v1 v2 map[uint64]uint32) map[uint64]uint32

/*
import (
	"math"
	"math/rand"
)



// SampleWalkLength computes the number of steps for a random walk given a parameter alpha.
func SampleWalkLength(alpha float64) int {
	// TODO come up with a better solution, maybe to include N
	return int(alpha)
}

// edge is a pair of two pin ids.
type edge struct {
	p int // id of the pin in the edge
	b int // id of the board in the edge
	f features // set of feature ids of the edge.
}

// BasicRandomWalk computes a random walk for a single query pin.
// q the query pin, ie. the starting point of the algorithm.
// E the total set of edges in the graph.
// alpha is a parameter to determine the length of each individual walk.
// N is total number of steps allowed for across all walks in a run.
func BasicRandomWalk(q int, E []edge, alpha float64, N int) map[int]int {
	var (
		totSteps = 0
		currPin int
		currBoard int
		V = make(map[int]int)
		i int
		found bool
		currSteps int
	)
	for {
		currPin = q
		currSteps = SampleWalkLength(alpha)
		for i = 1; i <= currSteps; i ++ {
			currBoard = randPick(boards(currPin, E))
			currPin = randPick(pins(currBoard, E))
			if _, found = V[currPin]; !found {
				V[currPin] = 1
			}
			V[currPin]++
		}
		totSteps += currSteps
		if totSteps >= N {
			break
		}
	}
	return V
}

// boards returns all the boards a pin p is in, essentially E(p) from the paper.
func boards(p int, edges []edge) []int {
	// TODO a more efficient implementation
	out := []int{}
	for _, e := range edges {
		if e.p == p  {
			out = append(out, e.b)
		}
	}
	return out
}

// pins returns all the pins inside the board b, essentially E(b) from the paper.
func pins(b int, edges []edge) []int {
	// TODO find a more eficint implementation
	out := []int{}
	for _, e := range edges {
		if e.b == b  {
			out = append(out, e.p)
		}
	}
	return out
}

func randPick(ids []int) int {
	return ids[rand.Intn(len(ids))] // TODO initialize the rand with a different seed in init().
}

// features are a list of labels, in this case we only store the ids of those labels.
type features []int

// labels contains a mapping of label_id => label_name
var labels map[int][]string

// PixieRandomWalk is a random walk with the pixie improvements.
// q - the query pin.
// U - user features as a set of tags.
// E - the set of edges, in effect the entire bipartite graph.
// alpha - a parameter to determine the length of each individual walk. ????
// N - the total number of steps across all the pins in the query.
// (np, nv) - the algorithm terminates the walk when at least np candidates have been visited at least nv times.
func PixieRandomWalk(q int, E []edge, U features, alpha float64, N, np, nv int) map[int]int {
	var (
		totSteps = 0
		V = make(map[int]int)
		nHighVisited = 0
		currPin int
		currBoard int
		currSteps int
		found bool
	)
	for {
		currSteps = SampleWalkLength(alpha)
		for i := 1; i <= currSteps; i ++ {
			currBoard = PersonalisedBoard(boards(currPin, E), U)
			currPin = PersonalisedPin(pins(currBoard, E), U)
			if _, found = V[currPin]; !found {
				V[currPin] = 1
			}
			V[currPin]++
			if V[currPin] == nv {
				nHighVisited++
			}
		}
		totSteps += currSteps
		if totSteps >= N || nHighVisited > np {
			break
		}
	}
	return V
}

// globals structures containing the set of feature ids for each pin and board.
var pinsXfeatures map[int][]int
var boardsXfeatures map[int][]int

// PersonalisedBoard picks a neighbouring board with a bias towards the given features.
func PersonalisedBoard(ids []int, U features) int {
	// TODO find a better implementation.
	return ids[0]
}

// PersonalisedPin picks a neighbouring pin with a bias towards the given features.
func PersonalisedPin(ids []int, U features) int {
	// TODO find a better implementation.
	return ids[0]
}

// PixieRandomWlakMultiple is the main method executed.
// Q is a set of start query pins.
// W is a set of weights for the given query pins.
func PixieRandomWlakMultiple(Q []int, W []float64, E []edge, U features, alpha float64, N int) map[int]int {
	var (
		Vq = make(map[int]map[int]int)
		V = make(map[int]int)
		Nq, np, nv int
		i int
		q, p int
	)
	for i, q = range Q {
		Nq = allocateSteps(i, N, Q, W, E)
		np, nv = int(N/2), int(N/2) // TODO find better approximations.
		Vq[q] = PixieRandomWalk(q, E, U, alpha, Nq, np, nv)
	}
	for p = range Vq {
		V[p] = multiHitBooster(Vq[p]) // TODO follow equation 3. from the paper.
	}
	return V
}

func multiHitBooster(vq map[int]int) int {
	sum := 0.0
	for _, v := range vq {
		sum += math.Sqrt(float64(v))
	}
	return int(sum * sum)
}

// allocateSteps implements the equation 2. from the paper.
func allocateSteps(i, N int, Q []int, W []float64, E []edge) int {
	q := Q[i]
	sq := scalingFactor(q, E)
	sums := 0.0
	for _, r := range Q {
		sums += scalingFactor(r, E)
	}
	wq := W[i]
	return int(wq * float64(N) * sq / sums)
}

// C is the maximum number of boards a pin can be linked to!
const C = 100 // TODO this has to be pre-computed!

// scalingFactor implements equation 1. from the paper.
func scalingFactor(q int, E []edge) float64 {
	bs := boards(q, E)
	sq := float64(len(bs)) * (C - math.Log(float64(len(bs)))) // equation 1. from the paper.
	return sq
}

func main() {
	// TODO
}

// Data structures.

type graph struct {
	offsets []int
	neighbours []int
}

// newGraph takes in a list of pairs, each representing an edge between two
func newGraph(n int, edges [][]int) *graph {
	adjacency := make(map[int][]int, n)
	for _, e := range edges {
		i, j := e[0], e[1]
		if _, found := adjacency[i]; !found {
			adjacency[i] = []int{j}
		} else {
			adjacency[i] = append(adjacency[i], j)
		}
	}
	offsets := make([]int, n)
	neighbours := make([]int, len(edges) * 2)
	j := 0
	for i := 0; i < n; i ++ {
		offsets[i] = j
		if xs, found := adjacency[i]; !found {
			continue
		} else {
			for _, x := range xs {
				neighbours[j] = x
				j++
			}
		}
	}
	return &graph{offsets, neighbours}
}

// Neighbours calculates neighbouring pins given the id of a board.
// OR the neighbouring boards given the id of a pin.
func (g *graph) Neighbours(id int) []int {
	start := g.offsets[id]
	end := g.offsets[id+1] - 1
	return g.neighbours[start:end]
}

func (g *graph) CountNeighbours(id int) int {
	if len(g.offsets) == id - 1 {
		return len(g.neighbours) - g.offsets[id]
	}
	return g.offsets[id+1] - g.offsets[id]
}
*/
