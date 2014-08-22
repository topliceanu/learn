import heapq

VISITED = 0x100
NOT_VISITED = 0x101

def shortest_path_heap(graph, start_vertex):
    """ Computes shortest path using a dijkstra algorithm and speeding it up
    using a heap data structure.
    """
    S = [start_vertex]
    A = {}
    A[start_vertex] = 0
    heap = [] # stores all vertices which are not yet in S with the 'dijkstra
              # greedy score' as the key.

    while True:
        frontier = get_frontier(graph, S)
        if len(frontier) == 0:
            break

        heap = push_frontier(graph, heap, frontier)
        (vertex, score) = heapq.heappop(heap)
        S.append(vertex)
        A[vertex] = score

    return A

def push_frontier(graph, heap, frontier):
    pass

def shortest_path_naive(graph, start_vertex):
    """ Computes single source shortest paths to every other vertex
    in a directed graph.

    Assumptions:
    - there is a directed path from start_vertex to any other
    vertex in the graph.
    - edge weights are non-negative.

    It's the naive implementation because it's not very fast O(n^2)
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
    """
    min_vertex = None
    min_length = 0
    for edge in frontier:
        (tail, head, value) = graph.split_edge(edge)
        if (distances[tail] + value < min_length) or (min_vertex is None):
            min_vertex = head
            min_length = distances[tail] + value
    return (min_vertex, min_length)
