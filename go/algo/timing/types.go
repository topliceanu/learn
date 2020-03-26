package main

import (
	"time"
)

type Action func() {}

type Timer interface {
	Start(duration time.Duration, action Action) (timerID int)
	Stop(timerID int)
	Process()
}

