package types

import (
	"context"
	"net"
	"time"
)

// Reader reads a log file line by line.
type ReadCloser interface {
	// Read returns a line from the log as a raw byte slice.
	// Implementation should make sure the returned byte slice is not reused!
	Read(ctx context.Context) ([]byte, error)
	Close() error
}

type Line struct {
	Timestamp   time.Time         `json:"timestamp"`
	Level       LogLevel          `json:"level"`
	RemoteIP    net.IP            `json:"remote-ip"`
	RemoteAddrs []string          `json:"remote-addrs"`
	Msg         string            `json:"msg"`
	Tags        map[string]string `json:"tags"`
}

type LogLevel int // Parse using https://pkg.go.dev/encoding/json/v2#UnmarshalerFrom

const (
	Fatal LogLevel = iota
	Error
	Warn
	Info
	Debug
)

type Parser interface {
	Parse([]byte) (Line, error)
}

type Enricher interface {
	Enrich(context.Context, *Line) error
}

type FilterFactory interface {
	New(query string) (Filter, error)
}

type Filter interface {
	Match(Line) bool
}

type Writer interface {
	Write(context.Context, []byte) error
}
