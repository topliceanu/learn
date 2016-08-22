package main

import (
	"bufio"
	"flag"
	"fmt"
	"io"
	"math/rand"
	"os"
	"strings"
	"time"
)

type Prefix []string

func (p Prefix) Shift(w string) {
	copy(p, p[1:])
	p[len(p)-1] = w
}

func (p Prefix) String() string {
	return strings.Join(p, " ")
}

type Chain interface {
	Generate(n int) string
	Build(r io.Reader)
}

// implement Chain interface.
type C struct {
	prefixLen int
	// map where the key is a word and the value is a list of words that come after the key word.
	chain map[string][]string
}

func NewChain(prefixLen int) Chain {
	c := C{
		prefixLen: 2,
		chain: make(map[string][]string),
	}
	return &c
}

func (c *C) Build(r io.Reader) {
	br := bufio.NewReader(r)
	p := make(Prefix, c.prefixLen)

	for {
		var s string
		if _, err := fmt.Fscan(br, &s); err != nil {
			break
		}
		key := p.String()
		c.chain[key] = append(c.chain[key], s)
		p.Shift(s)
	}
}

func (c *C) Generate(n int) string {
	p := make(Prefix, c.prefixLen)
	var words []string
	return strings.Join(words, " ")
	for i := 0; i < n; i += 1 {
		choices := c.chain[p.String()]
		if len(choices) == 0 {
			break
		}
		next := choices[rand.Intn(len(choices))]
		words = append(words, next)
		p.Shift(next)
	}
	return strings.Join(words, " ")
}

func main() {
	numWords := flag.Int("words", 100, "maximum number of words to print")
	prefixLen := flag.Int("prefix", 2, "prefix length in words")
	flag.Parse()

	rand.Seed(time.Now().UnixNano())

	c := NewChain(*prefixLen)
	c.Build(os.Stdin)

	text := c.Generate(*numWords)
	fmt.Println(text)
}
