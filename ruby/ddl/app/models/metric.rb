class Metric < ActiveRecord::Base
  validates :name, uniqueness: { scope: :account_id }
  belongs_to :account, inverse_of: :metrics
  has_many :datapoints, inverse_of: :metric
end
