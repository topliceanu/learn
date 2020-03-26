package client

import (
	"context"
	"io"
	"log"

	"github.com/learnscalability/grpc-echo-service/pb"

	"google.golang.org/grpc"
)

// Client struct for the Echo RPC Service.
// Client reference implements pb.EchoClient
type Client struct {
	conn *grpc.ClientConn
	echo pb.EchoClient
}

// NewClient connects to the server url given.
func NewClient(server string) (*Client, error) {
	var (
		conn   *grpc.ClientConn
		err    error
		client pb.EchoClient
	)
	conn, err = grpc.Dial(server, grpc.WithInsecure())
	if err != nil {
		return nil, err
	}
	client = pb.NewEchoClient(conn)
	return &Client{
		conn: conn,
		echo: client,
	}, nil
}

// Close should be used with with the defer statement to always close the client connection before exit.
func (c *Client) Close() error {
	return c.conn.Close()
}

// Send encodes a Ping message and sends it to the echo server, the response will be printed to stdout.
func (c *Client) Send(ping *pb.Ping) {
	var (
		ctx    context.Context
		cancel context.CancelFunc
		pong   *pb.Pong
		err    error
	)
	ctx, cancel = context.WithCancel(context.Background())
	defer cancel()
	pong, err = c.echo.Send(ctx, ping)
	if err != nil {
		log.Fatalf("Send request failed with error %+v", err)
		return
	}
	log.Printf("Received pong %+v\n", pong)
}

// Subscribe encodes a Ping message, sends it, then opens a stream to receive Pong messages from the echo server.
func (c *Client) Subscribe(ping *pb.Ping) {
	var (
		ctx    context.Context
		cancel context.CancelFunc
		stream pb.Echo_SubscribeClient
		err    error
		pong   *pb.Pong
	)
	ctx, cancel = context.WithCancel(context.Background())
	defer cancel()
	stream, err = c.echo.Subscribe(ctx, ping)
	if err != nil {
		log.Fatalf("Failed to send ping request to server with error %+v", err)
		return
	}
	for {
		pong, err = stream.Recv()
		if err == io.EOF {
			log.Println("Subscription ended")
			return
		}
		if err != nil {
			log.Fatalf("Received error from server %+v", err)
			return
		}
		log.Printf("Received pong %+v\n", pong)
	}
}
