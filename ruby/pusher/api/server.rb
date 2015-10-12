require "eventmachine"
require "em-hiredis"
require "sinatra/base"
require "thin"


class API < Sinatra::Base
  def initialize(redis)
    super
    @redis = redis
  end

  configure do
    set :threaded, false
  end

  get '/ping' do
    'pong'
  end

  post '/events/:channel' do
    channel = params["channel"]
    payload = request.body.read
    @redis.publish(channel, payload)
  end
end

EM.run {
  redis = EM::Hiredis.connect

  dispatch = Rack::Builder.app do
    map '/' do
      run API.new(redis)
    end
  end

  Rack::Server.start({
    app: dispatch,
    server: 'thin',
    Host: '0.0.0.0',
    Port: 8080,
    signals: false
  })
}
