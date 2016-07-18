package main

import (
	"io"
	"fmt"
	"log"
	"net/http"
	"html/template"

	"golang.org/x/net/websocket"
)

var rootTemplate = template.Must(template.New("root").Parse(`
	<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>My websocket site</title>
		</head>
		<body>
			<script>
			var ws = new WebSocket("ws://{{.}}/socket");
			ws.onmessage = onMessage;
			ws.onclose = onClose;
			</script>
		</body>
	</html>
`))

var listenAddress string = "0.0.0.0:4000"

func rootHandler(c *websocket.Conn) {
	rootTemplate.Execute(w, listenAddress)
}

func socketHandler() {
}

func main() {
	http.HandleFunc("/", rootHandler)
	http.Handle("/socket", websocket.Handler(socketHandler))
	err := http.ListenAndServe(listenAddress, nil)
	if err != nil {
		log.Fatal(err)
	}
}
