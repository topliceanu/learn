# -*- coding: utf-8 -*-

from operator import itemgetter
from src.heap import Heap

VISITED = 0x100
NOT_VISITED = 0x101


class VertexHeap(Heap):
    """ Stores vertexes in a heap.

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
        """ Overrides parent method to remove a vertex by it's vertex not cost.

        Args
            vertex: str, name of the vertex to remove.
        """
        index = map(itemgetter(0), self.data).index(vertex)
        return Heap.remove(self, index)

def shortest_path_heap(graph, start_vertex):
    """ Computes shortest path using a dijkstra algorithm and speeding it up
    using a heap data structure.

    Note! The reason dijkstra doesn't work with negative-length edges is
    because the algorithm may take the negative edges in considerations
    multiple times (ie. a cycle) in an effort to decrease the dijkstra score.

    Args:
        graph: data structure exposing graph operations.
        start_vertex: name of the vertex to start exploring

    Returns:
        A dict containing all vertices in the graph as keys and minimum cost
            to get there from start_vertex.
    """
    INF = float('inf')
    S = [] # List of vertices processed so far.
    A = {} # Computed shortes paths distances for every node
           # in the graph. Format: {vertex: path_length}

    # Initially all vertices have an INF cost.
    frontier = VertexHeap.heapify([(v, INF) for v in graph.get_vertices()])
    frontier.remove(start_vertex)

    vertex = (start_vertex, 0)
    while vertex:
        S.append(vertex[0])
        A[vertex[0]] = vertex[1]

        if len(S) == len(graph.get_vertices()):
            break

        for head in graph.get_vertices():
            if head not in S:
                # For each vertex not in S compute greedy
                # score of all inbound vertices.
                dijkstra_greedy_score = INF
                for edge in graph.ingress(head):
                    [tail, __, cost] = graph.split_edge(edge)
                    if tail in S:
                        if dijkstra_greedy_score > cost + A[tail]:
                            dijkstra_greedy_score = cost + A[tail]
                # Store that back into the heap.
                if dijkstra_greedy_score != INF:
                    frontier.remove(head)
                    frontier.insert((head, dijkstra_greedy_score))

        # Compute the next vertex to add
        vertex = frontier.extract_min()

    return A

def push_frontier(graph, heap, frontier):
    pass

def shortest_path_naive(graph, start_vertex):
    """ Computes single source shortest paths to every other vertex
    in a directed graph starting from the start_vertex.

    Assumptions:
    - there is a directed path from start_vertex to any other
    vertex in the graph. If there isn't, a value of inf is returned.
    - edge weights are non-negative!

    Note! The reason dijkstra doesn't work with negative-length edges is
    because the algorithm may take the negative edges in considerations
    multiple times (ie. a cycle) in an effort to decrease the dijkstra score.

    Note: It's the naive implementation because it's not very fast, ie. O(n^2).

    Args:
        graph: data structure exposing graph operations.
        start_vertex: name of the vertex to start exploring

    Returns:
        A dict containing all vertices in the graph as keys and the smallest
        number of hops to get there from start_vertex.
    """
    S = [start_vertex] # List of vertices processed so far.
                       # By default the start vertex is the first computed.
    A = {} # Computed shortes paths distances for every node in the graph.
           # Format: {vertex: path_length}
    A[start_vertex] = 0 # Path to itself is 0.
    B = {} # Stores actual shortest path vertices for each node in graph.
           # Format: {vertex: [list_of_vertices]}
           # TODO implement B functionality

    while True:
        frontier = get_frontier(graph, S)
        if len(frontier) == 0:
            break

        (vertex, min_length) = pick_min_path(graph, A, frontier)
        S.append(vertex)
        A[vertex] = min_length # We always compute shortest path length
                               # to any vertex in S.
    return A

def get_frontier(graph, explored_vertices):
    """ Computes the edges on the frontier of graph given
    the already explored vertices, ie. the edges where the tail was explored
    and the head was not yet explored.

    Args:
        graph: data structure holding graph data.
        explored_vertices: a list of vertex names

    Returns:
        A list of tuples representing vertices (tail, head, value).
    """
    frontier = set()
    for vertex in explored_vertices:
        for other in graph.neighbours(vertex):
            if other not in explored_vertices:
                value = graph.get_edge_value((vertex, other))
                frontier.add((vertex, other, value))
    return frontier

def pick_min_path(graph, distances, frontier):
    """ Implements Dijkstra's greedy criterion: ie. find the vertex to add to
    the explored set so that it minimizes the path it creates.

    Args:
        graph: data structure containg graph data and operations.
        distances: dict of so far explored vertices and the min number of hops
            to reach them.
        frontier: a list of tuples representing vertices (tail, head, value)
            where the head vertex was not explored.
    """
    min_vertex = None
    min_length = 0
    for edge in frontier:
        (tail, head, value) = graph.split_edge(edge)
        if (distances[tail] + value < min_length) or (min_vertex is None):
            min_vertex = head
            min_length = distances[tail] + value
    return (min_vertex, min_length)
