# -*- coding: utf8 -*-

import random
from operator import itemgetter

from src.breadth_first_search import bfs
from src.graph import Graph
from src.heap import Heap
from src.union_find import UnionFind


def prims_suboptimal_mst(graph):
    """ Computes minimum spanning tree using the Prim's algorithm.

    Running time: O(n*m), where n is the num of vertices and m the num of edges.

    A greedy routine wereby we enlarge the set of explored vertices by always
    adding the edge on the frontier with the least cost.

    Discovered in 1957 by Robert Prim, 1959 by Edsger Dijkstra, 1930 by Iarnik.

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

class VertexHeap(Heap):
    """ A heap to store vertices ordered by their cost.

    This heap maintains two invariants:
    1. elements in heap are vertexes with format (vertex, cost) which are part
    of the frontier, ie. the unexplored section of the graph.
    2. Each vertex has as cost the min of all Dijkstra greedy scores for edges
    incident in vertex.
    """

    def __init__(self, data=None):
        Heap.__init__(self, data)

    def compare(self, left, right):
        """ Overrides to support vertices in format (vertex, cost). """
        return cmp(left[1], right[1])

    def remove(self, vertex):
        """ Overrides parent method to remove a vertex by it's vertex name,
        not cost.

        Args
            vertex: str, name of the vertex to remove.
        """
        index = map(itemgetter(0), self.data).index(vertex)
        return Heap.remove(self, index)

def prims_heap_mst(graph):
    """ Computes minimal spanning tree using a heap data structure to store
    unexplored vertices.

    The difference is that it maintains the frontier of the explored MST in a
    heap, as such always computing the min vertex in O(logm), where m is the
    number of edges.

    The heap is used to store the vertices not the edges as in the previous
    implementation. The heap maintains two invariants:
    1. elements in the heap are vertices not yet explored
    2. keys under which each vertex is stored in the heap is the minimum weight
    of an edge incident on the vertex whose tail is already in the MST.

    Complexity: O(m*log n), m - number of edges, n - number of vertices

    Args:
        graph: object, data structure to hold the graph data.

    Returns:
        A Graph instance reperesenting the MST.
    """
    mst_vertices = []
    mst_edges = []
    INF = float('inf')
    vertices = graph.get_vertices()
    num_vertices = len(vertices)

    frontier = VertexHeap.heapify([(v, INF) for v in vertices])
    vertex = random.choice(graph.get_vertices())
    frontier.remove(vertex)

    # This dict stores for each vertex the neighbour with the smallest edge,
    # and the edge cost. Format {vertex: (incident_vertex, edge_cost)}
    vertices = {}

    while vertex:
        mst_vertices.append(vertex)
        if len(mst_vertices) == num_vertices:
            break

        for edge in graph.egress(vertex):
            [__, head, cost] = graph.split_edge(edge)
            if head not in mst_vertices:
                [__, head_key] = frontier.remove(head)
                min_cost = min(cost, head_key)
                frontier.insert((head, min_cost))
                if min_cost < head_key:
                    vertices[head] = (vertex, cost)

        # Extract the vertex with min cost and compute it's associated min edge.
        (head, __) = frontier.extract_min()
        (tail, cost) = vertices[head]
        mst_edges.append((tail, head, cost))
        vertex = head

    mst = Graph.build(edges=mst_edges, directed=False)
    return mst

def kruskal_suboptimal_mst(graph):
    """ Computes the MST of a given graph using Kruskal's algorithm.

    Complexity: O(m*n) - it's dominated by determining if adding a new edge
    creates a cycle which is O(n). This implementation does not use union-find.

    This algorithm also works for directed graphs.

    Discovered in 1956 by Joseph Kruskal.

    Args:
        graph: object, data structure to hold the graph data.

    Returns:
        A Graph instance reperesenting the MST.
    """
    mst_edges = []
    edges = graph.get_edges()
    num_vertices = len(graph.get_vertices())

    edges = graph.get_edges()
    edges.sort(key=lambda e: e[2]) # sort edges asc by length.

    index = 0
    mst = Graph.build(edges=[], directed=False)
    while index < num_vertices:
        edge = edges[index]
        index += 1

        # Make sure the picked edge does not create a cycle in the existing MST.
        [tail, head, __] = graph.split_edge(edge)
        explored = bfs(mst, tail)
        if head not in explored:
            mst.add_edge(edge)

    return mst

def kruskal_union_find_mst(graph):
    """ Uses Kruskel's greedy algorithm to compute the MST of graph.

    Running time: O(m*log n) - where m is the number of edges and n is the
        number of vertices.

    Params:
        graph: object, instance of src.graph.Graph

    Returns:
        object, src.graph.Graph instance reperesenting the MST.
    """
    mst_edges = []
    edges = graph.get_edges()
    num_vertices = len(graph.get_vertices())

    edges = graph.get_edges()
    edges.sort(key=lambda e: e[2])

    union_find = UnionFind()

    index = 0
    while index < num_vertices:
        edge = edges[index]
        [tail, head, value] = graph.split_edge(edge)
        index += 1

        if union_find.find(head) == union_find.find(tail):
            continue
        else:
            union_find.union(head, tail)
        mst_edges.append(edge)

    mst = Graph.build(edges=mst_edges, directed=False)
    return mst

def minimum_spanning_tree_randomized(graph):
    """ Computes the minimum spanning tree using a randomized approach.

    Complexity: O(m*alpha(n)) - where m - number of edges, n - number of vertices.

    Created by: Karger, Klein and Tarjan in 1995.
    """
    # TODO

def minimum_spanning_bottleneck_tree(graph):
    """ A minimum spanning bottleneck tree is a subgraph of a connected,
    undirected graph which connects all vertices in the graph but minimizes
    the maximum picked edge costs.
    """
    # TODO
