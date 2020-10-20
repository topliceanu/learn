package ocr

type Message interface {
  // TODO maybe serialize
}

type MessageProgress struct {
  // implements Message
}

type MessageNewEpoch struct {
  Pj int // ID of the source peer
  EPrime int // new epoch the source peer communicates
}

func newMessageNewEpoch(ePrime, id int) *MessageNewEpoch {
  return &MessageNewEpoch{
    Pj: id,
    EPrime: ePrime,
  }
}

type MessageObserveReq struct {
  Pj int // ID of the source peer
  RPrime int // Round number
}

func newMessageObserveReq(pj, rPrime int) MessageObserveReq {
  return MessageObserveReq{
    Pj: pj,
    RPrime: rPrime,
  }
}

type MessageObserve struct {
  Pj int // id of the source of the message
  // TODO in the reporting leader algo, Rf is called RPrime.
  Rf int // current round of observation
  Value int // observation value
  Signature string // message signature
}

func newMessageObserve(rf, value, signature) *MessageObserve {
  return &MessageObserve{
    Rf: rf,
    Value: value,
    Signature: signature,
  }
}

type MessageReport struct {
  Pj int // id of the source node of the message
  RPrime int // round number
  R Report // report
  Tau int // Q: what is this tau?
}

type MessageReportRequest struct {
  Pj int // id of the source of the message
  RPrime int // round number
  R Report
}

type Report struct {
  Measurements []Measurement
}

func (r Report) Compressed() []NonSignedMeasurement {
}

type NonSignedMeasurement struct {
  W, K int
}

type Measurement struct {
  W, K int
  Signature []byte
}

type MessageFinal struct {
  Pj int
  RPrime int
  O int
}

type MessageFinalEcho struct {
  Pj int
  RPrime int
  O int
}

func newMessageFinalEcho(id, r, O int) MessageFinalEcho {
  return MessageFinalEcho{
    Pj: id,
    RPrime: r,
    O: O,
  }
}

type Network interface {
  Broadcast(message Message, senderID int)
}
