# -*- coding: utf-8 -*-

from collections import deque

def bfs_shortest_path_distance(graph, start):
    """ Compute the length of the shortest path between start and end vertices
    given a graph.

    Works the same as classic BFS except that it keep track
    of how many hops there are from the start point to each vertex.

    Params:
        graph: a datastructure holding all vertices and edges.
        start: a vertex name to start the graph exploration from.

    Returns:
        The number of hops to get from start to each vertex in the graph.
    """
    explored_vertices = []
    explored_vertices.append(start)
    queue = deque()
    queue.append(start)
    graph.set_vertex_value(start, 0)

    while len(queue) != 0:
        vertex = queue.pop()
        vertex_level = graph.get_vertex_value(vertex)
        for neighbour in graph.neighbours(vertex):
            if neighbour not in explored_vertices:
                explored_vertices.append(neighbour)
                queue.append(neighbour)
                graph.set_vertex_value(neighbour, vertex_level + 1)

    return graph
