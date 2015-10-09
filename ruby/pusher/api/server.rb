require "sinatra"
require "hiredis"


redis = Hiredis::Connection.new
redis.connect("127.0.0.1", 6379)


post "/events/:channel" do
  channel = params["channel"]
  redis.write ["PUBLISH", channel, request.body.read]
  puts "Publishing message ", channel, redis.read
  200
end
