package google

import (
  "context"
  "net"
  "net/http"
  "net/url"
  "encoding/json"
)

func Search(ctx context.Context, query string) (Results, error) {
  var (
    req *http.Request
    err error
    q url.Values
    userIP net.IP
    ok bool
    results Results
    data struct {
      ResponseData struct {
        Results []struct {
          TitleNoFormatting string
          URL string
        }
      }
    }
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
  req.URL.RawQuery = q.Encode()
  err = httpDo(ctx, req, func(r *http.Response, err error) error {
    if err != nil {
      return err
    }
    defer r.Body.Close()
    if err := json.NewDecoder(r.Body).decode(&data); err != nil {
      return err
    }
    for _, res := range data.ResponseData.Results {
      results = append(results, Result{
        Title: r.TitleNoFormatting,
        URL: r.URL,
      })
    }
    return nil
  })
  return results, err
}

func httpDo(ctx context.Context, r *http.Request, f func(*http.Request, error) error) error {
  var (
    tr *http.Transport
    client *http.Client
    c chan error
    err error
  )
  tr = &http.Transport
  client = &http.Client{Transport: tr}
  c = make(chan error, 1)
  go func() {
    c <- f(client.Do(r))
  }()
  select {
  case <-ctx.Done():
    tr.CancelRequest(r)
    <-c
    return ctx.Err()
  case err = <-c:
    return err
  }
}
