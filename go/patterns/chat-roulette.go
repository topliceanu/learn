package main

import (
	"fmt"
	"io"
	"log"
	"net"
)

var partener = make(chan io.ReadWriteCloser)

// net.Conn implements in io.ReadWriteCloser implicitly.
func match(c io.ReadWriteCloser) {
	fmt.Println(c, "Waiting for partener...")
	// Let go's scheduler pair parteners toghether: all match goroutines will
	// block on writing themselves to the partners queue or reading a partner from
	// the queue to chat with. When at least two match go routines exist, this
	// pairing is done by the scheduler and BOOM! they're chatting.
	select {
	case partener <- c:
		// now handled by the other goroutine.
	case p := <-partener:
		chat(p, c)
	}
}

func chat(a, b io.ReadWriteCloser) {
	fmt.Fprintf(a, "Found one! Say hi.")
	fmt.Fprintf(b, "Found one! Say hi.")
	errc := make(chan error, 1)
	go cp(a, b, errc)
	go cp(b, a, errc)
	if err := <-errc; err != nil {
		log.Println(err)
	}
	a.Close()
	b.Close()
}

func cp(w io.Writer, r io.Reader, errc chan<- error) {
	_, err := io.Copy(w, r)
	errc<- err
}

func main() {
	l, err := net.Listen("tcp", "0.0.0.0:4000")
	if err != nil {
		log.Fatal(err)
	}

	for {
		conn, err := l.Accept()
		if err != nil {
			log.Fatal(err)
		}
		go match(conn)
	}
}
