# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20151024172101) do

  create_table "accounts", force: :cascade do |t|
    t.string   "email",      limit: 100, null: false
    t.string   "pass",       limit: 100, null: false
    t.datetime "created_at",             null: false
    t.datetime "updated_at",             null: false
  end

  create_table "charts", force: :cascade do |t|
    t.string   "name",       limit: 255
    t.integer  "account_id"
    t.datetime "created_at",             null: false
    t.datetime "updated_at",             null: false
  end

  create_table "datapoints", id: false, force: :cascade do |t|
    t.integer "value",     null: false
    t.integer "ts",        null: false
    t.integer "metric_id"
  end

  create_table "metrics", force: :cascade do |t|
    t.string   "name",       limit: 100, null: false
    t.string   "desc",       limit: 255, null: false
    t.datetime "created_at",             null: false
    t.integer  "account_id"
  end

  add_index "metrics", ["account_id"], name: "index_metrics_on_account_id"

end
