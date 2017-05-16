package main

import (
  "bytes"
  "log"
  "net/http"
  "regexp"
  "sync"
  "strconv"
)

var visitors struct {
  sync.Mutex
  m int
}

var colorRx = regexp.MustCompile(`^\w*$`)

var bufPool = sync.Pool{
  New: func() interface{} {
    return new(bytes.Buffer)
  },
}

func handleHi(w http.ResponseWriter, r *http.Request) {
  if !colorRx.MatchString(r.FormValue("color")) {
    http.Error(w, "Optional color is invalid", http.StatusBadRequest)
    return
  }
  visitors.Lock()
  visitors.m++
  visitorsNum := visitors.m
  visitors.Unlock()

  //fmt.Fprintf(w, "<h1 style='color: %s'>Welcome!</h1>You are visitor number %v!", r.FormValue("color"), visitorsNum)
  // This is equivalent to the above!
  buf := bufPool.Get().(*bytes.Buffer)
  defer bufPool.Put(buf)
  buf.Reset()
  buf.WriteString("<h1 style='color: ")
  buf.WriteString(r.FormValue("color"))
  buf.WriteString(">Welcome!</h1>You are visitor number ")
  b := strconv.AppendInt(buf.Bytes(), int64(visitorsNum), 10)
  b = append(b, '!')
  w.Write(b)
}

func main() {
  log.Printf("Starting on port 8080")
  http.HandleFunc("/hi", handleHi)
  log.Fatal(http.ListenAndServe("0.0.0.0:8080", nil))
}
