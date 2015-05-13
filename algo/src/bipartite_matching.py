# -*- coding: utf-8 -*-

from src.maximum_flow import ford_fulkerson_maximum_flow


def bipartite_matching(g):
    """ Solves the bipartite matching problem.

    Given a bipartite graph where each node on the left is connected to the
    nodes on the right to which it wishes to be connected to, edge weights
    corresponding to the preference.

    Reduces to the maximum flow problem.

    Complexity: polinomial time

    Args:
        g, instance of src.graph.Graph which is bipartite graph, ie. there
            exists a cut which crosses all edges in the graph.

    Returns:
        list, of pairs, format [(u, v)]
    """
    # TODO
