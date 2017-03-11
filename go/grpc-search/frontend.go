package main

import (
	"flag"
	"log"
	"net"

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
