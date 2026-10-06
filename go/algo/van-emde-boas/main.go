package main

import "math"

// See https://en.wikipedia.org/wiki/Van_Emde_Boas_tree
type VEBNode struct {
	size     uint
	min, max uint
	summary  []bool
	clusters []*VEBNode
}

func NewVEBNode(size uint) *VEBNode {
	return &VEBNode{
		size:    size,
		min:     256,
		max:     0,
		summary: make([math.Sqrt(size)]uint),
	}
}

func (v *VEBNode) Insert(val uint) {
	if v.isEmpty() {
		v.min = val
		v.max = val
		return
	}
	if val < v.min {
		v.min = val
	} else if val > v.max {
		v.max = val
	}
}
