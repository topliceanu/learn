require 'json'

require 'em-websocket'
require 'em-hiredis'
require 'juggler'


EM.run {
  puts "WebSockets server started"
  channels = Hash.new([])

  # Create redis connection and subscribe to all channels.
  redis = EM::Hiredis.connect("redis://localhost:6379")
  redis.pubsub.psubscribe("*")

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

      unless msg["channel"].nil?
        channel = msg["channel"]
        data = msg["data"]
        redis.publish(channel, data.to_json)
        Juggler.throw(:channel, {:channel => channel, :data => data})
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

  redis.pubsub.on(:pmessage) { |__, channel, data|
    puts "Received message from redis", channel, data
    channels[channel].each { |ws|
      ws.send data
    }
  }

}
