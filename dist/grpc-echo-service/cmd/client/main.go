package main

import (
	"flag"
	"log"

	"github.com/learnscalability/grpc-echo-service/client"
	"github.com/learnscalability/grpc-echo-service/pb"
)

func main() {
	var (
		server, method, message string
		cl                      *client.Client
		err                     error
		ping                    *pb.Ping
	)
	flag.StringVar(&server, "server", ":3000", "server address `ip:port` to contact")
	flag.StringVar(&method, "method", "get", "method to use, either `send` or `subscribe`")
	flag.StringVar(&message, "message", "", "message to send to the server")
	flag.Parse()
	cl, err = client.NewClient(server)
	if err != nil {
		log.Fatalf("Failed to connect to the server %s with error %+v", server, err)
	}
	defer func() {
		err = cl.Close()
		if err != nil {
			log.Printf("Failed to close the client connection %+v\n", err)
		}
	}()
	ping = &pb.Ping{Message: message}
	switch method {
	case "send":
		cl.Send(ping)
	case "subscribe":
		cl.Subscribe(ping)
	default:
		log.Fatalf("Method %s not supported", method)
	}
}
