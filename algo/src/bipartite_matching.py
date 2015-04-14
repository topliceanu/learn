# -*- coding: utf-8 -*-


def bipartite_matching(g):
    """ Solves the bipartite matching problem.

    Reduces to the maximum flow problem.

    Params:
        g, instance of src.graph.Graph which is bipartite graph, ie. there
            exists a cut which crosses all edges in the graph.
    """
