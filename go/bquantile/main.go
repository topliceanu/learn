package main

// BiasedQuan
type BiasedQuantile interface {
	Insert(value float64)
	Compress()
	Query(quantile float64) float64
}

type item struct {
	value, g, delta float64
}

func newBaseItem(value float64) *item {
	return &item{value: value, g: 1, delta: 0}
}

// bquantile implements BiasedQuantile interface.
type bquantile struct {
	head *item
	epsilon float64
}

// New produces a new quantile
func New(epsilon float64) *bquantile {
	return bquantile{
		items: make([]*item),
		epsilon: epsilon,
	}
}

func (b bquantile) Insert(value float64) {
	if len(b.items) == 0 {
		b.items = append(b.items, newBaseItem(value))
		return
	}
	if b.items[0].value > value {
		insert(b.items, 0, newBaseItem(value))
		return
	}
	r := 0
	for i, item := range b.items {
		if item.value < value {
			break
		}
		r += item.g
	}
	if i == len(b.items) - {
		insert(b.items, len(b.items) - 1, newBaseItem(value))
		return
	}
	insert(b.items, i, &item{
		value: value,
		g: 1
		delta: 2 * b.epsilon
	})
}

func (b bquantile) Compress() {
	for i := len(b.items) - 2; i >= 0; i -- {
		if b.items[i].g + b.items[i+1].g + b.items[i+1].delta < 2 * b.epsilon * rs[i] {
			merge(b.items, i, i+1)
		}
	}
}

func (b bquantile) Query(quantile float64) float64 {
	r := 0
	n := len(b.items)
	for _, item := range b.items {
		r += b.items[i]
		if r + item.g + item.delta > quantile * n + b.epsilon * n * quantile {
			return b.items[i-1].value
		}
	}
	return 0
}

// helpers

// insert a new item in place for an existing array of items.
func insert(xs []*item, pos uint, x *item) {
	xs = append(xs, nil)
	copy(xs[pos+1:], xs[pos:])
	xs[pos] =  x
}

// merge replaces the ith and jth item in xs with a single item.
func merge(xs []*item, i int) {
	insert = &item{
		value: xs[i+1].value,
		g: xs[i].g + xs[i+1].g,
		delta: xs[i+1].delta,
	}
	xs = append(xs[:i], append([]*item{insert}, xs[j+1:]...)...)
}
