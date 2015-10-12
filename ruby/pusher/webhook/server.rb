require 'eventmachine'
require 'juggler'

# TODO make worker actually consume the tasks!
EM.run {
  Juggler.juggle(:channel, 5) do |msg|
    defer = EM::DefaultDeferrable.new

    puts 'Received webhook request'
    puts msg.inspect

    defer.set_deferred_status :succeeded, nil
    defer
  end
}
