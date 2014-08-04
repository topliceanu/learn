# -*- coding: utf-8 -*-

from collections import deque

def bfs_shortest_path_distance(graph, start, end):
    """ Compute the length of the shortest path between start and end vertices
    given a graph.

    Params:
        graph - a datastructure holding all vertices and edges.
        start - a vertext name
        end - a vertext name
    Returns the number of hops to get from start to end vertices.
    """
    if start == end:
        return 0

    # Data structure to keep the layer for each node.
    layers = {}

    explored_vertices = []
    queue = deque()
    queue.appendleft(start)
    layers[start] = 0

    while len(queue) != 0:
        v = queue.pop()
        for s in graph.neighbors(v):
            if s not in explored_vertices:
                explored_vertices.append(s)
                layers[s] = layers[v]+1
                queue.appendleft(s)

    return layers[end]
