class CreateMetrics < ActiveRecord::Migration
  def change
    create_table :metrics do |t|
      t.string :name, limit: 100, null: false
      t.string :desc, limit: 255, null: false
      t.datetime :created_at, null: false
      t.belongs_to :account, index: true
    end
  end
end
