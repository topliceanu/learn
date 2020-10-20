package ocr

import (
  "context"
  "time"
)

// TODO: report generation follower
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
  f int // number of allowed broken nodes
}

func newReporter(pl, i, e, f int) *reporter {
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
    f: f,
  }
}

func (r *reporter) run(ctx context.Context, network Network) {
  for {
    r.checkStatus()

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
          if len(message.R.Measurements) >= 2 * ref.f + 1 && message.IsValidSignature() {
            if r.shouldReport(message.R) {
              RPrime = message.R.Compressed()
              signature = sign("REPORT", r.e, r.rf, RPrime)
              r.sentReport = true
              network.Send(newMessageReport(r.rf, RPrime, signature), r.pl)
            } else {
              r.completeRound()
            }
          }
        }
        // Q: who sends the MessageFinal part?!
      case MessageFinal:
        if message.Pj == r.pl && (message.RPrime == r.rf || !r.sentEcho) {
          if r.verifyAttestedReport(message.O) {
            r.sentEcho = true
            network.Broadcast(newMessageFinalEcho(r.i, r.rf, message.O))
          }
        }
      case MessageFinalEcho:
        if message.RPrime = r.rf && !r.completeRound {
          if r.verifyAttestedReport(message.O) {
            r.final[message.Pj] = message.O
            if !r.sentEcho {
              r.sentEcho = true
              network.Broadcast(newMessageFinalEcho(r.i, r.rf, message.O))
            }
          }
        }
      }
    case ctx.Done():
      return
    }
  }
}

func (r *reporter) checkState() {
  // TODO invoke transmit(O) // see transmission protocol
  r.completeRound()
}

func (r *reporter) shouldReport(r Report) {
}

func (r *reporter) completeRound() {
  // (1) when no transmit is needed and (2) when transmit has been invoked
  r.completeRound = true

  // see pacemaker protocol in Alg. 1; indicates leader is performing correctly
  // TODO invoke event progress

  // the round ends and p i waits until pl initiates the next round
  return
}

func (r *reporter) verifyAttestedReport(rep Report) {
  for _, measurement := range rep.Measurements {
    if !measurement.Verify() {
      return False
    }
  }
  return True
}
