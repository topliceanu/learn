# -*- coding: utf8 -*-

import random
from operator import itemgetter

from src.graph import Graph
from src.heap import Heap


def prims_suboptimal_mst(graph):
    """ Computes minimum spanning tree using the Prim's algorithm.

    Running time O(n*m), where n is the num of vertices and m the num of edges.
    A greedy routine wereby we enlarge the set of explored vertices by always
    adding the edge on the frontier with the least cost.

    Args:
        graph: object, undirected graph where each edge has an associated cost
            (which can be negative).

    Returns:
        A subgraph tree of minimal cost. ie. a connected subgraph with no
        cycles and whose sum of all edges is minimal.
    """
    mst_vertices = []
    mst_edges = []

    start_vertex = random.choice(graph.get_vertices())
    mst_vertices.append(start_vertex)

    while len(mst_vertices) != len(graph.get_vertices()):

        min_value = float('inf')
        min_edge = None
        min_vertex = None
        for edge in graph.get_edges():
            [tail, head, value] = graph.split_edge(edge)
            if ((tail in mst_vertices and head not in mst_vertices) or \
              (head in mst_vertices and tail not in mst_vertices)) and \
              (value < min_value):
                min_value = value
                min_edge = edge
                if tail not in mst_vertices:
                    min_vertex = tail
                else:
                    min_vertex = head

        mst_vertices.append(min_vertex)
        mst_edges.append(min_edge)

    mst = Graph.build(edges=mst_edges, directed=False)
    return mst

def prims_heap_mst(graph):
    """ Computes minimal spanning tree using a heap data structure to make
    things faster.

    The difference is that it sticks the frontier of the explored MST in a
    heap, as such always computing the min vertex is O(logm), where m is the
    number of edges.

    TODO this implementation is broken.

    Args:
        graph: object, data structure to hold the graph data.

    Returns:
        A Graph instance reperesenting the MST.
    """
    mst_vertices = []
    mst_edges = []

    start_vertex = random.choice(graph.get_vertices())
    mst_vertices.append(start_vertex)

    cost_edge = {edge[2]: edge for edge in graph.get_edges()}
    edge_cost = {edge: edge[2] for edge in graph.get_edges()}

    values = map(itemgetter(2), graph.egress(start_vertex))
    frontier = Heap.heapify(values)

    while len(mst_vertices) != len(graph.get_vertices()):
        min_cost_edge = frontier.extract_min()
        edge = cost_edge[min_cost_edge]

        if edge[0] not in mst_vertices:
            other_vertex = edge[0]
        if edge[1] not in mst_vertices:
            other_vertex = edge[1]

        mst_vertices.append(other_vertex)
        mst_edges.append(edge)

        # Insert outgoing edges.
        edges = graph.egress(other_vertex)
        for edge in edges:
            if edge[1] not in mst_vertices:
                frontier.insert(edge[2])

        # Remove ingoing edges whose vertices are already in the mst.
        edges = graph.ingress(other_vertex)
        for edge in edges:
            if edge[0] in mst_vertices:
                frontier.remove(edge[2])

    mst = Graph.build(edges=mst_edges, directed=False)
    return mst

def prims_fast_heap_mst(graph):
    """ Computes a mst from the given graph using prims algorithm and a heap.

    The heap is used to store the vertices not the edges as in the previous
    implementation. The heap maintains two invariants:
    1. elements in the heap are vertices not yet explored
    2. keys under which each vertex is stored in the heap is the minimum weight
    of an edge incided to the vertex whose tail is already in the MST.

    Args:
        graph: object, data structure to hold the graph data.

    Returns:
        A Graph instance reperesenting the MST.
    """
