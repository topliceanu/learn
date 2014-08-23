# -*- coding: utf-8 -*-

import random


def pick_random_edge(graph):
    """ Returns a random edge from the given graph. """
    edges = graph.get_edges()
    return random.choice(edges)

def contract(graph, edge):
    """ Composes a new vertex from the ends of the given edge.

    All the resulting self-loop edges are removed.

    Args:
        graph: a data structure containg all data and operations.
        edge: a tuple of format (tail, head, value)

    Returns:
        The graph after contracting value.
    """
    (tail, head, value) = graph.split_edge(edge)
    super_vertex = '{start}_{end}'.format(start=tail, end=head)

    # Remove individual vertices and add super-vertex.
    graph.rename_vertex(tail, super_vertex)
    graph.rename_vertex(head, super_vertex)

    return graph

def minimum_cut(graph):
    """ Finds the cut in a given graph with
    the lowest number of crossing edges using
    the random contraction algorithm
    defined by David Carted in eary 90s.

    Args:
        graph: a data structure containg all data and operations.

    Returns:
        The compacted graph.
    """
    while len(graph.get_vertices()) != 2:
        edge = pick_random_edge(graph)
        graph = contract(graph, edge)

    return graph
