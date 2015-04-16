# -*- coding: utf-8 -*-

from src.bellman_ford import shortest_path as bellman_ford_shortest_paths
from src.dijkstra_shortest_path import shortest_path_heap as dijkstra_shortest_path
from src.graph import Graph


INF = float('inf')


def dijkstra(graph):
    """ Run dijkstra on all nodes in a graph with no cycles and no negative edges.
    """
    pass

def roy_floyd_warshall(graph):
    """ Implements the Roy-Floyd-Warshall algorithm for computing min cost
    shortest paths between any two vertices in the input graph which does not
    have negative cycles.

    Complexity: O(n^3) - NOTE it's independent of the sparsity (num of edges)
        of the graph.

    Params:
        g: object, object encapsulating a graph.

    Returns:
        False, if the graph has a negative cost cyle in it
        dict, containg costs for each pair of vertices, format {tail: {head: min_cost}}
    """

    # 0. Initialization
    vertices = graph.get_vertices()
    n = len(vertices)
    A = [[[0]*n for __ in range(n)] for __ in range(n)]

    for pos_i in range(n):
        for pos_j in range(n):
            i = vertices[pos_i]
            j = vertices[pos_j]
            if i == j: # When they are the same vertex.
                A[pos_i][pos_j][0] = 0
            elif graph.adjacent(i, j) is True: # When they are adjacent in the graph.
                A[pos_i][pos_j][0] = graph.get_edge_value((i, j))
            else: # When they are not adjacent in the graph.
                A[pos_i][pos_j][0] = INF

    # 1. Recurrence and check for negative cost cycles in the graph.
    has_negative_cost_cycles = False
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                A[i][j][k] = min(A[i][j][k-1], A[i][k][k-1]+A[k][j][k-1])
                if A[i][j][k] < 0:
                    has_negative_cost_cycles = True

    # 2. Print output.
    if has_negative_cost_cycles:
        return False
    else:
        out = []
        for i in range(n):
            out.append([])
            for j in range(n):
                out[i].append(A[i][j])
        return out

def johnson(g):
    """ Compute the shortest path for every pair of vertices in the given graph
    using the Johnson's algorithm.

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
