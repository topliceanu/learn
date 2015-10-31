class MetricController < ApplicationController
  # Handles the API for creating metrics and posting data to them.

  def create
    # Creates a new metric.
    metric = Metric.new(params)
    is_saved = metric.save
    if is_saved
      render json: metric
    else
      render json: {error: metric.errors}
    end
  end

  def update
    # Modifies an existing metric.
  end

  def remove
    # Removes an existing metric.
  end

  def add_datapoint
    # Adds a new datapoint to an existing metric.
  end

  def read_datapoints
    # Returns a list of datapoints for the current metric.
  end
end
