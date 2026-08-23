(* facts is a graph where:
 - vertices are the units of measurement (m, ft, in, hr, min)
 - edges are directed, and contain an operation (multiplication) performed for the transformation 
 OR edges are triplets (src, dst, factor). Eg. ("m", "ft", 3.28), ("ft", "m", 1/3.28)

query is triplet: (source vertex, destination vertex, quantity of source)

The problem reduces to finding a path (shortest?) between source and destination vertices. 
- shortest path -> Dijkstra's algo; Disadvantage: generates shortest paths to all other nodes. We can have a pre-processing step where we run dijkstra from all nodes, and produce a bipartite graph between any vertex and any other vertex with the wight being the multiplication of the weights in the path.
  - Only works if there are no cycles. 
- any path we use DFS. The graph is a set of independent SCCs. 
*)

type 'a graph = ('a list * ('a * 'a * int) list)

(* val dfs : 'a graph -> 'a list *)
let dfs start g = g





