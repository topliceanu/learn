package main

import (
  "fmt"
  "context"
)

func gen(ctx context.Context) <-chan int {
  ch := make(chan int)
  go func() {
    var n int
    for {
      select {
      case <-ctx.Done():
        return
      case ch <- n:
        n += 1
      }
    }
  }()
  return ch
}

func main() {
  ctx, cancel := context.WithCancel(context.Background())
  defer cancel()
  for n := range gen(ctx) {
    fmt.Println(n)
    if n == 5 {
      cancel()
      break
    }
  }
}
