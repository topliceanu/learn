package main

import (
	"fmt"
	"log"
	"net/http"
	"regexp"
)

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handler(w http.ResponseWriter, r *http.Request) {
	re := regexp.MustCompile("^(.+)@golang.org$")
	path := r.URL.Path[1:]
	match := re.FindAllStringSubmatch(path, -1)
	if match != nil {
		fmt.Fprintf(w, "Hello, gopher %s\n", match[1])
		return
	}
	fmt.Fprintf(w, "Hello, dear %s\n", path)
}
