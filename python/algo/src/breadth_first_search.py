# -*- conding: utf-8 -*-

from collections import deque


def bfs(graph, start_vertex):
    """ Parses all vertices in the graph, using the breadth first search,
    which are reachable from start_vertex.

    Done in O(|V|+|E|) where |V| - cardinality of vertices set.
                             |E| - cardinality of edges set.
    Not so usefull for directed graphs.

    Args:
        start_vertex: the name of the start vertex.

    Returns:
        The list of visited vertexes.
    """

    queue = deque()
    queue.appendleft(start_vertex)
    explored_vertices = [start_vertex]

    while len(queue) != 0:
        vertex = queue.pop()
        neighbours = graph.neighbours(vertex)
        for neighbour in neighbours:
            if neighbour not in explored_vertices:
                explored_vertices.append(neighbour)
                queue.appendleft(neighbour)

    return explored_vertices
