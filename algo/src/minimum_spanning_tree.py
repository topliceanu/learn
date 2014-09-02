# -*- coding: utf8 -*-

def prims_mst(graph):
    """ Computes minimum spanning tree using the Prim's algorithm.

    Args:
        graph: object, undirected graph where each edge has an associated cost
            (which can be negative).

    Returns:
        A subgraph tree of minimal cost. ie. a connected subgraph with no
        cycles and whose sum of all edges is minimal.
    """
