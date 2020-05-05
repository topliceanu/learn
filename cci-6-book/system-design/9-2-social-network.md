# 9.2 Social network

1. Scope the problem
- features: shortest path between two people
- data size: 2B users
2. Assumptions
- We can't fit all data on one machine
3. Diagram
- start DFS for shortest path from source and destination. Stop when a common node is found!
- best data structure is adjacency list
- ![drawing](https://excalidraw.com/#json=5203606399614976,0TE37x04J2ZWKzBVzyK_MA)
4. Key issues
- Sharding a large, constantly updating graph is hard.
  Solution1: preprocessing step: connected components, minimal cuts
  Solution2: when a new node is created choose the appropriate node for it.
- communication between nodes is expensive in graph search.
  Solution1: shard by location
  Solution2: overlapping graphs on each box, move vertices around as the links between them are more used!
- DFS is still going to go through a massive graph
  Solution: preprocessing, identify connector nodes.
