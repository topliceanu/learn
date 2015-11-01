class AddIndexDatapointsMetricIdAndTimestamp < ActiveRecord::Migration
  def change
    add_index :datapoints, [:metric_id, :ts], :unique => true
  end
end
