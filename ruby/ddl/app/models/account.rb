class Account < ActiveRecord::Base
  validates :email, presence: true, length: { in: (5..100) }
  validates :pass, presence: true, length: { in: (5..100) }
  has_many :charts, inverse_of: :account
  has_many :metrics, inverse_of: :account
end
