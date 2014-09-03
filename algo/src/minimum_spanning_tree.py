# -*- coding: utf8 -*-

import random

from src.graph import Graph


def prims_suboptimal_mst(graph):
    """ Computes minimum spanning tree using the Prim's algorithm.

    Running time O(n^2)

    Args:
        graph: object, undirected graph where each edge has an associated cost
            (which can be negative).

    Returns:
        A subgraph tree of minimal cost. ie. a connected subgraph with no
        cycles and whose sum of all edges is minimal.
    """
    #import pdb; pdb.set_trace()
    mst_vertices = []
    mst_edges = []

    start_vertex = random.choice(graph.get_vertices())
    mst_vertices.append(start_vertex)

    while len(mst_vertices) != len(graph.get_vertices()):

        min_value = float('inf')
        min_edge = None
        min_vertex = None
        for edge in graph.get_edges():
            [tail, head, value] = graph.split_edge(edge)
            if ((tail in mst_vertices and head not in mst_vertices) or \
              (head in mst_vertices and tail not in mst_vertices)) and \
              (value < min_value):
                min_value = value
                min_edge = edge
                if tail not in mst_vertices:
                    min_vertex = tail
                else:
                    min_vertex = head

        mst_vertices.append(min_vertex)
        mst_edges.append(min_edge)

    mst = Graph.build(edges=mst_edges, directed=False)
    return mst
