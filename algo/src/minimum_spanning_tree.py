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


class EdgeHeap(Heap):
    """ A heap storing graph edges. Format of element: (key, edge). """

    def __init__(self):
        Heap.__init__(self)

    def compare(self, left, right):
        return cmp(left[0], right[0])


def prims_heap_mst(graph):
    """ Computes minimal spanning tree using a heap data structure to make
    things faster.

    The difference is that it sticks the frontier of the explored MST in a
    heap, as such always computing the min vertex is O(logm), where m is the
    number of edges.

    NOTE! This implementation assumes all vertex costs are distinct.

    Args:
        graph: object, data structure to hold the graph data.

    Returns:
        A Graph instance reperesenting the MST.
    """
    mst_vertices = []
    mst_edges = []
    INF = float('inf')

    edges = {index: edge for index, edge in enumerate(graph.get_edges())}
    frontier = Heap.heapify([(INF, e) for e in graph.get_edges()])

    vertex = random.choice(graph.get_vertices())
    mst_vertices.append(vertex)

    for e in graph.egress(vertex):
        index = frontier.data.index((float('inf'), e))
        frontier.remove(index)
        frontier.insert((e[2], e))

    while True:
        edge = frontier.get_min()
        [tail, head, cost] = graph.split_edge(edge)
        mst_vertices.append(head)
        mst_edges.append(edge)

        for e in graph.egress(head):
            index = frontier.data.index((float('inf'), e))
            frontier.remove(index)
            frontier.insert((e[2], e))

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
    mst_vertices = []
    mst_edges = []
    INF = float('inf')
    num_vertices = len(graph.get_vertices())

    frontier = EdgeHeap.heapify([(INF, v) for v in graph.get_vertices])
    vertex = random.choice(graph.get_vertices())

    while len(mst_vertices) != num_vertices:
        mst_vertices.append(vertex)

        for edge in graph.egress(vertex):
            [__, head, value] = graph.split_edge(edge)
            frontier.remove(head)


        vertex = frontier.get_min()

def kruskal_suboptimal_mst(graph):
    """ Computes the MST of a given graph using Kruskal's algorithm.

    Complexity is O(m*n) dominated by determining if adding a new edge
    creates a cycle which is O(n).

    Args:
        graph: object, data structure to hold the graph data.

    Returns:
        A Graph instance reperesenting the MST.
    """
    mst_vertices = []
    mst_edges = []
    edges = graph.get_edges()
    num_vertices = len(graph.get_vertices())

    edges = graph.get_edges()
    edges.sort(key=lambda e: e[2])

    index = 0
    while len(mst_vertices) != num_vertices:
        edge = edges[index]
        [tail, head, value] = graph.split_edge(edge)
        index += 1

        if tail in mst_vertices and head in mst_vertices:
            continue
        if tail not in mst_vertices:
            mst_vertices.append(tail)
        if head not in mst_vertices:
            mst_vertices.append(head)
        mst_edges.append(edge)

    mst = Graph.build(edges=mst_edges, directed=False)
    return mst
