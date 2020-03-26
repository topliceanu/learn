package server

import (
	"net"
	"time"

	"github.com/learnscalability/grpc-echo-service/pb"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

// Server wraps the Echo RPC server.
// Server implements pb.EchoServer
type Server struct {
	bind string
}

// NewServer creates a new rpc server.
func NewServer(bind string) *Server {
	return &Server{bind}
}

// Listen binds the server to the indicated interface:port.
func (s *Server) Listen() error {
	var (
		ln  net.Listener
		err error
		srv *grpc.Server
	)
	ln, err = net.Listen("tcp", s.bind)
	if err != nil {
		return err
	}
	srv = grpc.NewServer()
	pb.RegisterEchoServer(srv, s)
	return srv.Serve(ln)
}

// Send handles Ping messages by simply returning the same message wrapped in a Pong type.
func (s *Server) Send(ctx context.Context, ping *pb.Ping) (*pb.Pong, error) {
	return &pb.Pong{
		Message:   ping.Message,
		Timestamp: time.Now().Unix(),
	}, nil
}

// Subscribe will return the contents of the Ping message every second in a stream.
func (s *Server) Subscribe(ping *pb.Ping, stream pb.Echo_SubscribeServer) error {
	var (
		ticker    *time.Ticker
		ctx       context.Context
		timestamp time.Time
		err       error
	)
	ticker = time.NewTicker(1 * time.Second)
	ctx = stream.Context()
	for {
		select {
		case timestamp = <-ticker.C:
			err = stream.Send(&pb.Pong{
				Message:   ping.Message,
				Timestamp: timestamp.Unix(),
			})
			if err != nil {
				return err
			}
		case <-ctx.Done():
			ticker.Stop()
			return ctx.Err()
		}
	}
}
