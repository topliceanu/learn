type 'a graph = 'a list * ('a * 'a) list (* vertices x edges *)

(* Strongly connected components in a directed acyclical graph (DAG).
* A strongly connected components is a section of a DAG where each node is reachable from any other node.
* Kosaraju's algorithm: https://en.wikipedia.org/wiki/Kosaraj u
* My understading of the idea:
*  - step 1. topologically sort vertices in the inverted graph (ie. edges are inverted). 
*        Note, it's not an actually topological sort because that doesn't work on graphs with cycles. Instead the vertices we already visited are ignored.
*        This identifies the sinks in the condensation graph (ie. the graph where each CC becomes a node).
*  - step 2. pick the first sink, and run DFS. this will identify the first SCC, which is the sink node in the condensed graph.
*        Recurse until there are no more nodes in the list from 1.
* See: https://cp-algorithms.com/graph/strongly-connected-components.html
*)
let kosaraju_scc g = 
  (* var rev : 'a graph -> 'a graph *)
  let rev g =
    let (vertices, edges) = g in
      (vertices, List.map (fun (x, y) -> (y, x)) edges)

  (* val dfs: 'a -> 'a graph -> 'a list -> 'a list *)
  (* Dfs traverses the graph recursively from source v ignoring all visited nodes and produce as list of newly visited nodes*)
  in let rec dfs v g visited new_visited =
    if List.mem v visited then new_visited
    else 
      let (_, edges) = g in
      let adjs = List.fold_left (fun adjs (x, y) ->
        if x == v && not (List.mem y (new_visited @ visited)) then y :: adjs
        else adjs
      ) [] edges
    in let new_visited = List.fold_left (fun acc w ->
      acc @ (dfs w g  visited (v::new_visited))
    ) [] adjs
    in v :: new_visited

  (* val topological_sort: 'a graph -> 'a list *)
  (* Builds an ordering of the vertices, cycles are permitted as in whenever a new visited vertex is discovered, it's skipped!*)
  in let topological_sort g =
    let (vertices, edges) = g 
    in List.fold_left (fun visited v -> 
      let new_visited = dfs v g visited []
      in new_visited @ visited 
    ) [] vertices
  in let first_pass = topological_sort (rev g)
  (* Recurse over the sinks in the sorted nodes until all SCCs are traversed.*)
  in List.fold_left (fun (sccs, visited) v -> 
    let scc = dfs v g visited []
    in (scc :: sccs, scc @ visited)
  ) ([], []) first_pass

  
(* val dijkstra_single_source_shortest_paths: 'a -> 'a graph -> 'a list *) 
let dijkstra_single_source_shortest_paths src g = g
