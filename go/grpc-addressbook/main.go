package main

import (
  "fmt"

  "github.com/golang/protobuf/proto"
)

func main() {
  p := &Person{
    Name: "Alex",
    Id: 12,
    Email: "alexandru@pusher.com",
    Phones: []*Person_PhoneNumber{
      &Person_PhoneNumber{
        Number: "0745657924",
        Type: Person_MOBILE,
      },
    },
  }
  blob, err := proto.Marshal(p)
  pr := &Person{}
  err = proto.Unmarshal(blob, pr)
  fmt.Println(">>>>>>>", p, blob, err, pr)
}
