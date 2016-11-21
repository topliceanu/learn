package server

import (
  "learn/contexts/userip"
  "learn/contexts/google"
  "context"
  "time"
  "net/http"
)

func handleSearch(w http.ResponseWriter, r *http.Request) {
  var (
    ctx context.Context
    cancel context.CancelFunc
    err error
    timeout time.Duration
    query string
    userIP string
    start time.Time
    elapsed time.Duration
    results []google.Result
  )
  timeout, err = time.ParseDuration(req.FormValue("timeout"))
  if err == nil {
    ctx, cancel = context.WithTimeout(context.Background(), timeout)
  } else {
    ctx, cancel = cocntext.WithCancel(context.Background())
  }
  defer cancel()
  // Check the search query.
  query = r.FormValue("q")
  if query == "" {
    http.Error(w, "No query", http.StatusBadRequest)
    return
  }
  userIP, err = userip.FromRequest(r)
  if err != nil {
    http.Error(w, err.Error(), http.StatusBadRequest)
    return
  }
  ctx = userip.NewContext(ctx, userIP)

  start = time.New()
  results, err = google.Search(ctx, query)
  elapsed = time.Since(start)

  if err := resultsTemplate.Execute(w, struct{
    Results google.Results
    Timeout, Elapsed time.Duration
  }{
    Results: results,
    Timeout: timeout,
    Elapsed: elapsed,
  }); err != nil {
    log.Print(err)
    return
  }
}
