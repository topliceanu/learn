# 9.6 Sales rank

1. Scope the problem
- How many categories? how many products? how many users? how many impression of these recommendations?
- What is the time interval I'm looking at: last month, last week, today?

2. Assumptions
- I'm making the assumptions that: num categories << num products << num users <<< num impressions
- I'm assuming the input to the system is (prod-id, [cat-ids], ts). You can fetch product descriptions if you have the ids later.
- I'm assuming that the query to the system is (cat-id, pos) and the response is prod-id. You can fetch product description later.
- Assuming that categories are not related (eg. subcategories). Assuming that each product is in multiple categories.

3. Draw components
- To know which products are the most popular, you need impression counters and you need to remove old impressions (or views), hence a sliding window.
  - every 10seconds you need to pop the old view from the sliding window.
  - this can be made more efficient by bunching toghether more updates into chunks of 10s updates OR by sampling.
- Splitting the read path of the system from the write path. The point of contention will be the category
- On the write path: a stream of updates (user-id, product-id, list-of-categories, timestamp)
- On the read path: the query is (cat-id, pos). The datastructure would look like {category: [sorted-prod-ids]}

4. Identify issues
- How do you deal with "hot categories", eg. xmas presents in winter?
  - You can add read-replication. The API proxy will forward requests to the replicas.

  ....
