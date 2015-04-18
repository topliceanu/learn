# -*- conding: utf-8 -*-

from src.graph import Graph


def shortest_path(graph, s, return_paths=True):
    """ Implement the single source shortest path problem using the bellman-ford
    algorithm.

    This is usefull for graphs that may have edges with negative length.
    Also, this algorithm is highly distributed-able.

    TODO: memory optimization, notice that bellman-ford only uses the results
    from the last iteration, so everything else can be thrown out.
    TODO: implement solution reconstruction using the memory optimizations.

    Complexity: O(m*n), where m is the number of edges, n the number of nodes.

    Params:
        graph: object, instance of src.graph.Graph, structure representing a graph.
        s: int, the key of the starting vertex in the graph.
        return_paths: bool, returns the shortest paths also.

    Returns:
        tuple, format (costs, paths)
            costs: dict, format {destination_vertex: cost_to_that_vertex}
            paths: dict, format {destination_vertex: [edges_to_that_vertex]}
                Only available if returns_paths=True, otherwise is an empty dict.
    """
    # 0. Initialization:
    # A[i][v] - cost of shortest path from start vertex s to v using at most
    # i edges in the path. (i has values from 0 to n edges)
    # B[i][v] - holds the second to last vertex on the shortest path from s to
    # v with at most i edges OR None if no such path exists.
    # We only need the last two rows or A and the last row of B.
    vertices = graph.get_vertices()
    n = len(vertices)
    #A = [[0] * n for __ in range(n+1)]
    #B = [[None] * n for __ in range(n+1)]
    A = [[0] * n for __ in range(2)]
    B = [None] * n

    # s - the name of the vertex s; pos_s - the position of vertex in the list.
    pos_s = vertices.index(s)

    # 1. Base case: if v == s then total cost is 0;
    # if allowed num edges is 0 then there are no shortest paths.
    for pos_v in range(n):
        if pos_v != pos_s:
            A[0][pos_v] = float('inf')
        else:
            A[0][pos_v] = 0

    # 2. Recurse for every combination of end vertex v and max num of allowed
    # edges is i. The min path is either obtained with one less vertex, or
    # it is the minimum of all paths to all the vertices w incident to v plus
    # the value of the edge (w,v). Formally:
    #
    # L(i,v) = min( L(i-1,v), min {L(i-1,w)+c(v,w)} )
    #                        (w,v)
    for i in range(1, n+1):
        if i > 1:
            # Move the last computed row of path costs for the next computation.
            A[0] = A[1]
            A[1] = [0] * n
        for pos_v in range(n):
            v = vertices[pos_v]
            # If there are no shortest paths from s to v (perhaps because
            # there are too few vertices allowed), we set the value to INF.
            min_case_two = float('inf')
            min_pos_w = None
            for w in graph.incident(v):
                pos_w = vertices.index(w)
                #tmp = A[i-1][pos_w] + graph.get_edge_value((w, v))
                tmp = A[0][pos_w] + graph.get_edge_value((w, v))
                if tmp < min_case_two:
                    min_case_two = tmp
                    min_pos_w = pos_w
            #min_case_one = A[i-1][pos_v]
            min_case_one = A[0][pos_v]

            #A[i][pos_v] = min(min_case_one, min_case_two)
            A[1][pos_v] = min(min_case_one, min_case_two)
            B[pos_v] = min_pos_w

        # Optimization: when the two successive rows of computed min path costs
        # are the same, then we can stop sooner.
        #if i < n and A[0] == A[1]:
        #    break

    # 3. Detect negative cycles by running the algorithm for i > n-1 and
    # checking if the shortest paths change value.
    #if A[n-1] != A[n]:
    if A[0] != A[1]:
        return False # graph has cycles with negative cost.
    else:
        costs = dict(zip(vertices, A[0]))

    # 4. Compute the paths as well from each vertex to every other vertex,
    # by using the B 2d array.
    paths = {}
    if return_paths is True:
        def rec_path(i):
            if B[i] in [None, pos_s]:
                return []
            rest = rec_path(B[i])
            rest.append(vertices[B[i]])
            return rest
        paths = {v: rec_path(i) for i, v in enumerate(vertices)}

    # 5. Return solution.
    return (costs, paths)
