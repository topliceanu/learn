from collections import deque


def bfs(graph, start_vertex):
    """ Parses all the graph using the breadth first search.
    Done in O(|V|+|E|) where n - number of vertices, m - number of edges
    Not so usefull for directed graphs.

    Returns:
    The list of visited vertexes.
    """

    queue = deque()
    queue.appendleft(start_vertex)
    explored_vertices = []
    explored_vertices.append(start_vertex)

    while len(queue) != 0:
        vertex = queue.pop()
        neighbours = graph.neighbours(vertex)
        for neighbour in neighbours:
            if neighbour not in explored_vertices:
                explored_vertices.append(neighbour)
                queue.appendleft(neighbour)

    return explored_vertices
