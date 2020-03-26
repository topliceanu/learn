# -*- coding: utf-8 -*-

import random

from src.maximum_flow import ford_fulkerson_maximum_flow


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

def randomized_cut(graph):
    """ Finds a cut in a given graph using the random contraction algorithm
    defined by David Karger in '93.

    NOTE! This algorithm modifies the graph in place, so make sure you clone
    it before compacting if you don't want your original graph modified.

    Args:
        graph: a data structure containg all data and operations.

    Returns:
        The compacted graph.
    """
    while len(graph.get_vertices()) != 2:
        edge = pick_random_edge(graph)
        contract(graph, edge)

    return graph

def minimum_cut(graph, tries):
    """ Finds the the minimum cut in the given graph after a running the
    randomized cut algorithm a given number of tries.

    Args:
        graph: a data structure containg all vertices, edges and supported
            operations.
        tries: int, number of times to try the randomized cut algorithm.

    Returns:
        cuts, list of cut edges which produce the minimum cut.
    """
    min_cuts = []
    for __ in xrange(tries):
        g = graph.clone()
        randomized_cut(g)

        [left_super_vertex, right_super_vertex] = g.get_vertices()
        left_vertices = set(left_super_vertex.split('_'))
        right_vertices = set(right_super_vertex.split('_'))

        cuts = []
        for left_vertex in left_vertices:
            right_neighbours = set(graph.neighbours(left_vertex))\
                                .intersection(right_vertices)
            for right_vertex in right_neighbours:
                cuts.append((left_vertex, right_vertex))

        if (len(min_cuts) == 0 or len(min_cuts) > len(cuts)):
            min_cuts = cuts

    return min_cuts

def minimum_cut_using_maximum_flow(graph, start, end):
    """ Solve the minimum cut problem by reducing it to maximum flow. """
    # TODO
