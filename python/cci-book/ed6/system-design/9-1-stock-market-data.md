# 9.1 Stock market data

1. Scope the problem
- features/use-cases: get the latest snapshot of data, - get historical data
- numbers: 1000 clients, 100 requests/second,
    5000 companies on the stock exchange * 240 days open * 4 data points * (64 + 8 + 128)
2. Assumptions
- data is immutable
- it's a log of triplets (key, value, timestamp) - it's a timeseries.
- data has locality of reference: everyone will call to get the data at the end of market day
3. Alternatives:
- first, files exposed through a SFTP server. Downside: format inconsistent.
- second, XML or JSON exposed through a REST api. Downside: inflexible, overhead.
- third, stick data into SQL, expose TCP port to clients. Downside: security model.
4. Diagram
- if we want historical, then we need a data store
- we can cache recent data: as soon as data is available, load it onto caches.
- ![diagram](https://excalidraw.com/#json=4902715243102208,rY1svXoksaJZSfwSPlwGMA)
5. Key issues
- data format and encoding. You can't change it afterwards. Solution: IDL like protobuf.
- scale historical data. Solution: indexes
- thundering herds: Solution: auto-scaling, rate-limitting per box, per client
