class MetricController < ApplicationController
  # Handles the API for creating metrics and posting data to them.

  def create
    # Creates a new metric.
    account = Account.find_by_id(create_params[:account_id])
    unless account
      return render status: 404, json: {error: "Unable to find account with id #{create_params[:account_id]}"}
    end

    metric = account.metrics.new(create_params)
    if metric.save
      render status: 200, json: metric
    else
      render status: 400, json: {error: metric.errors}
    end
  end

  def update
    # Modifies an existing metric.
    metric = Metric.where(id: update_params[:metric_id]).includes(:account).first
    unless metric
      return render status: 404, json: {error: "Unable to find metric to update with id #{update_params[:metric_id]}"}
    end

    unless metric.account.id.to_s == update_params[:account_id].to_s
      return render status: 404, json: {error: "Unable to find account with id #{update_params[:account_id]}"}
    end

    [:name, :desc].each do |key|
      metric[key] = update_params[key] if update_params.has_key?(key)
    end

    if metric.save
      render status: 200, json: metric
    else
      render status: 400, json: {error: metric.errors}
    end
  end

  def remove
    # Removes an existing metric.
  end

  def add_datapoint
    # Adds a new datapoint to an existing metric.
    metric = Metric.where(id: add_params[:metric_id], account_id: add_params[:account_id]).first
    unless metric
      return render status: 404, json: {error: "Unable to find metric to update with id #{update_params[:metric_id]}"}
    end

    datapoint = metric.datapoints.new({ts: add_params[:ts], value: add_params[:value]})
    if datapoint.save
      render status: 201, nothing: true
    else
      render status: 400, json: {error: datapoint.errors}
    end
  end

  def read_datapoints
    metric = Metric.where(id: read_params[:metric_id], account_id: read_params[:account_id]).first
    unless metric
      return render status: 404, json: {error: "Unable to find metric to update with id #{update_params[:metric_id]}"}
    end

    # TODO correctly build the query.
    if read_params.has_key?(:start) && !read_params.has_key?(:end)
      datapoints = metric.datapoints.select('ts, value')
        .where('ts >= ?', read_params[:start])
    elsif !read_params.has_key?(:start) && read_params.has_key?(:end)
      datapoints = metric.datapoints.select('ts, value')
        .where('ts <= ?', read_params[:end])
    elsif !read_params.has_key?(:start) && !read_params.has_key?(:end)
      datapoints = metric.datapoints
    else
      datapoints = metric.datapoints.select('ts, value')
        .where('ts >= ?', read_params[:start])
        .where('ts <= ?', read_params[:end])
    end

    render status: 200, json: datapoints
  end

  private

  def create_params
    params.permit(:name, :account_id, :desc)
  end

  def update_params
    params.permit(:metric_id, :account_id, :name, :desc)
  end

  def add_params
    params.permit(:metric_id, :account_id, :ts, :value)
  end

  def read_params
    params.permit(:metric_id, :account_id, :start, :end)
  end
end
