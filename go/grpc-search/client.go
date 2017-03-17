package main

import (
	"context"
	"flag"
	"fmt"
  "io"
	"log"
	"time"

	"google.golang.org/grpc"
	pb "learn/grpc-search/rpc"
)

func main() {
	var (
		conn   *grpc.ClientConn
		err    error
		server string
		client pb.GoogleClient
		mode   string
		query  string
	)
	flag.StringVar(&mode, "mode", "search", "search or watch")
	flag.StringVar(&query, "query", "", "query to send to the backends")
	flag.StringVar(&server, "server", "0.0.0.0:3000", "server address")
	flag.Parse()
	conn, err = grpc.Dial(server, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to dial %v", err)
	}
	defer conn.Close()
	client = pb.NewGoogleClient(conn)
	switch mode {
	case "search":
		search(client, query)
	case "watch":
		watch(client, query)
	default:
		log.Fatalf("unknown mode %q", mode)
	}
}

func search(client pb.GoogleClient, query string) {
	var (
		ctx    context.Context
		cancel context.CancelFunc
		req    *pb.Request
		res    *pb.Result
		err    error
	)
	ctx, cancel = context.WithTimeout(context.Background(), 80 * time.Millisecond)
	defer cancel()
	req = &pb.Request{
		Query: query,
	}
	res, err = client.Search(ctx, req)
	if err != nil {
		log.Fatalf("failed to query the server %+v", err)
	}
	fmt.Println(res)
}

func watch(client pb.GoogleClient, query string) {
	var (
		ctx    context.Context
		cancel context.CancelFunc
		err    error
    req *pb.Request
    stream pb.Google_WatchClient
    res *pb.Result
	)
	ctx, cancel = context.WithCancel(context.Background())
	defer cancel()
	req = &pb.Request{
		Query: query,
	}
	stream, err = client.Watch(ctx, req)
	if err != nil {
		log.Fatalf("failed to start streaming request %+v", err)
	}
	for {
		res, err = stream.Recv()
		if err == io.EOF {
			fmt.Println("watch ended")
			return
		}
		if err != nil {
			log.Fatal("Failed to read from stream %+v", err)
			return
		}
		fmt.Println(res)
	}
}
