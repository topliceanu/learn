package main

import (
	"fmt"
	"log"
	"net/http"
	_ "net/http/pprof"
	"strings"
)

func main() {
	http.HandleFunc("/", handler)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Failed to start the server on :8080 with error: %s", err)
	}
}

func handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/plain")
	var path = r.URL.Path[1:]
	if strings.HasSuffix(path, "@golang.org") {
		name := strings.TrimSuffix(path, "@golang.org")
		fmt.Fprintf(w, "Hello gopher %s\n", name)
		return
	}
	fmt.Fprintf(w, "Hello dear %s\n", path)
}
