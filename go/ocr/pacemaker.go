package ocr

import (
	"context"
	"time"
)

type pacemaker struct {
  // TODO these are also part of the state but they are not added in the paper.
	i int // peer identifier
  n int // number of peers in total
  f int // number of allowed faulty peers

	e int // what the current peer thinks the current epoch is.
	l int // what the current peer thinks the leader of the current epoch is.

	ne int // what the current peer thinks the next epoch should be. Highest epoch that pi has initialised or sent a NEWEPOCH for.
  newEpoch map[int]int // mapping of the other peer ids and the NEWEPOCH ids from them.

	deltaProgressSec int // timeout to observe the a report from the leader.
	deltaResendSec int // interval to rebroadcast NEWEPOCH.
}

func newPacemaker(i, n, deltaProgressSec, deltaResendSec int) *pacemaker {
	return &peer {
    i: i,
    n: n,
    f: n/3,
    e: 0,
    l: 0,
    ne: 0,
    newEpoch: make(map[int]int),
    deltaProgressSec: deltaProgressSec,
    deltaResendSec: deltaResendSec,
	}
}

func (p *pacemaker) run(ctx context.Context, network Network) error {
  // TODO initialize instance (e, l) of report generation
  p.timerProgress = time.NewTimer(p.deltaProgressSec * time.Second)
  p.timerResend = time.NewTimer(p.deltaResendSec * time.Second)

  for {
    p.checkState()

    select {
      case raw := <-network.Read():
        switch message := raw.(type) {
        case MessageProgress:
          // the current leader is progressing with the report generation protocol
          p.restartProgressTimer()
        case MessageNewEpoch:
          p.newEpoch[message.Pj] = max(p.ePrime, message.EPrime)
        default:
        }
      case <-p.timerResend.C:
        // resend NEWEPOCH message every ∆ resend seconds, in case network drops it
        p.sendNewEpoch(p.ne, network)
        // Q: do we restart resend?
      case <-p.timerProgress.C:
        // leader is too slow, or tenure is over
        if !p.timerProgress.Stop() {
          <-p.timerProgress.C
        }
        p.sendNewEpoch(max(p.e+1, p.ne), network)
      case <- ctx.Done():
        // TODO how do we cleanup?
      default:
    }
  }
}

func (p *pacemaker) checkState() {
  // NEWEPOCH amplification rule
  p.amplificationRule()
  p.agreementRule()
}

func (p *pacemaker) amplificationRule() {
  countPeersWithLargerNewEpochs := 0
  for pj, ne := range p.newEpoch {
    if ne > p.ne {
      countPeersWithLargerNewEpochs += 1
    }
  }
  if countPeersWithLargerNewEpochs > p.f {
    // Node progresses to the next epoch if at least f other peers report a ne larger the current ne.
    // Q: Is it possible that two subsets of peers are working in separate epochs?
    eBar, found := p.findLargestNextEpoch(p.f)
    // Q: What happens if there is no eBar?
    p.sendNewEpoch(max(p.ne, eBar))
  }
}

func (p *pacemaker) findLargestNextEpoch(threshold int) (int, bool) {
  counts := make(map[int]int)
  for _, ne := range p.newEpoch {
    if _, exists := counts[ne]; !exists {
      counts[ne] = 0
    }
    counts[ne] += 1
  }
  // Q: What happens if I have two larger next epochs in here?
  for ne, count := range counts {
    if ne > p.ne && count > threshold { // TODO in the paper this is count >= pf - p.7
      return ne, true
    }
  }
  return 0, false
}

func (p *pacemaker)  agreementRule() {
  eBar, found := p.findLargestNextEpoch(p.f * 2)
  // Q: what happens if I can't find any eBar
  // TODO abort instance (e, l) of report generation
  p.e = eBar
  p.l = leader(p.e)
  p.ne = max(p.ne, p.e)
  // TODO initialize instance (e, `) of report generation
  p.restartProgressTimer()
  if p.i == p.l {
    // TODO invoke event startepoch(e, l) see report generation protocol
  }
}

// Helpers to restart timers:

func (p *pacemaker) restartProgressTimer() {
  if !p.timerProgress.Stop() {
    <-p.timerProgress.C
  }
  p.timerProgress.Reset(p.deltaProgressSec * time.Second)
}

func (p *pacemaker) restartResendTimer() {
  if !p.timerResend.Stop() {
    <-p.timerResend.C
  }
  p.timerResend.Reset(p.deltaResendSec * time.Second)
}

// TODO this utility does more than sendNewEpoch! It should be renamed.
func (p *pacemaker) sendNewEpoch(ePrime, network *network Network) error {
  network.Broadcast(newMessageNewEpoch(ePrime, p.i), p.i)
  p.ne = ePrime
  p.restartResendTimer()
}
