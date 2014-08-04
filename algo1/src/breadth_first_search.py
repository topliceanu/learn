from collections import deque

import graph.py


def bfs(graph, start_vertex):
    """ Parses all the graph using the breadth first search.

    Returns:
    The list of visited vertexes.
    """

    queue = deque()
    queue.append(start_vertex)
    explored_vertices = []

    while len(queue) == 0:
        v = queue.pop()
        edges = graph.edges_from(v)
        for edge in edges:
            if edge[1] not in explored_vertices:
                explored_vertices.append(edge[1])
                queue.appendleft(edge[1])

    return explored_vertices
