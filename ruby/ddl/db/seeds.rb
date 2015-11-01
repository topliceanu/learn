# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)

a = Account.create!({email: 'me@ddl.io', pass: 'superduper'})

m = a.metrics.create!({name: 'my.metric', desc: 'simple metric to monitor'})

datapoints = (1..20).map { |i| {ts: Time.now.to_i - i * 10, value: Random.rand(20)} }
m.datapoints.create!(datapoints);
