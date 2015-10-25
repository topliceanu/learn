class Chart < ActiveRecord::Base
  belongs_to :account, inverse_of: :charts
  validates :name, presence: true, limit: { maximum: 255 }
end
