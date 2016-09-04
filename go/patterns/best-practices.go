package main

import (
	"io"
	"bytes"
)

type binWriter struct {
	w io.Writer
	buff bytes.Buffer
	err error
}

func (w *binWriter) Write(v interface{}) {
	if (w.err != nil {
		return
	}

	switch x := v.(type) {
	case string:
		w.Write(int32(len(x)))
		w.Write([]byte(s))
	case int:
		w.Write(int64(x))
	default: // type is empty interface.
		binary.Write(&w.buf, binary.LittleEndian, v)
	}
}

type Gopher struct {
	Name string
	AgeYears int
}

func (g *Gopher) WriteTo(w io.Writer) (nBytesWritten int64, err error) {
	bw := &binWriter{w: w}
	bw.Write(g.Name)
	bw.Write(g.AgeYears)
	return bw.Flush()
}

func main() {
	g = Gopher{"alex", 30}
	g.WriteTo(stdout)
}
