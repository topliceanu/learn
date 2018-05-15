package main

import "os"
import "fmt"
import "container/heap"
import "math"

// Basic idea:
// 1. find the closest rectangular shape to the square of A. This will improve the chances we will have room for the shape and lower the general error of the gopher digger.
// 2. build a heap of all the inner cells (leave the borders of the cell out), ordered by the number of neighbours.
// 3. When a cell has the max number of members pop it from the heap, otherwise put it back in even if it has been dug before.
// 4. Finish when the heap is empty.

func main() {
	var T, A int
	if _, err := fmt.Fscanln(os.Stdin, &T); err != nil {
		panic(err)
	}
	//fmt.Fprintln(os.Stderr, ">>>> T=", T)
	for i := 1; i <= T; i ++ {
		if _, err := fmt.Fscanln(os.Stdin, &A); err != nil {
			panic(err)
		}
		//fmt.Fprintln(os.Stderr, ">>>> A=", A)
		var s = NewSolution(A)
		for j := 1; j <= 1000; j ++ {
			I, J := s.Deploy()
			if _, err := fmt.Fprintf(os.Stdout, "%d %d\n", I+1, J+1); err != nil {
				panic(err)
			}
			//fmt.Fprintln(os.Stderr, ">>>> send", I, J)
			var jI, jJ int
			if _, err := fmt.Fscanf(os.Stdin, "%d %d", &jI, &jJ); err != nil {
				panic(err)
			}
			//fmt.Fprintln(os.Stderr, ">>>> read", jI-1, jJ-1)
			if jI == 0 && jJ == 0 {
				break // the current tests was SUCCESSFULL
			}
			if jI == -1 && jJ == -1 {
				panic("The judge indicates that the algo messed up somewhere!")
			}
			s.Ingest(jI-1, jJ-1)
			//prntMap(s.w.mat)
		}
	}
}

type Solution struct {
	w *world
}

func NewSolution(A int) *Solution {
	return &Solution{
		w: newWorld(A),
	}
}

func (s *Solution) Deploy() (x, y int) {
	if len(s.w.cells) == 0 {
		panic("algo shouldn't determine by itself when it is done!")
	}
	//prnt(s.w.cells)
	unsafe := heap.Pop(s.w)
	c := unsafe.(*cell)
	heap.Push(s.w, c)
	return c.x, c.y
}

func (s *Solution) Ingest(x, y int) {
	c := s.w.mat[x][y]
	if c.isDone {
		return
	}
	s.w.markAsDone(c)
}

type cell struct {
	x, y int
	isDone bool // the cell was already done.
	index int // the index of the cell in the heap, -1 if not present.
	count int // number of dug neighbours.
}

// world reference implements container/heap.Interface such that the top of the
// heap contains the cell which has the lowest number of neighbours.
type world struct {
	cells []*cell // heap!
	mat [][]*cell
	height, length int
}

func calculateRectangle(size int) (height int, length int) {
	if size <= 9 {
		return 3, 3
	}
	height = int(math.Floor(math.Sqrt(float64(size))))
	length = height + int(math.Ceil(float64(size - height * height) / float64(size)))
	return height, length
}

func newWorld(size int) *world {
	height, length := calculateRectangle(size)
	//fmt.Fprintln(os.Stderr, ">>>> height, length", height, length)
	var (
		mat = make([][]*cell, height)
		cells = make([]*cell, (height - 2) * (length - 2))
	)
	for i := 0; i < height; i ++ {
		mat[i] = make([]*cell, length)
		for j := 0; j < length; j ++ {
			mat[i][j] = &cell{i, j, false, -1, 0}
			if i > 0 && i < height - 1 && j > 0 && j < length - 1 {
				index := (i - 1) * (length - 2) + j - 1
				mat[i][j].index = index
				//fmt.Fprintln(os.Stderr, "------", i, j, index, len(cells))
				cells[index] = mat[i][j]
			}
		}
	}
	w := &world{cells, mat, height, length}
	heap.Init(w)
	return w
}

func (w *world) Len() int {
	return len(w.cells)
}

func (w *world) Less(i, j int) bool {
	return w.cells[i].count < w.cells[j].count // make it a min-heap!
}

func (w *world) Swap(i, j int) {
	w.cells[i], w.cells[j] = w.cells[j], w.cells[i]
	w.cells[i].index = i
	w.cells[j].index = j
}

func (w *world) Push(u interface{}) {
	c := u.(*cell)
	c.index = len(w.cells)
	w.cells = append(w.cells, c)
}

func (w *world) Pop() interface{} {
	old := w.cells
	n := len(old)
	x := old[n-1]
	w.cells = old[0 : n-1]
	x.index = -1
	return x
}

func (w *world) markAsDone(c *cell) {
	c.isDone = true
	if c.x+1 < w.height {
		w.incCount(c.x+1, c.y) // top
	}
	if c.y > 0 {
		w.incCount(c.x, c.y-1) // left
	}
	if c.y+1 < w.length {
		w.incCount(c.x, c.y+1) // right
	}
	if c.x > 0 {
		w.incCount(c.x-1, c.y) // bottom
	}
	if c.x+1 < w.height && c.y > 0 {
		w.incCount(c.x+1, c.y-1) // top-left
	}
	if c.x+1 < w.height && c.y+1 < w.length {
		w.incCount(c.x+1, c.y+1) // top-right
	}
	if c.x > 0 && c.y > 0 {
		w.incCount(c.x-1, c.y-1) // bottom-left
	}
	if c.x > 0 && c.y+1 < w.length {
		w.incCount(c.x-1, c.y+1) // bottom-right
	}
}

func (w *world) incCount(x, y int) {
	c := w.mat[x][y]
	c.count += 1
	if c.count == 8 {
		heap.Remove(w, c.index)
		c.index = -1
	} else {
		heap.Fix(w, c.index)
	}
}

/*
func prnt(xs []*cell) {
	for _, x := range xs {
		fmt.Fprintf(os.Stderr, "%+v; ", x)
	}
	fmt.Fprintln(os.Stderr, "")
}

func prntMap(xxs [][]*cell) {
	var n, m = len(xxs), len(xxs[0])
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if xxs[i][j].isDone {
				fmt.Fprint(os.Stderr, "x ")
			} else {
				fmt.Fprint(os.Stderr, "_ ")
			}
		}
		fmt.Fprintln(os.Stderr, "")
	}
}
*/
