# Stanford's Algorithms I Class on Coursera

`src` contains all the source code.

`test` contains fixtures and test cases.


## Tests

```bash
cd learn/algo
python -m unittest discover test # to run all tests.
python -m unittest discover test -p `test_graph.py` # to run a specific test case.
```

## Primitives

### Part 1
1. karatsuba multiplication
2. recursion
3. master method - big O analysis of recursive algorithms.
4. counting inversions
5. sub-cubic matrix multiplication by Strassen
6. closest pair of points in 2D
7. quicksort
8. selection of an element on position k in an unsorted array - randomized and deterministic
9. minimum cut - Karger's randomized algorithm.
10. breadth-first search - single source shortest path distance, undirected conectivity
11. depth-first search - topological sort, strong components
12. DAG - directed acyclic graph
13. heap data structure
14. single source shortest path - dijkstra algorithm
15. binary search tree
16. ballanced binary search tree - red/black tree.
17. hash tables
18. universal hashing
19. bloom filters

### Part 2
1. caching
2. job scheduling
2. greedy methodology
3. minimum spanning tree - prim, kruskal
5. union-find data structure
6. clustering - single-link, k-means, graph clustering
7. prefix-codes
8. dynamic programming - max-weight independent set, sequence alignment, knapsack, optimal binary search tree.
9. single source shortest path (in graphs with negative cost edges and non-negative cycles) - bellman-ford algorithm.
10. all pairs shortest path - algoritms by floyd warshall (dynamic programming), johnson (combo of bellman-ford and dijkstra).
11. vertex-cover
12. traveling salesman (dynamic programming)
13. local search optimization approach
14. maximum cut
15. 2sat
16. random walk
17. stable matching
18. maximum flow
19. minimum cut
20. linear programming

### Extra
1. A* (a-start) search algorithm
2. backtracking
3. bit manipulation
4. flood fill
5. logical clocks
6. multimap
7. radix sort
8. string matching
9. skiplist
10. splay tree
11. trie

## Todo

### Part 1
0. [X] refactor trees to support custom data in the nodes..
0. [ ] implement btree
1. [X] implement avl tree
1. [ ] implement lsm tree.
3. [ ] dijkstra single source shortest path - return the actual shortest paths.
4. [ ] red-black tree delete should work correctly.
5. [X] backtracking algorithms
6. [ ] implement a compressed Trie data structure.
7. [ ] implement range trees: [ ] interval trees, [ ] segment trees, [ ] binary indexed trees.
8. [ ] implement KD-trees
9. [X] flood fill algorithm
10. [ ] implement Bitmapped Vector Trie

### Part 2
1.  [x] caching - finish implementation of ARCache.
2.  [ ] min spanning tree - randomized algorithm for min spanning tree by Tarjan.
4.  [ ] min spanning tree - minimum spanning bottleneck tree!
5.  [ ] min spanning tree - optimal branching problem for directed graphs (prim&kruskal work for undirected graphs)
6.  [ ] min spanning tree - implement O(m) algorithm by Karger-Klein-Tarjan
7.  [x] huffman code - fix huffman coding
8.  [ ] dynamic programming - max-weight independent set - compute for trees.
9.  [ ] dynamic programming - find best approximate match of substring in string.
10. [ ] dynamic programming - longest common subsequence of two strings.
11. [ ] dynamic programming - linear partition - solution reconstruction does not work.
12. [ ] dynamic programming - flower garden problem!
13. [ ] substring matching - implement knut-morris-pratt, boyer-moore, rabin-karp algorithms. See `single_pattern_string_matching.py`.
14. [ ] knapsack - use dynamic programming to solve the two knapsack problem. (generalize to m different knapsacks!)
        - Add another dimension to the array to keep track of the residual capacity of the second knapsack, this increases the running time by a factor of at most W.
15. [ ] bellman-ford - optimize memory consumption on the algorithm.
16. [ ] bellman-ford - implement solution reconstrunction.
17. [ ] 3sat - implement the algorithm for 3sat by Uwe Schoening.
18. [ ] bipartite-matching - use maximum flow to solve bipartite matching.
19. [ ] maximum flow - implement the Edmonds-Karp advanced algorithm
19. [ ] maximum flow - solve minimum cost for maximum flow problem.
20. [ ] maximum flow - solve minimum cut using maximum flow algorithm.
21. [ ] data structures - implement the d-ary heap
22. [ ] traveling salesman - make the fast version work for very large instances (ie. programming assignment 5)
23  [ ] fix tests for the convex hull implementation.
24. [ ] learn linear programming
25. [ ] learn semi-definite programming

## List of Computer Scientists

1. Robert Prim - 1957 - Prim's minimum spanning tree (also by Dijkstra in 1959 and Vojtech Jarnik in 1930!).
2. Joseph Kruskal - 1956 - Kruskal's minimum spanning tree.
3. Robert Trajan - Union Find O(m\*log_star n) amortized running time; minimum spanning tree in O(m) time.
3. David Karger - minimum spaning tree in O(m) time.
3. Rolf Dieter Klein - minimum spaning tree in O(m) time.
4. Albert Huffman - 1952 - developed huffman prefix-free variable-length lossless compression codes.
5. Saul Needleman, Christian Wunsch - sequence alignment algorithm.
6. Richard Bellman - 1940s - invented dynamic programming; 1956 - single source shorted path algo (known as bellman-ford algo).
7. Lester Ford - 1958 - single source shortest path algo (known as bellman-ford algo).
8. Robert Floyd - 1962 - all pairs shortest path (known as Roy-Floyd-Warshall algorithm)
9. Bernard Roy - 1959 - all pairs shortest path (known as Roy-Floyd-Warshall algorithm)
10. Stephen Warshall - 1962 - all pairs shortest path (known as Roy-Floyd-Warshall algorithm)
10. Donald Johnson - 1977 - algorithm to compute all pairs shortest path (Johnson's algorithm); 1975 - d-ary heap data structure.
11. Christos Papadimitriou - randomized algorithm for 2sat problem.
12. Lloyd Shapley - 1962 - stable matching algorithm
13. David Gale - 1962 - stable matching algorithm
14. George Bernard Dantzig - inventor of linear programming

## Wikipedia Links

- `http://en.wikipedia.org/wiki/Robert_C._Prim`
- `http://en.wikipedia.org/wiki/Vojt%C4%9Bch_Jarn%C3%ADk`
- `http://en.wikipedia.org/wiki/Joseph_Kruskal`
- `http://en.wikipedia.org/wiki/Huffman_coding#Applications`
- `http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm`
- `http://en.wikipedia.org/wiki/Richard_E._Bellman`
- `http://en.wikipedia.org/wiki/L._R._Ford,_Jr.`
- `http://en.wikipedia.org/wiki/Robert_W._Floyd`
- `http://en.wikipedia.org/wiki/Bernard_Roy`
- `http://en.wikipedia.org/wiki/Stephen_Warshall`
- `http://en.wikipedia.org/wiki/Christos_Papadimitriou`
- `http://en.wikipedia.org/wiki/Lloyd_Shapley`
- `http://en.wikipedia.org/wiki/David_Gale`
- `http://en.wikipedia.org/wiki/Donald_B._Johnson`
- `http://en.wikipedia.org/wiki/George_Dantzig`
