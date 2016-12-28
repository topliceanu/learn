package main

import (
  "net"

  "google.golang.org/grpc"
)

var addr string

type server struct {

}

func main() {
  listener, err := net.Listen("tcp", addr)
  if err != nil {
    log.Fatalf("Failed to bind to port: %v", err)
  }
  s := grpc.NewServer()
  Register
}
