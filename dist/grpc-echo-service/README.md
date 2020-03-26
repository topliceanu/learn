# grpc-echo-service

A simple RPC example implemented using gRPC

## Instalation

Setup [learnscalability/vm](https://github.com/learnscalability/vm)

Install project dependencies
```sh
$ cd ~/go/src/github.com/learnscalability/grpc-echo-service
$ glide install
```

## How to run

Make sure the protobuf generated `pb` package is up-to-date:
```sh
$ ./script/proto
```

Running the server
```sh
$ go run ./cmd/server/main.go -bind="0.0.0.0:3000"
```

Running the client, both send and subscribe
```sh
$ go run ./cmd/client/main.go -message="hello there" -method="subscribe" -server="0.0.0.0:3000"
```

Running the godoc tool
```sh
godoc -http=:8080
```
then navigate to `192.168.33.10:8080/pkg/github.com/learnscalability/grpc-echo-service` for godoc.org style docs.
