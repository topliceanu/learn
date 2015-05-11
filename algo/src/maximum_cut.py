# -*- coding: utf-8 -*-

from collections import deque
import random

from src.graph import Graph


def maximum_cut_for_bipartite_graph(g):
    """ Solved the maximum cut problem in a bipartite graph.

    A bipartite graph is a graph where there exists a cut which crosses all
    edges in the graph.

    Complexity: O(m+n) - each vertex is visited only once.

    Params:
        g: object, instance of src.graph.Graph

    Returns
        tuple, format (left_vertex_set, right_vertex_set)
            left_vertex_set: list, of vertices composing the left side of the cut.
            right_vertex_set: list, of vertices composing the right side of the cut.
    """
    # Use BFS to traverse all edges, even if graph is not connected.

    #import pdb; pdb.set_trace()
    odds = set()
    evens = set()
    left_to_visit = set(g.get_vertices())

    while len(left_to_visit) != 0:
        start_vertex = random.choice(list(left_to_visit))
        odds.add(start_vertex)
        left_to_visit.remove(start_vertex)
        queue = deque([start_vertex])
        g.set_vertex_value(start_vertex, False)

        while len(queue) != 0:
            vertex = queue.pop()
            # Boolean representing whether the vertex is in an odd or even layer.
            parent_is_even = g.get_vertex_value(vertex)
            if parent_is_even:
                bucket = odds
            else:
                bucket = evens
            for neighbour in g.neighbours(vertex):
                if neighbour not in left_to_visit:
                    continue
                left_to_visit.remove(neighbour)
                bucket.add(neighbour)
                g.set_vertex_value(neighbour, not parent_is_even)
                queue.appendleft(neighbour)


    return (odds, evens)

def maximum_cut(g):
    """ Solves the maximum cut problem using the local search algorithm with
    probability of success of 50%.

    This problem is NP-complete for the general case.

    Complexity: O(N^2) because we're using the local search heuristic.

    Params:
        g: object, instance of src.graph.Graph

    Returns
        tuple, format (left_vertex_set, right_vertex_set)
            left_vertex_set: list, of vertices composing the left side of the cut.
            right_vertex_set: list, of vertices composing the right side of the cut.
    """
    # 1. Randomly pick a vertex to split the set into two lists.
    vertices = g.get_vertices()
    split_point = random.randint(0, len(vertices)-1)
    left = vertices[:split_point]
    right = vertices[split_point:]

    # 2. Start searching for a better solution using local search.
    while True:
        possible_switches = []
        for v in vertices:
            # number of edges incident on v that _don't_ cross the cut (A,B)
            dv = 0
            # number of edges incident on v that _do_ cross the cut (A, B)
            cv = 0

            v_in_left = v in left
            for i in g.incident(v):
                i_in_left = i in left
                if i_in_left and v_in_left:
                    dv += 1
                elif i_in_left and not v_in_left:
                    cv += 1
                elif not i_in_left and v_in_left:
                    cv += 1
                elif not i_in_left and not v_in_left:
                    dv += 1
            if dv > cv:
                possible_switches.append(v)
        if len(possible_switches) == 0:
            break
        else:
            # The reason whey we pick a candidate v at random and not the v
            # that maximizes Cv and Dv is to avoid local optimum.
            v = random.choice(possible_switches)
            if v in left:
                left.remove(v)
                right.append(v)
            else:
                right.remove(v)
                left.append(v)

    return (left, right)

def weighted_maximum_cut(g):
    """ Weighted version of maximum cut problem solution using local search.
    Each edge has a weight, we need to find the cut which maximizes the total
    sum of the edges crossed by the cut.

    Complexity: O(exp(n))

    Params:
        g: object, instance of src.graph.Graph, represents an undirected
            weighted graph.

    Returns
        tuple, format (left_vertex_set, right_vertex_set)
            left_vertex_set: list, of vertices composing the left side of the cut.
            right_vertex_set: list, of vertices composing the right side of the cut.
    """
    # 1. Randomly pick a point where to split the set into two lists.
    vertices = g.get_vertices()
    split_point = random.randint(0, len(vertices)-1)
    left = vertices[:split_point]
    right = vertices[split_point:]

    # 2. Start searching for a better solution using local search.
    while True:
        possible_switches = []
        for v in vertices:
            # Cost of edges incident on v that _don't_ cross the cut (A,B)
            cost_dv = 0
            # Cost of edges incident on v that _do_ cross the cut (A, B)
            cost_cv = 0

            v_in_left = v in left
            for i in g.incident(v):
                i_in_left = i in left
                if i_in_left and v_in_left:
                    cost_dv += g.get_edge_value((v, i))
                elif i_in_left and not v_in_left:
                    cost_cv += g.get_edge_value((v, i))
                elif not i_in_left and v_in_left:
                    cost_cv += g.get_edge_value((v, i))
                elif not i_in_left and not v_in_left:
                    cost_dv += g.get_edge_value((v, i))
            if cost_dv > cost_cv:
                possible_switches.append(v)
        if len(possible_switches) == 0:
            break
        else:
            # The reason whey we pick a candidate v at random and not the v
            # that maximizes Cv and Dv is to avoid local optimum.
            v = random.choice(possible_switches)
            if v in left:
                left.remove(v)
                right.append(v)
            else:
                right.remove(v)
                left.append(v)

    return (left, right)
