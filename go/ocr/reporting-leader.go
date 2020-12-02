package ocr

import (
  "context"
  "time"
)

const (
  PhaseObserve = iota
  PhaseGrace
  PhaseReport
  PhaseFinal
)

type leader struct {
  // TODO in the follower algorithm this is called rf?!
  rl int // current round number within the epoch
  observe map[int]int // received observed messages
  report map[int]int // received report messages
  deltaRoundSec int // interval for a round.
  deltaGraceSec int // grace period interval.
  phase string // either "OBSERVE", "GRACE", "REPORT", "FINAL"

  timerTRound time.Timer
  timerTGrace time.Timer

  // Not in the paper
  i int // id of the node
  e int // epoch number
  f int // number of nodes allowed to be down.
  l int // current leader
}

func newLeader() *leader {
  return &leader{
  }
}

func (l *leader) run(ctx context.Context) {
  // TODO upon event startepoch (e, `) do start-round ()

  for {
    l.checkState()

    select {
    case <- l.timerTRound.C:
      l.startRound()
    case raw <- l.network.Read():
      switch message := raw.(type) {
      case MessageObserve:
        // TODO inconsistency in the paper with the other protocol
        if message.Rf == l.rl && r.i = r.l { // Q: What is this?
          if l.verify("OBSERVE", r.e, r.rl, messave.Value, message.Signature) {
            r.observe[message.Pj] = (message.Value, message.Signature) // TODO implement pairs
          }
        }
      case MessageReport:
        if message.RPrime = l.rl && l.i = l.l && l.phase = PhaseReport {
          // TODO: isn't Tau here in fact sigma?
          if l.verify("REPORT", l.e, l.rl, message.R, message.Tau) {
            l.report[message.Pj] = (message.R, message.Tau) // TODO add a pair here
          }
        }
      }
    case <- l.timerTGrace.C:
      if l.phase == PhaseGrace {
        // TODO assemble report R ← sorted((w, k, σ) for k, (w, σ) in enumerate(observe))
        R := extractReport(l.observe)
        network.Broadcast(newMessageReportReq(l.rl R))
        l.phase = PhaseReport // TODO what is the state machine here?
      }
  }
}

func (l *leader) checkState() {
  // grace period for slow oracles
  if l.phase == PhaseObserve && l.countObservations() == 2 * l.f + 1 {
    l.timerTGrace = time.NewTimer(l.deltaGraceSec * time.Second)
    l.phase = PhaseGrace
  }
  // inialize final stage
  if l.phase = PhaseFinal && len(l.report) > l.f {
    k := 1
    // Collect the attestation of the final report.
    // TODO O ← [e, rl , R, J, T ]
    l.network.Broadcast(newMessageFinal(l.i, l.rl, O))
    l.phase = PhaseFinal
  }
}

func (l *leader) startRound() {
  l.rl = l.rl + 1 // leader protocol moves to next round
  l.observe = make(map[int]int)
  l.report = make(map[int]int)
  l.networking.Broadcast(newMessageObserveReq(l.rl))
  l.timerTRound = time.NewTimer(l.deltaRoundSec * time.Second)
  l.phase = PhaseObserve
}
