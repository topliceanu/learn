class MetricController < ApplicationController
  # Handles the API for creating metrics and posting data to them.

  def create
  end

  def read_all
  end

  private

    def create_params
      params.require(:ts, :value)
    end

end
