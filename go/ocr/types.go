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

type MessageObserveRequest struct {
  Pj int // ID of the source peer
  RPrime int // Round number
}

type MessageObserve struct {
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

type MessageReportRequest struct {
  Pj int // id of the source of the message
  RPrime int // round number
  R Report
}

type Report struct {
  Measurements []Measurement
}

type Measurement struct {
  W int
  K int
  Signature []byte
}

type MessageFinal struct {
}

type MessageFinalEcho struct {
}

type Network interface {
  Broadcast(message Message, senderID int)
}
