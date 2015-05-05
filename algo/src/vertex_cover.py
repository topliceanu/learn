# -*- coding: utf-8 -*-

import random


def vertex_cover(g):
    """ Solves the vertex cover problem.

    Given a graph G=(E,V), find the subset S of V, such that every edge in E
    has at least one endpoint in S, S has the minimal cardinality amongst all
    possible solutions.

    Complexity: NP-complete (exponential time) O(m2^k)

    Params:
        g: object, instance of src.graph.Graph

    Returns:
        list, of vertices which compose the vertex cover.
    """
    min_solution = None
    for k in range(1, len(g.get_vertices())):
        local_solution = vertex_cover_bounded_num_edges(g.clone(), k)
        if local_solution == []:
            continue
        if min_solution == None:
            min_solution = local_solution
        if len(min_solution) > len(local_solution):
            min_solution = local_solution
    return min_solution

def vertex_cover_bounded_num_edges(g, k):
    """ This is a simplification of the previous problem, whereby we compute a
    vertex cover by choosing at most k edges. Ie. it is a reduction to a
    decision problem.

    Params:
        g: object, instance of src.graph.Graph
        k: int, the number of edges allowed to build the vertex cover.

    Returns:
        list, of vertices which compose the vertex cover. If the list is empty,
            this means there is no vertex set to cover all edges.
    """
    vertices = g.get_vertices()
    edges = g.get_edges()

    # Base cases:
    if len(vertices) == 0:
        return []
    if len(vertices) == 1:
        return vertices
    if len(edges) == 0:
        return vertices
    if k == 0:
        return [] # No vertex cover with 0 edges.
    if k == 1:
        # Brute-force to find a vertex cover containing one vertex.
        transport = {edges[0][0], edges[0][1]}
        for edge in edges[1:]:
            transport = transport.intersection({edge[0], edge[1]})
            if len(transport) == 0:
                return []
        return list(transport)

    (tail, head, __) = random.choice(edges)

    g_without_tail = g.clone()
    g_without_tail.remove_vertex(tail)
    tail_less_solution = vertex_cover_bounded_num_edges(g_without_tail, k-1)
    if len(tail_less_solution) != 0:
        tail_less_solution.append(tail)
        return tail_less_solution

    g_without_head = g.clone()
    g_without_head.remove_vertex(head)
    head_less_solution = vertex_cover_bounded_num_edges(g_without_head, k-1)
    if len(head_less_solution) != 0:
        head_less_solution.append(head)
        return head_less_solution

    return [] # No vertex cover
