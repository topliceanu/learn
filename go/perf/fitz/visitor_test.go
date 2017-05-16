package main

import (
  "bufio"
  "io/ioutil"
  "net/http"
  "net/http/httptest"
  "strings"
  "sync"
  "testing"
)

func TestHandlerHi(t *testing.T) {
  rw := httptest.NewRecorder()
  handleHi(rw, req(t, "GET / HTTP/1.0\r\n\r\n"))
  if !strings.Contains(rw.Body.String(), "visitor number") {
    t.Errorf("Unexpected output: %s", rw.Body)
  }
}

func req(t testing.TB, v string) *http.Request {
  req, err := http.ReadRequest(bufio.NewReader(strings.NewReader(v)))
  if err != nil {
    t.Fatal(err)
  }
  return req
}

func TestHandleHi_TestServer_Parallel(t *testing.T) {
  ts := httptest.NewServer(http.HandlerFunc(handleHi))
  defer ts.Close()
  var wg sync.WaitGroup
  for i := 0; i < 20; i++ {
    wg.Add(1)
    go func() {
      defer wg.Done()
      res, err := http.Get(ts.URL)
      if err != nil {
        t.Error(err)
        return
      }
      if g, w := res.Header.Get("Content-Type"), "text/html; charset=utf-8"; g != w {
        t.Errorf("Content-Type = %q; want %q", g, w)
      }
      slurp, err := ioutil.ReadAll(res.Body)
      defer res.Body.Close()
      if err != nil {
        t.Error(err)
        return
      }
      t.Logf("Got: %s", slurp)
    }()
  }
  wg.Wait()
}

func BenchmarkHandlerHi(b *testing.B) {
  b.ReportAllocs()
  r := req(b, "GET / HTTP/1.0\r\n\r\n")
  rw := httptest.NewRecorder()
  for i := 0; i < b.N; i ++ {
    handleHi(rw, r)
    reset(rw)
  }
}

func BenchmarkHiParallel(b *testing.B) {
  r := req(b, "GET / HTTP/1.0\r\n\r\n")
  b.RunParallel(func(pb *testing.PB) {
    rw := httptest.NewRecorder()
    for pb.Next() {
      handleHi(rw, r)
      reset(rw)
    }
  })
}


func reset(rw *httptest.ResponseRecorder) {
  m := rw.HeaderMap
  for k := range m {
    delete(m, k)
  }
  body := rw.Body
  body.Reset()
  *rw = httptest.ResponseRecorder{
    Body:      body,
    HeaderMap: m,
  }
}
