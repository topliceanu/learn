package main

import (
	"flag"
	"log"
	"net"
	"sync"

	context "golang.org/x/net/context"
	"google.golang.org/grpc"
	pb "learn/grpc-search/rpc"
)

func main() {
	var (
		ln       net.Listener
		err      error
		g        *grpc.Server
		srv      *frontend
		bind     string
		backends []string
		i        int
		b        string
	)
	flag.StringVar(&bind, "bind", "0.0.0.0:3000", "ip:port for the server to listen to")
	flag.Parse()
	backends = flag.Args()
	ln, err = net.Listen("tcp", bind)
	if err != nil {
		log.Fatalf("Failed to start tcp frontend %+v", err)
	}
	g = grpc.NewServer()
	srv = &frontend{
		clients: make([]pb.GoogleClient, len(backends)),
	}
	for i, b = range backends {
		conn, err := grpc.Dial(b, grpc.WithInsecure())
		if err != nil {
			log.Fatalf("Failed to contact backend %s %+v", b, err)
		}
		defer conn.Close()
		client := pb.NewGoogleClient(conn)
		srv.clients[i] = client
	}
	pb.RegisterGoogleServer(g, srv)
	g.Serve(ln)
}

// implements pb.GoogleServer
type frontend struct {
	clients []pb.GoogleClient
}

type result struct {
	res *pb.Result
	err error
}

func (f *frontend) Search(ctx context.Context, req *pb.Request) (*pb.Result, error) {
	var (
		results chan result
		gc      pb.GoogleClient
	)
	results = make(chan result, len(f.clients))
	for _, gc = range f.clients {
		go func(c pb.GoogleClient) {
			res, err := c.Search(ctx, req)
			results <- result{res, err}
		}(gc)
	}
	first := <-results
	return first.res, first.err
}

func (f *frontend) Watch(req *pb.Request, stream pb.Google_WatchServer) error {
	var (
		ctx     context.Context
		results chan result
		wg      sync.WaitGroup
		c       pb.GoogleClient
		res     result
    err     error
	)
	ctx = stream.Context()
	results = make(chan result)
	for _, c = range f.clients {
		wg.Add(1)
		go func(gc pb.GoogleClient) {
			defer wg.Done()
			watchBackend(ctx, gc, req, results)
		}(c)
	}
	go func() {
		wg.Wait()
		close(results)
	}()
	for res = range results {
		if res.err != nil {
			return res.err
		}
		if err = stream.Send(res.res); err != nil {
			return err
		}
	}
	return nil
}

func watchBackend(ctx context.Context, gc pb.GoogleClient, req *pb.Request, results chan result) {
	var (
		stream pb.Google_WatchClient
		err    error
		res    *pb.Result
	)
	stream, err = gc.Watch(ctx, req)
	if err != nil {
		select {
		case results<- result{err: err}:
		case <-ctx.Done():
		}
		return
	}
	for {
		res, err = stream.Recv()
		select {
		case results <- result{res, err}:
			if err != nil {
				return
			}
		case <-ctx.Done():
			return
		}
	}
}
