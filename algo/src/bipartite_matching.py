# -*- coding: utf-8 -*-


def bipartite_matching(g):
    """ Solves the bipartite matching problem.

    Given a bipartite graph where each node on the left has a strict preference
    onto which node on the right they want to be paired with.
    Reduces to the maximum flow problem.

    Complexity: polinomial time

    Args:
        g, instance of src.graph.Graph which is bipartite graph, ie. there
            exists a cut which crosses all edges in the graph.
    """
