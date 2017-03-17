package main

import (
  "flag"
  "log"
  "net"

  "golang.org/x/net/context"
  "google.golang.org/grpc"
  "learn/grpc-routeguide/pb"
)

// implements pb.RouteGuideServer
type RouteGuideServer struct {

}

func (s *RouteGuideServer) GetFeature(ctx context.Context, p *pb.Point) (*pb.Feature, error) {
  return nil, nil
}

func (s *RouteGuideServer) ListFeatures(p *pb.Rectangle, stream pb.RouteGuide_ListFeaturesServer) error {
  return nil
}

func (s *RouteGuideServer) RecordRoute(stream pb.RouteGuide_RecordRouteServer) error {
  return nil
}

func (s *RouteGuideServer) RouteChat(stream pb.RouteGuide_RouteChatServer) error {
  return nil
}

func main() {
  var (
    lis net.Listener
    err error
    address string
    gs *grpc.Server
  )
  flag.StringVar(&address, "address", ":3000", "ip:port to bind to")
  flag.Parse()
  lis, err = net.Listen("tcp", address)
  if err != nil {
    log.Fatalf("failed to listen: %+v", err)
  }
  gs = grpc.NewServer()
  pb.RegisterRouteGuideServer(gs, &RouteGuideServer{})
  gs.Serve(lis)
}
