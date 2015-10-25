class CreateAccounts < ActiveRecord::Migration
  def change
    create_table :accounts do |t|
      t.string :email, limit: 100, null: false
      t.string :pass, limit: 100, null: false
      t.timestamps null: false
    end
  end
end
