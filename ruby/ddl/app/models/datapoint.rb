class Datapoint < ActiveRecord::Base
  belongs_to :metric, index: false, inverse_of: :datapoints
  validate :ts, uniqueness: { scope: :metric_id }
  validate :ts, numericality: { greater_than: 0 }
end
