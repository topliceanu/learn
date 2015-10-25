class CreateCharts < ActiveRecord::Migration
  def change
    create_table :charts do |t|
      t.string :name, limit: 255
      t.belongs_to :account
      t.timestamps null: false
    end
  end
end
