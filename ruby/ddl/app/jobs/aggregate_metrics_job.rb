class AggregateMetricsJob < ActiveJob::Base
  queue_as :default

  def perform(*args)
    puts "Worker at #{Time.now}"
  end
end
