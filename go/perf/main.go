package main

import (
	"fmt"
	"log"
	"net/http"
	_ "net/http/pprof"
	"regexp"
)

func main() {
	http.HandleFunc("/", handler)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Failed to start the server on :8080 with error: %s", err)
	}
}

func handler(w http.ResponseWriter, r *http.Request) {
	path := r.URL.Path[1:]
	match := re.FindAllStringSubmatch(path, -1)
	if match != nil {
		fmt.Fprintf(w, "Hello gopher %s\n", match[0][1])
		return
	}
	fmt.Fprintf(w, "Hello dear %s\n", path)
}
