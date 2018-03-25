package main

import "math"

// HeapSort time complexity O(NlogN), space complexity O(N)
func HeapSort(A []int) []int {
	h := heapify(A)
	out := make([]int, len(A))
	for i := 0; len(h) > 0; i++ {
		out[i] = h.min()
	}
	return out
}

type heap []int

func heapify(data []int) heap {
	h := heap(data)
	for i := range h {
		h.bubbleDown(i)
	}
	return h
}

func (h heap) min() int {
	n := len(h) - 1
	h[0], h[n] = h[n], h[0]
	out := h[n]
	h = h[:n-1]
	h.bubbleDown(0)
	return out
}

func (h heap) insert(i int) {
	h = append(h, i)
	h.bubbleUp(len(h) - 1)
}

func (h heap) bubbleUp(i int) {
	if i == 0 {
		return
	}
	p := int(math.Ceil(float64(i) / 2))
	if h[p] > h[i] {
		h[p], h[i] = h[i], h[p]
		h.bubbleUp(p)
	}
}

func (h heap) bubbleDown(i int) {
	l := i*2 + 1
	r := i*2 + 2
	m := h.indexWithMinValue(i, l, r)
	if m == i {
		return
	}
	h[i], h[m] = h[m], h[i]
	h.bubbleDown(m)
}

func (h heap) indexWithMinValue(i, l, r int) int {
	var out int
	if h[l] < h[r] {
		out = l
	} else {
		out = r
	}
	if h[out] > h[i] {
		out = i
	}
	return out
}
