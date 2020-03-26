package main

import (
	"encoding/json"
	"flag"
	"log"
	"os"
	"os/signal"
)

type peerConfig struct {
	Id string `json:"id"`
	Bind string `json:"bind"`
	CmdBind string `json:"cmdbind,omitempty"`
	Peers []peerConfig `json:"peers,omitempty"`
}

func main() {
	var (
		err  error
		sigs = make(chan os.Signal)
		sig  os.Signal
		fp   *os.File
		pc *peerConfig
		peer *Peer
	)
	flag.Parse()
	if flag.NArg() != 1 {
		log.Fatal("Expected first argument to be a config file")
	}
	fp, err = os.Open(flag.Arg(0))
	if err != nil {
		log.Fatalf("Failed to open file `%d` with error: %+v", flag.Arg(0), err)
	}
	err = json.NewDecoder(fp).Decode(pc)
	if err != nil {
		log.Fatalf("Failed to parse peer config with error: %+v", err)
	}
	peer, err = NewPeer(pc)
	err = peer.start()
	if err != nil {
		log.Fatal(err)
	}
	defer peer.stop()
	// Setup termination handlers.
	signal.Notify(sigs, os.Interrupt, os.Kill)
	sig = <-sigs
	log.Fatalf("Received signal %+v. Terminating", sig)
}
