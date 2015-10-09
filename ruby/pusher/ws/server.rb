require 'em-websocket'
require 'em-hiredis'
require 'json'


EM.run {
  puts "WebSockets server started"
  channels = Hash.new([])

  # WebSocket code.
  EM::WebSocket.run(:host => '0.0.0.0', :port => 9090, :debug => true) do |ws|
    ws.onopen { |handshake|
      puts "WebSocket connection open"
    }

    ws.onmessage { |data|
      puts "WebSocket read #{data}"
      msg = JSON.parse(data)

      unless msg["subscribe"].nil?
        channel = msg["subscribe"]
        channels[channel] << ws
        ws.send "{\"subscribed\": \"#{channel}\"}"
      end

      unless msg["unsubscribe"].nil?
        channel = msg["unsubscribe"]
        channels[channel].delete ws
        ws.send "{\"unsubscribed\": \"#{channel}\"}"
        channels[channel].delete(ws)
      end
    }

    ws.onclose {
      puts "WebSocket connection closed"
      channels.each { |__, wss|
        wss.delete(ws)
      }
      p channels
    }

    ws.onerror { |error|
      if error.kind_of?(EM::WebSocket::WebSocketError)
        puts "WebSocket error: #{error}"
      else
        puts "Application error #{error}"
      end
    }
  end

  # Redis code.
  redis = EM::Hiredis.connect("redis://localhost:6379")

  redis.pubsub.psubscribe("*")
  redis.pubsub.on(:pmessage) { |__, channel, data|
    puts '=================='
    puts "Received message from redis", __, channel, data
    p channels[channel].length
    puts '=================='
    channels[channel].each { |ws|
      puts "Sending message to the client", data, ws
      ws.send data
    }
  }

}
