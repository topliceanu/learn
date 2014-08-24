# -*- coding: utf-8 -*-


# Const marking when a node is visited or not.
VISITED = 1

def dfs(graph, start_vertex):
    """ Recursive algorithms to parse a directed graph. """
    graph.set_vertex_value(start_vertex, VISITED)

    for neighbour in graph.neighbours(start_vertex):
        if graph.get_vertex_value(neighbour) != VISITED:
            dfs(graph, neighbour)
