# -*- coding: utf-8 -*-

from src.graph import Graph


INF = float('inf')

def all_pairs_shortest_path(graph):
    """ Implements the Roy-Floyd-Warshall algorithm for computing min cost
    shortest paths between any two vertices in the input graph which does not
    have negative cycles.

    Complexity: O(n^3) - NOTE it's independent of the sparsity (num of edges)
        of the graph.
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
