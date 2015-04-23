# -*- coding: utf-8 -*-


def maximum_flow(g, s, t):
    """ Solves the maximum flow problem.

    Given a directed weighted graph g, a source vertex s and a sink vertex t,
    send as much flow as possible from s to t, knowing that each edge has a
    capacity value which is the maximum ammount of flow that the edge can
    accomodate.

    Running time: O(m*n) where m - number of edges, n - number of vertices.

    Params:
        g: object, instance of src.graph.Graph
        s: str, name of the source vertex
        t: str, name of the sink vertex
    """

def ford_fulkerson_maximum_flow(g, s, t):
    """ Solves the maximum flow problem using the ford-fulkerson algorithm.
    """
