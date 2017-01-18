package main

import (
  "flag"
  "log"
)

func main() {
  flag.Parse()

  conn, err := grpc.Dial(*server, grpc.WithInsecure())
  if err != nil {
    log.Fatalf("fail to dial: %v", err)
  }
}
