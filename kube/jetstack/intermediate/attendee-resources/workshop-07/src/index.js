"use strict";
const http = require('http')
const os = require('os')

let counter = 0
const server = http.createServer((req, res) => {
  console.log('request ' + counter)
  const data = {
    env: process.env.HELLO,
    argv: process.argv,
    hostname: os.hostname()
  }
  res.setHeader('content-type', 'application/json')
  res.end(JSON.stringify(data, null, 4))
})

server.listen(80)