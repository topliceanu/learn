# Pusher Clone

## Runing
```
bundle install
bundle exec foreman start
curl -vv -XPOST http://192.168.33.11:8080/events/test -H 'Content-type: application/json' -d '{"works": 1}'
```

## TODO
- [x] introduce `foreman` as a proc manager
- [x] use event machine in the api code as well
- [x] use em-hiredis to publish from the api code to redis
- [x] extend client lib: allow full pub-sub interface, ie. publish client-side.
- [ ] introduce unsubscribe to a specific channel
- [x] introduce webhooks, so clients can receive updates, using beanstalkd workers
- [ ] shard redis by channel
- [ ] add multiple api servers by introducing a load ballancer in front.
- [ ] _refactor_ introduce the concept of a channel as a container class.
- [ ] make the processes more resilient by handling errors
- [ ] add logging to the processes
- [ ] introduce presence channels (Check: how are they implemented into Pusher)
