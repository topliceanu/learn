# -*- coding: utf-8 -*-

import random


def pick_random_edge(graph):
    """ Returns a random edge from the given graph. """
    random.randint(0, len(graph.edges) - 1)

def contract(graph, edge):
    """
        Composes a new vertex from the ends of the given edge.
        All the resulting self-loop edges are removed.
    """
    [start, end] = edge
    super_vertex = '{start}_{end}'.format(start=start, end=end)

    # Remove individual vertices and add super-vertex.
    graph.replaceVertex(start, super_vertex)
    graph.replaceVertex(end, super_vertex)

    # Process edges such that start and end vertices
    # are replaced by the new super-vertex.
    # Also remove self-loops.
    for edge in graph.edges:
        [s, e] = edge
        if (s == start and e == end) or (s == end and e == start):
            graph.delete(s, e)
        elif (s == start) or (s == end):
            edge[0] = super_vertex
        elif (e == start) or (e == end):
            edge[1] = super_vertex

    return graph

def minimum_cut(graph):
    """ Finds the cut in a given graph with
    the lowest number of crossing edges using
    the random contraction algorithm.

    Defined by David Carted in eary 90s.
    Returns
    Two lists of vertices representing the split graphs.
    """
    while len(graph.vertices) != 2:
        edge = pick_random_edge(graph)

        graph = contract(graph, edge)

    left = graph.vertices[0].split('_')
    right = graph.vertices[1].split('_')
    return left, right
