package main

import (
	"flag"
	"fmt"
	"log"
	"math/rand"
	"net"
	"time"

	context "golang.org/x/net/context"
	"golang.org/x/net/trace"
	"google.golang.org/grpc"
	pb "learn/grpc-search/rpc"
)

func main() {
	var (
		ln    net.Listener
		err   error
		g     *grpc.Server
		srv   pb.GoogleServer
		index uint
		bind  string
	)
	flag.UintVar(&index, "index", uint(0), "the index of the current server")
	flag.StringVar(&bind, "bind", "0.0.0.0:3000", "ip:port for the server to listen to")
	flag.Parse()
	ln, err = net.Listen("tcp", bind)
	if err != nil {
		log.Fatalf("Failed to start tcp backend %d: %+v", index, err)
	}
	g = grpc.NewServer()
	srv = &backend{
		index: index,
	}
	pb.RegisterGoogleServer(g, srv)
	g.Serve(ln)
}

// implements pb.GoogleServer
type backend struct {
	index uint
}

func (b *backend) Search(ctx context.Context, req *pb.Request) (*pb.Result, error) {
	var (
		d time.Duration
	)
	d = randDuration(100) * time.Millisecond
	logSleep(ctx, d)
	select {
	case <-time.After(d):
		return &pb.Result{
			Title: fmt.Sprintf("result for %s from backend %d", req.Query, b.index),
		}, nil
	case <-ctx.Done():
		return nil, ctx.Err()
	}
}

func (b *backend) Watch(req *pb.Request, stream pb.Google_WatchServer) error {
	var (
		ctx context.Context
		i   int
		d   time.Duration
	)
	ctx = stream.Context()
	for i = 0; ; i++ {
		d = randDuration(100) * time.Millisecond
		logSleep(ctx, d)
		select {
		case <-time.After(d):
      log.Print("Send event")
			err := stream.Send(&pb.Result{
				Title: fmt.Sprintf("result %d for [%s] from backend %d", i, req.Query, b.index),
			})
			if err != nil {
				return err
			}
		case <-ctx.Done():
			return ctx.Err()
		}
	}
}

func randDuration(n int) time.Duration {
	return time.Duration(int64(rand.Intn(n)))
}

func logSleep(ctx context.Context, d time.Duration) {
	var (
		tr trace.Trace
		ok bool
	)
	if tr, ok = trace.FromContext(ctx); ok {
		tr.LazyPrintf("sleeping for %d", d)
	}
}
