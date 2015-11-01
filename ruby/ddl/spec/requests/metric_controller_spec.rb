require 'rails_helper'

RSpec.describe MetricController, type: :request do

  before :each do
    @account = Account.create({email: 'me@ddl.com', pass: 'superduper'})
  end

  describe "#create" do
    it 'should create a new metric' do
      payload = {name: 'my.test.metric', desc: 'test metric'}
      post "/accounts/#{@account.id}/metrics", payload

      expect(response.status).to be(200)

      body = JSON.parse(response.body)
      expect(body["name"]).to eq(payload[:name])
      expect(body["desc"]).to eq(payload[:desc])

      metrics = @account.metrics
      expect(metrics.length).to eq(1)
      expect(metrics[0]['name']).to eq(payload[:name])
      expect(metrics[0]['desc']).to eq(payload[:desc])
    end

    it 'should complain if the account does not exist' do
      not_an_account_id = 111
      payload = {name: 'my.test.metric', desc: 'test metric'}
      post "/accounts/#{not_an_account_id}/metrics", payload

      expect(response.status).to eq(404)
    end

    it 'should complain if there already is another metric with the same name' do
      payload = {name: 'my.test.metric', desc: 'test metric'}
      @account.metrics.create(payload)
    end
  end

  describe '#update' do
    before :each do
      @metric = @account.metrics.create({name: 'my.test.metric', desc: 'test metric'})
    end

    it 'should update an existing metric' do
      payload = {name: 'my.modified.test.metric'}
      patch "/accounts/#{@account.id}/metrics/#{@metric.id}", payload

      expect(response.status).to eq(200)
      @metric.reload
      expect(@metric.name).to eq(payload[:name])
    end

    it 'should complain when no metric is available' do
      patch "/accounts/#{@account.id}/metrics/111", {}

      expect(response.status).to eq(404)
    end

    it 'should complain when no account is available' do
      patch "/accounts/111/metrics/#{@metric.id}", {}

      expect(response.status).to eq(404)
    end
  end

  describe '#add_datapoint' do
    before :each do
      @metric = @account.metrics.create({name: 'my.test.metric', desc: 'test metric'})
    end

    it 'should create a new datapoint' do
      payload = {ts: Time.now.to_i, value: Random.rand(100)}
      post "/accounts/#{@account.id}/metrics/#{@metric.id}/datapoints", payload

      expect(response.status).to eq(201)
      expect(response.body).to eq('')

      expect(@metric.datapoints.length).to eq(1)
    end

    it 'should reject the datapoint if it does not validate' do
      payload = {ts: 'this is not a timestamp', value: 'fake-value'}
      post "/accounts/#{@account.id}/metrics/#{@metric.id}/datapoints", payload

      expect(response.status).to eq(400)
    end
  end

  describe '#read_datapoints' do
    before :each do
      @metric = @account.metrics.create!({name: 'my.test.metric', desc: 'test metric'})
      @start = Time.now.to_i
      datapoints = (1..10).map { |i| {ts: @start - i*10, value: Random.rand(100)} }
      @datapoints = @metric.datapoints.create!(datapoints)
    end

    it 'should return all the datapoints' do
      get "/accounts/#{@account.id}/metrics/#{@metric.id}/datapoints"

      expect(response.status).to eq(200)
      data = JSON.parse(response.body)
      expect(data.length).to eq(10)
    end

    it 'should return only the last datapoints' do
      query = { start: @start - 5*10}
      get "/accounts/#{@account.id}/metrics/#{@metric.id}/datapoints", query

      expect(response.status).to eq(200)
      data = JSON.parse(response.body)
      expect(data.length).to eq(5)
    end

    it 'should return a subsets of datapoints' do
      query = { start: @start - 5*10, end: @start - 3*10}
      get "/accounts/#{@account.id}/metrics/#{@metric.id}/datapoints", query

      expect(response.status).to eq(200)
      data = JSON.parse(response.body)
      expect(data.length).to eq(3)
    end
  end
end
