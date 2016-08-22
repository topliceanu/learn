package main

import (
	"fmt"
	"net"
	"net/http"
	"html/template"
	"log"
	"io"
	"golang.org/x/net/websocket"
)

// setup an http and websocket server.

var partener = make(chan io.ReadWriteCloser)
var addr = "learn:4000"
var tpl = template.Must(template.New("root").Parse(`
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Chat Roulette</title>
		<script>
			var sock = new WebSocket("ws://{{.}}/socket");
			sock.onmessage = function (m) { console.log("Received:", m.data); }
			sock.onclose = function () { console.log("Closed!"); }
		</script>
	</head>
	<body>
	</body>
	</html>
`))

// implements io.ReadWriteCloser implicitly by embedding websocket.Conn
type socket struct {
	io.ReadWriter // embedded interface value!! instead of websocket.Conn
	done chan bool
}

func (s socket) Close() error {
	s.done<- true
	return nil
}

func main() {
	go tcpListen()
	http.HandleFunc("/", httpHandler)
	http.Handle("/socket", websocket.Handler(wsHandler))

	err := http.ListenAndServe(addr, nil)
	if err != nil {
		log.Fatal(err)
	}
}

func httpHandler(w http.ResponseWriter, r *http.Request) {
	tpl.Execute(w, addr)
}

func wsHandler(ws *websocket.Conn) {
	s := socket{ws, make(chan bool)}
	go match(s)
	<-s.done
}

// code to handle matching users.

// net.Conn implements in io.ReadWriteCloser implicitly.
func match(c io.ReadWriteCloser) {
	fmt.Fprintf(c, "Waiting for partener...\n")
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
	fmt.Fprintf(a, "Found one! Say hi.\n")
	fmt.Fprintf(b, "Found one! Say hi.\n")
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

// TODO bot to generate text.

// The same TCP chat server.
var tcpAddr = "0.0.0.0:4001"

func tcpListen() {
	l, err := net.Listen("tcp", tcpAddr)
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
