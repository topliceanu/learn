# -*- coding: utf-8 -*-

from src.graph import Graph
from src.dijkstra_shortest_path import VertexHeap


def a_star_shortest_path(graph, source, destination):
    """ Finds the least-cost path from source to destination vertices.

    Note: this is not the same as the single source shortest path problem.

    Args:
        graph: object, instance of src.graph.Graph
        source: str, the key of the source vertex
        destination: str, the key of the destination vertex

    Returns:
        tuple, format is (path, cost)
            cost: dict, format {vertex: shortest_path_cost}
            path: dict, format {vertex: source_vertex}
    """
    frontier = VertexHeap()
    frontier.insert((source, 0))
    came_from = {}
    cost_so_far = {}
    came_from[source] = None
    cost_so_far[source] = 0

    while len(frontier) != 0:
        (current_vertex, vertex_cost) = current.extract_min()

        if current_vertex == destination:
            break

        for edge in graph.egress(current_vertex):
            (__, next_vertex, next_cost) = graph.split_edge(edge)
            new_cost = cost_so_far[current_vertex] + next_cost
            if next_vertex not in cost_so_far or new_cost < cost_so_far[next_vertex]:
                cost_so_far[next_vertex] = new_cost
                priority = new_cost + heuristic(goal, next_vertex)
                frontier.insert((next_vertex, priority))
                came_from[next_vertex] = current_vertex

    return (came_from, cost_so_far)
