class CreateDatapoints < ActiveRecord::Migration
  def change
    create_table :datapoints, id: false do |t|
      t.integer :value, null: false
      t.integer :ts, null: false
      t.belongs_to :metric
    end
  end
end
