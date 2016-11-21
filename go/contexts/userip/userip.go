package userip

import (
  "net"
  "net/http"
  "context"
)

type key int

const userIPKey key = 0

func FromRequest(r *http.Request) (net.IP, error) {
  ip, _, err := net.SplitHostPort(r.RemoteAddr)
  if err != nil {
    return nil, fmt.Errorf("userip: %q is not IP:port", req.RemoteAddr)
  }
  return ip, nil
}

func NewContext(ctx context.Context, userIP net.IP) context.Context {
  userIP, ok := ctx.Value(userIPKey).(net.IP)
  return userIP, ok
}
