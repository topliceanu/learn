# -*- conding: utf-8 -*-

from src.graph import Graph


def shortest_path(graph, s):
    """ Implement the single source shortest path problem using the bellman-ford
    algorithm.

    This is usefull for graphs that may have edges with negative length.
    Also, this algorithm is highly distributed.

    TODO: memory optimization, notice that bellman-ford only uses the results
    from the last iteration, so everything else can be thrown out.
    TODO: implement solution reconstruction using the memory optimizations.

    Complexity: O(m*n)

    Params:
        graph: object, instance of src.graph.Graph, structure representing a graph.
        s, int, the key of the starting vertex in the graph.

    Returns:
        A dict containing all vertices in the graph as keys and the shortest
            paths values to that vertex from s.

        OR a list of edges which make up a negative length cycle.
    """
    # 0. Initialization:
    # A[i][v] - cost of shortest path from s to v using at most i edges in the path.
    vertices = graph.get_vertices()
    n = len(vertices)
    A = [[0]*n for __ in range(n+1)]
    # s - the name of the vertex s; pos_s - the position of vertex in the list.
    pos_s = vertices.index(s)

    # 1. Base case: if v == s then total cost is 0,
    # if allowed num edges is 0 then there are no shortest paths.
    for pos_v in range(n):
        if pos_v != pos_s:
            A[0][pos_v] = float('inf')
        else:
            A[0][pos_v] = 0

    # 2. Recurse for every combination of end vertex v and max num of edges is i.
    for i in range(1, n+1):
        for pos_v in range(n):
            v = vertices[pos_v]
            min_case_two = float('inf')
            for w in graph.incident(v):
                pos_w = vertices.index(w)
                tmp = A[i-1][pos_w] + graph.get_edge_value((w, v))
                if tmp < min_case_two:
                    min_case_two = tmp
            A[i][pos_v] = min(A[i-1][pos_v], min_case_two)

        # Optimization: if no progress is made at this step then we can stop recursing.
        #if A[i] == A[i-1] and i <= n:
        #    break

    # Shortest path costs from s to all vertices v:
    paths = dict(zip(vertices, A[n-1]))

    # 3. Detect negative cycles by running the algorithm for i > n-1 and
    # checking if the shortest paths change value.
    if A[n-1] == A[n]:
        return paths
    else:
        return False # There exist negative length cycles.
