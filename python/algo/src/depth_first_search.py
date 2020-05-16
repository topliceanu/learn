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

def dfs_explicit_stack(graph, start_vertex):
    """ Applies Depth-First Search algorithm without using recursion, ie. by
    using a explicig stack.

    Args:
        graph: object, instance of src.graph.Graph
        start_vertex: str, vertex to start the exploration from.
    """
    # stack maintains a list of vertices not yet visited.
    stack = [start_vertex]

    while len(stack) != 0:
        vertex = stack.pop()
        graph.set_vertex_value(vertex, VISITED)

        for neighbour in graph.neighbours(vertex):
            if graph.get_vertex_value(neighbour) != VISITED:
                stack.append(neighbour)

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
