package main

import (
	"fmt"
	"net"
	"time"
)

func worker(name int, jobs chan string, results chan<- string) {
	for j := range jobs {
		results<- fmt.Sprintf("Worker %d received job %s", name, j)
	}
}

func pool(jobs chan string, numWorkers int) {
	results := make(chan string)

	for i := 1; i <= numWorkers; i += 1 {
		go worker(i, jobs, results)
	}

	for r := range results {
		fmt.Println(r)
	}
}

func handler(c net.Conn, jobs chan<- string) {
	jobs<- c.RemoteAddr().String()
	c.Write([]byte("OK!"))
	c.Close()
}

func server(l net.Listener, jobs chan<- string) {
	for {
		c, err := l.Accept()
		if err != nil {
			continue
		}
		go handler(c, jobs)
	}
}

func main() {
	l, err := net.Listen("tcp", "0.0.0.0:5000")
	if err != nil {
		panic(err)
	}

	numWorkers := 10
	jobs := make(chan string)

	go pool(jobs, numWorkers)
	go server(l, jobs)

	time.Sleep(10 * time.Second)
}
