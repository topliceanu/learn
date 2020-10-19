package ocr

import (
  "context"
  "time"
)

type reporter struct {
  rf int // current round number within the epoch
  sentEcho bool // indicates if FINAL - ECHO message has been sent for this round
  sentReport bool // indicates if REPORT message has been sent for this round
  completeRound bool // denotes if current round is finished
  final map[int]bool // mapping of received FINAL-ECHO messages, by default they are all false.

  pl int // current leader ID
  rMax int // the maximum round allowed for the current epoch
  i int // ID of the current peer.
  e int // current epoch number.
}

func newReporter(pl, i, e int) *reporter {
  return &reporter{
    rf: 0,
    sentEcho: false,
    sentReport: false,
    completeRound: false,
    final: make(map[int]bool),

    // TODO these are not defined in the state of the protocol!
    pl: pl,
    rMax: 0, // TODO what is the value of RMax?
    i: i,
    e: e,
  }
}

func (r *reporter) run(ctx context.Context, network Network) {
  for {
    select {
    case raw := <-network.Read()
      switch message := raw.(type) {
      case MessageObserveRequest:
        // TODO what happens if the message is not from the leader?
        if message.Pj == r.pl && r.rf < message.RPrime && message.RPrime <= r.rMax {
          // oracle moves to next round as follower
          r.rf = message.RPrime
          // pl has exhausted its maximal number of rounds
          if r.rf > r.rMax {
            // TODO invoke event changeleader
            // Q: This is not defined anywhere?!
            return // TODO oracle halts this report generation instance. How do you cleanup?
          }
          r.sentEcho = false
          r.sentReport = false
          r.completeRound = false
          r.final = make(map[int]bool) // reset
          value := r.readValue()
          // TODO r.e is not defined anywhere
          // TODO you sign r, which is actually called rf!!
          // Q: What about the timestamp? Are we vulnerable to timing attacks?
          signature := sign(r.i, "OBSERVE", r.e, r.rf, value)
          // Q: What about sending the peer id for this observation?
          network.Send(newMessageObserve(r.rf, value, signature), r.pl)
        }
      case MessageReportRequest:
        if message.Pj == r.pl && message.RPrime == r.rf && !r.sentReport && !r.completeRound {
          // TODO verify that R is sorted with entries from 2f + 1 distinct oracles
          // AND verify that all signatures in R are valid
          // Q: what is the structure of R?
          if p.shouldReport(message.R)
        }
      case MessageFinal:
      case MessageFinalEcho:
      }
    case ctx.Done():
      return
    }
  }
}

func (r *reporter) readvalue() int {
}






















type reporter struct {
  l int // id of the current epoch leader
  e int // current epoch number
  ne int // highest epoch that thic peer initialised

  r int // current round number withing the epoch
  rmax int // maximum number of rounds a leader is allowed to do continuously, to prevent DDOS.
  // only for the leader
  observe map[int]int // received Observed messages
  report map[int]int // received Report messages
  n int // total  number of peers
  f int // number of peers allowed to be down
  deltaRoundSec int // number of seconds a round is allowed to remain.
  deltaObserveSec int // time to wait for observations.
}

func New() *reporter {
  return &reporter{
    l: 0,
    e: 0,
  }
}

func (rep *reporter) run(context.Context) error {
  var (
    timerRound *time.Timer
    timerObserve *time.Timer
    sentEcho bool = false
    roundComplete bool = false
    network = establishConnection()
  )
  for {
    select {
    case untypedMessage, networkClosed <-network.Read():
      if networkClosed {
        return network.Err()
      }
      switch message := untypedMessage.(type) {
      case MessageStartEpoch:
        rep.r += 1
        rep.observe = make(map[int]int) // clean the observations map
        network.Broadcast(newMessageObserveReq(r))
        timerRound = time.NewTimer(deltaRoundSec)
      case MessageObserveReq:
        if message.sender = rep.l && message.rPrime > rep.r {
          rep.r = message.rPrime
          sentEcho, RoundCompleted = false, false
          sig := sign(rep.e, rep.l, rep.r, message.v)
          network.Write(newMessageObserve(rep.r, message.v, sig), l) // writes to the leader node.
        }
      }
    case <- timerRound.C:
      rep.r += 1
      rep.observe = make(map[int]int) // clean the observations map
      network.Broadcast(newMessageObserveReq(r))
      timerRound = time.NewTimer(deltaRoundSec)
    }
  }
}


func sign() []byte {
}
