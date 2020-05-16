# Design TinyURL

1. Scope the problem:
- features: short urls, analytics
- data sizes: 1 link = 100bytes.
- the main resource user is the analytics
2. List assumptions
- separate write and read paths
- we want to scale horizontally - increase capacity linearly
- avoid hot shards
3. Draw diagram
- a prefix is the first 5 characters in a short url hash. { prefix => [{box, ro|rw}] }
- a metadata layer: a lvl4 LB in front and multiple boxes, all storing the mapping between prefixes and boxes.
- a storage layer: they just write and retrieve data
- use case 1: user write a new url
  - LB randomly allocates a proxy box, which assigns a prefix at random, and redirects to the storage node
  - the storage node hashes the original link, stores the pair and return the minified link
  - the proxy returns the minified link and pings the analytics system
- use case 2: user clicks on a minified url
  - LB randomly allocates a proxy, proxy extracts the prefix, identifies the storage node and forwards request.
  - storage node extracts expanded/original link and returns it to the proxy
  - proxy redirects client to original url and fires an async event to analytics
![excalidraw](https://excalidraw.com/#json=5751483232419840,KmpVZCxeU5TDH5ur0cSY_Q)
4. Identify issues
- the proxy nodes may fail. Solution: autoscaling, store same mapping on all of them
- a box is full. Solution: add new storage box for that prefix, remove the full box from the list of write node
- a prefix is full. Solution, remove it from the write set add a new storage box with a new prefix
