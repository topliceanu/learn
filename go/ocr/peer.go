package ocr

import (
	"context"
	"time"
)

type peer struct {
	i int // peer identifier
	e int // what the current peer thinks the current epoch is
	ne int // what the current peer thinks the next epoch should be
	l int // what the current peer thinks the leader of the current epoch is
	deltaResendSec int // interval to rebroadcast NEWEPOCH
	deltaProgressSec int // timeout to observe the final report

	peers map[int]*otherPeer // mapping of the other peer ids and their current epoch
}

type otherPeer struct {
	i int
	addr string
	e int // what the current peer thinks this other peers epoch is
}

func newPeer(i, e, l) *peer {
	return &peer {
		i, e, l
	}
}

// run should be executed as a goroutine
func (p *peer) run(ctx context.Context) error {
	network, err := p.startNetworkListener()
	if err != nil {
		return err
	}
	if err := network.Write(startEpochMessage(e, l)); err != nil {
		return err
	}
	timerProgress := time.NewTicker(p.deltaProgressSec * time.Second)
	timerResend := time.NewTicker(p.deltaResendSec * time.Second)

	nextEpochsByPeer := make(map[int]int)

	for {
		select {
		case message := <-network.Read():
			if message.typ == MessageTypeProgress {
				timerProgress.Reset(p.deltaProgressSec * time.Second)
				continue
			} else if message.typ == MessageTypeTimeout {
			} else if message.typ == MessageTypeChangeLeader {
			} else if message.typ == MessageTypeSendEpoch {
			}
		case <-timerProgress.C:
			// TODO: has there been a new report from the leader. Otherwise remove leader by requesting a new epoch.
		case <-timerResend.C:
			// TODO: how often should the peer resend timers.
		case <-ctx.Done():
			timerProgress.Stop()
			timerResend.Stop()
			if err := network.Close(); err != nil {
				return err
			}
		}
	}
}

func sendNewEpoch() error {
}

func messageStartEpoch(e, l int) []byte {
	// TODO
}

func messagelNewEpoch() []byte {
	// TODO
}

func messageComplaint() []byte {
	// TODO
}
