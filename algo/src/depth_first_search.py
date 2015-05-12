# -*- coding: utf-8 -*-


# Const marking when a node is visited or not.
VISITED = 1

def dfs(graph, start_vertex):
    """ Recursive algorithms to parse a directed graph.

    Args:
        graph: object, instance of src.graph.Graph
        start_vertex: str, vertex to start the exploration from.
    """
    graph.set_vertex_value(start_vertex, VISITED)

    for neighbour in graph.neighbours(start_vertex):
        if graph.get_vertex_value(neighbour) != VISITED:
            dfs(graph, neighbour)

def dfs_paths(graph, start, end):
    """ Returns all possible paths from start to end vertices in a directed graph.

    See: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    for explanation on how to better implement BFS and DFS in python.

    Args:
        graph: object, instance of src.graph.Graph
        start: str, the vertex to start from.
        end: str, the vertex to end with.

    Returns:
        list, of paths from start to end, format [[vertex]]
    """
    #import pdb; pdb.set_trace()
    paths = []
    stack = [(start, [start])]

    while len(stack) != 0:
        (vertex, path) = stack.pop()

        for neighbour in graph.neighbours(vertex):
            p = path[:]
            if neighbour in p:
                continue
            p.append(neighbour)

            if neighbour == end:
                paths.append(p[:])
            else:
                stack.append((neighbour, p[:]))

    return paths
