# -*- coding: utf-8 -*-

import random


VISITED = 0x100

def dfs_loop(g):
    """ Orders the vertices in a directed graph in an efficient way
    using depth_first_search.

    Args:
        g: instance of src.graph.Graph data structure of vertices and edges.

    Returns:
        A list of the vertices in g, sorted in the order of traversal.
    """
    # 1. All vertices as already marked as un-visited.
    # 2. Initial order is the total number of vertices.
    global current_level
    global ordering

    current_level = len(g.get_vertices())
    ordering = {}

    def dfs(g, start_vertex):
        """ Classical depth-first-search algorithm."""
        global current_level
        global ordering

        g.set_vertex_value(start_vertex, VISITED)
        for neighbour in g.neighbours(start_vertex):
            if g.get_vertex_value(neighbour) != VISITED:
                dfs(g, neighbour)

        ordering[start_vertex] = current_level
        current_level -= 1

    # 3. Go through all unvisited edges.
    for vertex in g.get_vertices():
        if g.get_vertex_value(vertex) != VISITED:
            dfs(g, vertex)

    return ordering


# Less efficient implementation based on the fact that there
# exist at least one sync vertex and no cycles.

def get_sync_vertices(g):
    """ Returns a list of sync vertices.

    A sync vertex is a vertex with no outgoing arcs.

    Args:
        g: data structure encapsulating graphs.

    Returns:
        A list of all vertex names.
    """
    return [v for v in g.get_vertices() if len(g.neighbours(v)) == 0]

def recurse_pick_then_remove_sync(g, pos):
    sync_vertices = get_sync_vertices(g)
    if len(sync_vertices) == 0:
        return

    sync = random.choice(sync_vertices)
    g.set_vertex_value(sync, pos)
    g.remove_vertex(sync)
    recurse_pick_then_remove_sync(g, pos-1)

def less_efficient_topological_ordering(g):
    """ Computes the topological ordering of vertices in a acyclic directed
    graph.

    Follows the algorithm:
    1. select a sync vertex (no outgoing edges), if multiple pick one.
    2. remove it (and all it's incident edges) from the graph.
    3. recurse!

    Args:
        g: data structure encapsulating graphs.

    Returns:
        A list of all vertex names.
    """
    recurse_pick_then_remove_sync(g, len(g.get_vertices()))
    return g.values
