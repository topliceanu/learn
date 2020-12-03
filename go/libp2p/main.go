package main

import (
	"context"
	"fmt"
	"os"
	"os/signal"
	"syscall"

	"github.com/libp2p/go-libp2p"
	"github.com/libp2p/go-libp2p-core/host"
	"github.com/libp2p/go-libp2p-core/peer"
	"github.com/libp2p/go-libp2p/p2p/protocol/ping"
	"github.com/multiformats/go-multiaddr"
)

func main() {
	// create a background context (i.e. one that never cancels)
	var (
		ctx    context.Context
		cancel context.CancelFunc
	)
	ctx, cancel = context.WithCancel(context.Background())
	defer cancel()

	// start a libp2p node with default settings
	var err error
	var node host.Host
	node, err = libp2p.New(ctx,
		libp2p.ListenAddrStrings("/ip4/0.0.0.0/tcp/2000"),
		libp2p.Ping(false),
	)
	if err != nil {
		panic(err)
	}

	// print the node's listening addresses
	fmt.Println("Listen addresses:", node.Addrs())

	// configure our own ping protocol
	var pingService *ping.PingService = &ping.PingService{Host: node}
	node.SetStreamHandler(ping.ID, pingService.PingHandler)

	// print the node's PeerInfo in multiaddr format
	peerInfo := peer.AddrInfo{
		ID:    node.ID(),
		Addrs: node.Addrs(),
	}
	var addrs []multiaddr.Multiaddr
	addrs, err = peer.AddrInfoToP2pAddrs(&peerInfo)
	fmt.Println("libp2p node address:", addrs[0])

	// if a remote peer has been passed on the command line, connect to it
	// and send it 5 ping messages, otherwise wait for a signal to stop
	if len(os.Args) > 1 {
		var remoteAddr multiaddr.Multiaddr
		remoteAddr, err = multiaddr.NewMultiaddr(os.Args[1])
		if err != nil {
			panic(err)
		}
		var remoteAddrInfo *peer.AddrInfo
		remoteAddrInfo, err = peer.AddrInfoFromP2pAddr(remoteAddr)
		if err != nil {
			panic(err)
		}
		if err := node.Connect(ctx, *remoteAddrInfo); err != nil {
			panic(err)
		}
		fmt.Println("sending 5 ping messages to", remoteAddr)
		ch := pingService.Ping(ctx, remoteAddrInfo.ID)
		for i := 0; i < 5; i++ {
			res := <-ch
			fmt.Println("pinged!", remoteAddr, "in", res.RTT)
		}
	} else {
		// wait for a SIGINT or SIGTERM signal
		osSigs := make(chan os.Signal, 1)
		signal.Notify(osSigs, syscall.SIGINT, syscall.SIGTERM)
		sig := <-osSigs
		fmt.Printf("Received signal '%s', shutting down...", sig)
	}

	// shut the node down
	if err := node.Close(); err != nil {
		panic(err)
	}
}
