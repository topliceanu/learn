# Pusher Clone

## HTTP API
- starts on port 8080
- command: `ruby api/server.rb -o 0.0.0.0 -p 8080`

## WS API
- starts on port 9090
- command: `ruby ws/server.rb`

## CLIENT WEBSITE
- starts on port 8000
- command: `cd client; python -m SimpleHTTPServer`

## TEST
- command: `curl -XPOST http://192.168.33.11:8080/events/test -H 'Content-type: application/json' -d '{"works": 1}'`

## TODO
- [ ] support messages comming from clients as well, ie publish client-side.
- [ ] introduce webhooks so clients can receive updates
- [ ] use event machine in the api code as well
- [ ] use em-hiredis to publish from the api code to redis
- [ ] shard redis by channel
- [ ] add multiple api servers by introducing a load ballancer in front.
