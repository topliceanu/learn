package main

import (
  "context"
  "io"
  "log"
  "flag"
  "google.golang.net/grpc"
  "learn/grpc-routeguide/pb"
)

func main() {
  var (
    address string
    command string
    args []string
    conn *grpc.ClientConn
    err error
    client RouteGuideClient
    feature *pb.Feature
    stream *pb.Stream
    lo, hi *pb.Point
  )
  flag.StringVar(&address, "address", "0.0.0.0:3000", "server address to contact")
  flag.Parse()
  command = flag.Args[0]
  conn, err = grpc.Dial(address)
  if err != nil {
    log.Fatalf("Failed to contact server with error %+v", err)
  }
  defer conn.Close()
  client = pb.NewRouteGuideClient(conn)
  switch command {
  case "get-feature":
    // Simple RPC
    feature, err = client.GetFeature(context.Background(), &pb.Point{flag.Args[1], flag.Args[2]})
    if err != nil {
      log.Fatalf("GetFeature failed with error %+v", err)
    }
  case "list-features":
    lo = &pb.Point{flag.Args[1], flag.Args[2]}
    hi = &pb.Point{flag.Args[3], flag.Args[4]}
    stream, err = client.ListFeatures(context.Background(), &pb.Rectangle{lo, hi})
    if err != nil {
      log.Fatalf("ListFeatures failed with error %+v", err)
    }
    for {
      feature, err = stream.Recv()
      if err == io.EOF {
        log.Println("Done listing features")
        break
      }
      if err != nil {
        log.Fatalf("Recv failed with error %+v", err)
      }
      log.Printf("Feature %v", feature)
    }
  case ""
    // TODO
  }
}
