package main

// See: http://www.minaandrawos.com/2016/05/14/udp-vs-tcp-in-golang/

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net"

	"github.com/golang/protobuf/proto"
	"github.com/learnscalability/gossip/pb"
)


// Peer is the peer running this process.
type peer struct {
	id string
	bind string
	commands chan interface{}
	view      View
	udpListener  net.PacketConn
	cmdServer *CmdServer
}

func newPeer(config *peerConfig) (*peer) {
	var (
		err    error
		peer   Peer
	)
	peer.id = config.id
	peer.bind = config.bind
	peer.cmdServer, peer.commands = NewCmdServer(config.CmdBind, peer.commands)
	peer.view = NewView(config.Peers)
	return &peer
}

func (p *peer) start() error {
	var (
		err      error
		listener net.PacketConn
	)
	// Setting up UDP listener
	listener, err = net.ListenPacket("udp", p.bind)
	if err != nil {
		return fmt.Errorf("Unable to bind to udp address %s with error: %+v", p.bind, err)
	} else {
		log.Printf("UDP peer started on %s and accepting connections on %v", p.bind, listener.LocalAddr())
	}
	p.listener = listener
	go p.runner()
	go p.udpHandler()
	// start http command server.
	go p.cmdServer.Run()
	return nil
}

// should be run as a goroutine.
func (p *peer) runner() {
	var (
		unsafe interface{}
	)
	for {
		select {
		case unsafe, ok = <- p.commands:
			if !ok {
				return
			}
			select command := unsafe.(type) {
			case *updatePeerCommand:
				err = p.sendToPeer(command)
			case *updateViewCommand:
				err = p.sendToAll(command)
			case *updateRandomCommand:
				err = p.sendToRandom(command)
			case *joinType:
				err = p.joinCluster(command)
			default:
				err = fmt.Errorf("unknown command type: %T", unsafe)
			}
			if err != nil {
				log.Println(err)
			}
		}
	}
}

func (p *peer) sendToPeer(c *updatePeerCommand) error {
}

// udpHandler read datagrams that are comming through the pipes.
// Should be run as a goroutine.
func (p *peer) udpHandler() {
	var (
		n      int
		caddr  net.Addr
		err    error
		buf    = make([]byte, 10*1024) // 10KB
		update pb.Update
		exists bool
		pid string
	)
	for {
		n, caddr, err = p.listener.ReadFrom(buf)
		if err != nil {
			log.Fatalf("Failed to read datagram: %T %+v", err, err)
		}
		err = proto.Unmarshal(buf[:n], &update)
		if err != nil {
			log.Fatalf("Unable to unmarshal update data: %+v", err)
		}
		log.Printf("Received data `%s` from %s\n", update.Payload, caddr)
		if update.Type == pb.Update_JOIN {
			log.Println("Adding join peer to the current peer view")
			exists = p.view.AddPeer(PeerConfig{
				Pid: update.JoinPayload.Pid,
				Bind: update.JoinPayload.Bind,
			})
			if exists == false {
				log.Println("Forwarding join request")
				for pid = range p.view {
					err = p.Send(pid, string(buf))
					if err != nil {
						log.Printf("Failed to send payload `%s` to peer id `%s` with error: %+v", buf, pid, err)
					}
				}
			}
		}
	}
}

func (p *Peer) Send(pid string, content string) error {
	var (
		buf    []byte
		update pb.Update
		err    error
		pc     PeerConfig
		ok     bool
		conn   net.Conn
	)
	update = pb.Update{
		Payload: []byte(content),
	}
	buf, err = proto.Marshal(&update)
	if err != nil {
		return fmt.Errorf("Failed to marshall update %+s with error: %+v", update, err)
	}
	if pc, ok = p.view[pid]; !ok {
		return fmt.Errorf("Could not find remote peer with pid %s", pid)
	}
	conn, err = net.Dial("udp", pc.Bind)
	if err != nil {
		return fmt.Errorf("Failed to contact remote peer %+v with error: %+v", pc, err)
	}
	defer conn.Close()
	_, err = conn.Write(buf)
	if err != nil {
		return fmt.Errorf("Failed to publish update %+s with error: %+v", content, err)
	}
	log.Printf("Published update %+v to remote peer %+s", pid, pc)
	return nil
}

func (p *Peer) SendJoin(pid, bind string) error {
	var (
		update pb.Update
		buf []byte
		err error
		conn   net.Conn
	)
	update = pb.Update{
		Type: pb.Update_JOIN,
		JoinPayload: &pb.Update_Join{
			Pid: p.config.Pid,
			Bind: p.config.Bind,
		},
	}
	buf, err = proto.Marshal(&update)
	if err != nil {
		return fmt.Errorf("Failed to marshall join update %+s with error: %+v", update, err)
	}
	conn, err = net.Dial("udp", bind)
	if err != nil {
		return fmt.Errorf("Failed to contact remote peer %s with error: %+v", pid, err)
	}
	defer conn.Close()
	_, err = conn.Write(buf)
	if err != nil {
		return fmt.Errorf("Failed to publish update %+s with error: %+v", buf, err)
	}
	log.Printf("Published update %+v to remote peer %s", update, pid)
	return nil
}

// Join works by exchanging the view with the contacted server, while leaving
// the contacted server to tell all other peers in it's view that the new node joined.
func (p *Peer) Join() {
}

// Close closes both the UDP listener and the HTTP command server.
func (p *Peer) stop() {
	p.listener.Close()
	p.cmdServer.Close()
}
