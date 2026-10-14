package main

import (
	"context"
	"os/signal"
	"sync"
	"syscall"

	"github.com/topliceanu/log/pkg/types"
)

// TODO:
// - [ ] a config package.
// - [x] a reader abstraction. Start by reading from one file, but then scale that to support multiple files.
// - [x] investigate reading the file
// - [x] hookup a context throughout the project.
// - [ ] parser for log lines: JSON, CSV, etc. https://pkg.go.dev/encoding/csv
// - [ ] think about error handling.
// - [x] build a struct for each log line.
// - [ ] handle signals from the operating system.
// - [ ] support multiple types of readers
// - [ ] add structured logging throughout the project
// ! Fail gracefully – don’t crash on bad input.
// - [ ] Use a thread safe LRU cache like https://pkg.go.dev/github.com/hashicorp/golang-lru/v2

// Questions for the interviewer:
// - What format are the logs in?
// - What happens if a log line is malformed - do we print and continue OR crash?
// - How many files? What size is each file? Are the files on disk? or am I reading them from a network connection?
// - Will a log line be larger than 1MB?
// - Does the output logs need to be in the same order as the input?
// - What type of output do you want to get? Stdout, file, stream

// DM on whatsapp +972527403332

// Things to optimise:
// - what's the right size of the buffer
// - how many workers?

// Things to communicate to the interviewer
// - My idea is to isolate the concurrency into a single file so the interractions are well visible.
// - Excalidraw: https://excalidraw.com/#json=1go1Sx9bzFK0FHjsjCvy8,VTAOxneZ8H12s2yeD4ijeA

func main() {
	var cfg types.Config
	var reader types.ReadCloser
	var parser types.Parser
	var enricher types.Enricher
	var filterFactory types.FilterFactory
	var writer types.Writer
	filter, err := filterFactory.New(cfg.Query)
	if err != nil {
		panic(err)
	}
	var lines = make(chan []byte, cfg.Reader.LineBufferSize)
	var output = make(chan []byte)
	var wg *sync.WaitGroup
	globalCtx, globalCancel := context.WithCancelCause(context.Background())
	defer globalCancel(nil)

	wg.Go(func() {
		for {
			line, err := reader.Read(globalCtx)
			if err != nil {
				globalCancel(err)
				return
			}
			select {
			case lines <- line:
			case <-globalCtx.Done():
				return
			}
		}
	})
	for range cfg.WorkerPool.NumWorkers {
		wg.Go(func() {
			for {
				select {
				case line := <-lines:
					log, err := parser.Parse(line)
					if err != nil {
						globalCancel(err)
						return
					}
					err = enricher.Enrich(globalCtx, &log)
					if err != nil {
						globalCancel(err)
						return
					}
					if !filter.Match(log) {
						continue
					}
					select {
					case output <- line:
					case <-globalCtx.Done():
						return
					}
				case <-globalCtx.Done():
					return
				}
			}
		})
	}
	wg.Go(func() {
		for {
			select {
			case line := <-output:
				if err := writer.Write(globalCtx, line); err != nil {
					globalCancel(err)
					return
				}
			case <-globalCtx.Done():
				return
			}
		}
	})
	wg.Go(func() {
		localCtx, localCancel := signal.NotifyContext(globalCtx, syscall.SIGINT, syscall.SIGTERM)
		defer localCancel()
		<-localCtx.Done()
	})
	wg.Wait()
}

/*
import (
	"bufio"
	"fmt"
	"net"
	"os"
	"regexp"
	"time"
)

type LogLine struct {
	Timestamp   time.Time
	RemoteIP    net.IP
	RemoteAddrs []string
	Msg         string
	Tags        map[string]string
}

func main() {
	f, err := os.Open("log.txt")
	if err != nil {
		panic(err)
	}
	query := Query{}
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)
	scanner.Buffer(make([]byte, 256*1024), 256*1024)
	for scanner.Scan() {
		line := scanner.Text()
		logLine, err := parse(line)
		if err != nil {
			panic(err)
		}
		if matchQuery(query, logLine) {
			fmt.Println(line)
		}
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}
}

func parse(line string) (LogLine, error) {
	return LogLine{}, nil
}

type Query struct {
	Timestamp   TimestampQuery
	RemoteIP    StringQuery
	RemoteAddrs []StringQuery
	Msg         StringQuery
	Tags        map[string]StringQuery
}

type TimestampQuery struct {
	Gt *time.Time
	Lt *time.Time
}

type StringQuery struct {
	Eq     *net.IP
	Match  *regexp.Regexp
	Prefix *string
	Suffix *string
}

// Eq, Gt, Lt, Interval, Contains,

func matchQuery(query Query, line LogLine) bool {
	return false
}
*/
