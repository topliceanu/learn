package types

import (
	"net"
	"regexp"
	"time"
)

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
