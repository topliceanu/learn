# -*- coding: utf-8 -*-

from src.bellman_ford import shortest_path as bellman_ford_shortest_paths
from src.dijkstra_shortest_path import shortest_path_heap as dijkstra_shortest_path
from src.graph import Graph


def all_pairs_shortest_path(g):
    """ Compute the shortest path for every pair of vertices in the given graph.

    Algorithm:
    1. Add a new vertex 'S' and connect it to every other vertex in the graph
    with an edge of value 0.
    2. Run bellman-ford with the source vertex being 'S' to compute shortest
    paths to all other vertices.
    3. If bellman-ford detects a negative cycle, report it and exit.
    4. Assign the value of the shortest path from 'S' to vertex X as the weight of X.
    5. Remove 'S' and all egress edges from the graph.
    6. Compute new weights for each edge with the formulat Ce' = Ce - Cu + Cv.
    7. Run Dijkstra from each of the original nodes to compute shortest paths.
    8. Extract the true shortest paths for each pair Ce' by subtracting Cu and Cv.

    Running Time: O(mnlogn) - for dense graphs m=O(n^2) it's O(n^3logn)

    Params:
        g: object, object encapsulating a graph.

    Returns:
        False, if the graph has a negative cost cyle in it
        dict, containg costs for each pair of vertices, format {tail: {head: min_cost}}
    """
    # 1.
    g.add_vertex('s')
    for vertex in g.get_vertices():
        g.add_edge(('s', vertex, 0))

    # 2.
    shortest_paths = bellman_ford_shortest_paths(g, 's')

    # 3.
    if shortest_paths is False:
        return False

    # 4.
    for head, cost in shortest_paths.iteritems():
        g.set_vertex_value(head, cost)

    # 5.
    g.remove_vertex('s')

    # 6.
    for (tail, head, value) in g.get_edges():
        newValue = value - g.get_vertex_value(tail) + g.get_vertex_value(head)
        g.set_edge_value((tail, head), newValue)

    # 7.
    out = {}
    for vertex in g.get_vertices():
        out[vertex] = dijkstra_shortest_path(g, vertex)

    # 8.
    for tail, span in out.iteritems():
        for head, cost in span.iteritems():
            out[tail][head] = cost + g.get_vertex_value(tail) - g.get_vertex_value(head)

    return out
