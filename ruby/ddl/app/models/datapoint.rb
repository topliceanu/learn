class Datapoint < ActiveRecord::Base
  belongs_to :metric, inverse_of: :datapoints
  validates :ts, uniqueness: { scope: :metric_id }
  validates :ts, numericality: { greater_than: 0 }
end
