package main

import "fmt"
import "math"

func SenateEvacuation(parties []int) []string {
	// The idea is to, initially, build a max-heap with all the (partyName, numMembers) pairs sorted by numMembers.
	// At each iteration, pop the max pair, to get the first senator, decrease the numMembers for the party and push it back in the heap.
	// Do this again to get the second senator.
	// Stop when the heap is empty
	fmt.Printf(">>>>%v\n", rune(byte(51)))
	h := makeMaxHeap(parties)
	out := []string{}
	row := ""
	count := 0
	for !h.empty() {
		p := h.pop()
		p.numMembers -= 1
		if p.numMembers > 0 {
			h.push(p)
		}
		switch count {
		case 0:
			row = fmt.Sprintf("%s%c", row, p.name)
			count += 1
		case 1:
			row = fmt.Sprintf("%s%c", row, p.name)
			out = append(out, row)
			row = ""
			count = 0
		}
	}
	return out
}

type party struct {
	name byte
	numMembers int
}

type maxHeap struct {
	contents []*party
}

func makeMaxHeap(parties []int) *maxHeap {
	contents := []*party{}
	for i := 0; i < len(parties); i ++ {
		contents = append(contents, &party{
			name: byte(51 + i),
			numMembers: parties[i],
		})
	}
	h := &maxHeap{contents}
	for i := 0; i < len(h.contents); i ++ {
		h.bubbleDown(i)
	}
	return h
}

func (mh *maxHeap) push(p *party) {
	mh.contents = append(mh.contents, p)
	mh.bubbleUp(len(mh.contents) - 1)
}

// make sure you call empty() before!
func (mh *maxHeap) pop() *party {
	n := len(mh.contents) - 1
	mh.contents[0], mh.contents[n] = mh.contents[n], mh.contents[0]
	p := mh.contents[n]
	mh.contents = mh.contents[:n]
	mh.bubbleDown(0)
	return p
}

func (mh *maxHeap) empty() bool {
	return len(mh.contents) == 0
}

func (mh *maxHeap) bubbleUp(i int) {
	if i == 0 {
		return
	}
	pi := int(math.Floor(float64(i - 1) / 2))
	if mh.contents[i].numMembers < mh.contents[pi].numMembers {
		return
	}
	mh.contents[i], mh.contents[pi] = mh.contents[pi], mh.contents[i]
	mh.bubbleUp(pi)
}

func (mh *maxHeap) bubbleDown(i int) {
	li := i * 2 + 1
	ri := i * 2 + 2
	m := mh.indexWithMaxValue(i, li, ri)
	if i == m {
		return
	}
	mh.contents[i], mh.contents[m] = mh.contents[m], mh.contents[i]
	mh.bubbleDown(m)
}

func (mh *maxHeap) indexWithMaxValue(i, j, k int) int {
	var l int
	if j >= len(mh.contents) {
		return i
	}
	if k >= len(mh.contents) {
		if mh.contents[i].numMembers > mh.contents[j].numMembers {
			return i
		}
		return j
	}
	if mh.contents[i].numMembers > mh.contents[j].numMembers {
		l = i
	} else {
		l = j
	}
	if mh.contents[l].numMembers > mh.contents[k].numMembers {
		l = k
	}
	return l
}

func main() {}
