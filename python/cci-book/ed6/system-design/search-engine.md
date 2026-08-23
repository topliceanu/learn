# Search engine

1. scope the problem
- features: words can appear multiple times in a document
-
2. make assumptions
- a subset of the words are mostly used - removing stop words
- replace words with their ids
3. draw diagram
- build and inverted index: {word => docs...}
- split the index into shards, each shard contains a subset of words - hash the words
- ![drawing](https://excalidraw.com/#json=5096733075832832,2ePHwlxT0_J-jt7tRD4sPQ)
4. identify key issues
- pathological queries. Solution: colocate words that are usually searched toghether
- queries with many words. Solution 1: resolve queries at the storage layer - calculate result cardinality for each word.
Solution 2: store results for multiple words
- hot shards. Solution: put the same words on multiple shards.
- query resolver fails midway through a query. Solution: retry mecanism
- storage node fails. Solution: each shard is replicated 3+ times on different nodes.
5. Alternatives:
- shard by document hash, each box keeps a subset of the documents in it's own index
- query resolve merges results from all shards.
- disadvanges: each query hits all boxes, not scalable.
