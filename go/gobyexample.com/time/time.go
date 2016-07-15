package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	bday := time.Date(1986, 9, 8, 12, 25, 10, 111111, time.UTC)
	fmt.Printf("%s %s is after: %t is before: %t\n", now, bday, now.After(bday), bday.Before(now))

	diff := now.Sub(bday)
	fmt.Printf("Hours since I've been alive: %f\n", diff.Hours())

	secs := now.Unix()
	nanos := now.UnixNano()
	fmt.Printf("Unix timestamps: %d seconds %d nanoseconds\n", secs, nanos)

	fmt.Printf("In format %s the current time is %s\n", time.RFC3339, now.Format(time.RFC3339))

	format := "3 04 PM"
	t, _ := time.Parse(format, "8 41 PM")
	fmt.Printf("Parsed time is %s\n", t)
}
