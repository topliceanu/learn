# 9.5 Search cache

1. Scope the problem
- features: cache as many results as possible
- size: 100 boxes (128GB RAM, 2TB SSD)
  search result: 50bytes query + 200 * (title, snippet) (5KB)
2. Assumptions
- LRU is sufficient as an eviction algorithm
- communication between the 100 boxes is fast (<1ms) and stable (data center networking)
- popular queries are very popular, standard deviation is low
3. Alternatives
- each machine has its own cache. Disadvange: poor utilization of space
- each machine has a copy of the cache. Disadvantage: synchronization between machines
- each machine stores a segment of the cache.
4. Diagram
- organise the cache by sharding: hash the search queries and store a subset of queries (say first 7 bits) on each of the available boxes.
- each node knows where each shard lives and can redirect requests to that shard
- each shard lives on 3 boxes
![diagram](https://excalidraw.com/#json=4787833994739712,tj4tfZzHuxoDMTt8uVXMcw)
- walk through a cache hit but on different machine:
  - client make a search query, reaches box i
  - box i hashes the query. If it has the results, it serves them, otherwise identifies box j that has the cache
  - box i contacts j and fetches the results, then forwards to client
- walk through a cache miss:
  - client make a search query, reaches box i
  - box i hashes the query, identifies box j who should handle that hash, contacts box j.
  - box j doesn't have the result so it calls the backend, updates it's cache, then responds to i
  - i responds to the client
5. Identify key issues
- cache miss - which box calls searchQuery? which box stores the cache?
Solution1: the box receiving the request. Solution2: the box closest to the client
- cache invalidation - what happens if results change? Solution: expire caches automatically
- network/box failures. Solution: store the same cached key on multiple servers
- cache eviction strategy - how do you evict? Solution: each node and its replicas evict independently
- you can have a node that monitors requests, identifies hot queries and caches them

