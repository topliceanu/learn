# -*- coding: utf-8 -*-

import random


VISITED = 0x100
NOT_VISITED = 0x101

def scc(g):
    """ Computes strongly connected components of a acyclic directed graph.

    Uses the Rao Kosaraju two-pass algorithm, with the following steps:
    1. reverse all the edges in a graph.
    2. run DFS on the reverse graph to compute finishing times for each
       vertex ie. an ordering of the vertices.
    3. run DFS on the normal graph in reverse order of finisihing times.

    Args:
        g: instance of src.graph.Graph, a data structure encapsulating graphs.
    """
    global t
    global finishing_time
    global s
    global leader

    t = 0
    finishing_time = {}
    s = None
    leader = {}

    # Reset visited value of each vertex.
    for vertex in g.get_vertices():
        g.set_vertex_value(vertex, NOT_VISITED)

    ordering = dfs_compute_ordering(g)

    # Reset visited value of each vertex.
    for vertex in g.get_vertices():
        g.set_vertex_value(vertex, NOT_VISITED)

    connected_components = dfs_discover_connected_components(g, ordering)
    return connected_components

def dfs_compute_ordering(g):
    """ First pass of Rao Kosaraju's algorithm. """
    vertices = g.get_vertices()
    global t
    global finishing_time
    t = 0 # number of nodes finishes exploring so far.
    finishing_time = {} # Stores the finishing time for each node.
                        # Format {vertex: finishing_time}

    # 1. shuffle node ordering for running dfs.
    tmp = range(len(vertices))
    ordering = range(len(vertices))
    random.shuffle(ordering)
    for index, order in enumerate(ordering):
        tmp[order] = vertices[index]
    vertices = tmp

    # 2. custom dfs to keep count of a vertex's finishing time and to
    # traverse the graph in reverse order of it's edges.
    def first_dfs(g, start):
        global t
        global finishing_time
        g.set_vertex_value(start, VISITED)
        for neighbour in g.incident(start):
            if g.get_vertex_value(neighbour) != VISITED:
                first_dfs(g, neighbour)
        t += 1
        finishing_time[start] = t

    # 3. compute finishing times for each node by iterating in decreasing order.
    for vertex in reversed(vertices):
        if g.get_vertex_value(vertex) != VISITED:
            first_dfs(g, vertex)

    # 4. Process the results to get a list of vertex orderings.
    out = range(len(vertices))
    for vertex, f in finishing_time.iteritems():
        out[f-1] = vertex

    return out

def dfs_discover_connected_components(g, vertices_ordering):
    """ The second pass through the graph in Kosaraju's algorithm. """
    global s
    global leader
    s = None # Stores the leader of the current node: the most recent vertex
             # from which a DFS was initiated.
    leader = {} # Stores the leader for each node. Format {vertex: leader}

    # 1. Custom dfs to keep track of the leader of each vertex.
    def second_dfs(g, start):
        global leader
        g.set_vertex_value(start, VISITED)
        leader[start] = s
        for neighbour in g.neighbours(start):
            if g.get_vertex_value(neighbour) != VISITED:
                second_dfs(g, neighbour)

    # 2. Go through each node in decreasing finishing time to discover sccs.
    for vertex in reversed(vertices_ordering):
        if g.get_vertex_value(vertex) != VISITED:
            s = vertex
            second_dfs(g, vertex)

    # 3. Process the leader dict to determine the sccs.
    components = set(leader.values())
    out = {}
    for vertex, component in leader.iteritems():
        if component not in out:
            out[component] = []
        out[component].append(vertex)
    return out.values()
