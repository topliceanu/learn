package google

import (
  "context"
  "net"
  "net/http"
  "net/url"
)

func Search(ctx context.Context, query string) (Results, error) {
  var (
    req *http.Request
    err error
    q url.Values
    userIP net.IP
    ok bool
  )
  req, err := http.NewRequest("GET", "https://ajax.googleapis.com/ajax/services/search/web?v=1.0", nil)
  if err != nil {
    return nil, err
  }
  q = req.URL.Query()
  q.Set("q", query)
  if userIP, ok = userip.FromContext(ctx); ok {
    q.Set("userip", userIP.String())
  }
}
