package main

import (
	"flag"
	"log"

	"github.com/learnscalability/grpc-echo-service/server"
)

func main() {
	var (
		bind string
		srv  *server.Server
		err  error
	)
	flag.StringVar(&bind, "bind", "0.0.0.0:3000", "ip:port for the server to bind to")
	flag.Parse()
	srv = server.NewServer(bind)
	err = srv.Listen()
	if err != nil {
		log.Fatalf("Failed to start a new echo server with error %+v", err)
	}
}
