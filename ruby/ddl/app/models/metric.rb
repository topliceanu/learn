class Metric < ActiveRecord::Base
  belongs_to :account, inverse_of: :metrics
  has_many :datapoint, inverse_of: :metric
end
