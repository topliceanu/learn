# -*- conding: utf-8 -*-

import itertools


def traveling_salesman(g):
    """ Solve the traveling salesman problem faster than brute force search.

    This gets solved by dynamic programming. The subproblems L[S][j] is the
    shortest path from vertex 1 to vertex j with where the visited vertex are
    in the set S (S includes 1 and j).

    Complexity: O((n^2)*(2^n)) far better than brute force O(n!)

    Args:
        g: object, instance of src.graph.Graph class.
            We assume that this graph is complete and undirected.

    Returns:
        min_cost - the min cost of the cycle visiting all vertices.
    """

    # 0. Initialization:
    A = {}
    S = tuple(sorted(g.get_vertices()))
    n = len(S)
    first_vertex = S[0]
    S_without_first = tuple(i for i in S if i != first_vertex)

    def get_nested(A, t, i):
        """ Returns A[t][i] where t is a tuple containing the last i-1 vertices
        and i is the last vertex.
        """
        if t not in A:
            A[t] = {}
        if i not in A[t]:
            if i == first_vertex:
                if t == tuple(first_vertex):
                    A[t][i] = 0
                else:
                    A[t][i] = float('inf')
        return A[t][i]

    def set_nested(A, t, i, value):
        """ Sets the value of A for vertices tuple t and last vertex i. """
        if t not in A:
            A[t] = {}
        A[t][i] = value

    def clear_level(A, m):
        if m <= 0:
            return
        for t in itertools.combinations(S, m):
            if t in A:
                del A[t]

    # 1. Corresponding Recurrence:
    # A[S][j] - minimum length of a path from first_vertex to vertex j that
    # visits precisely the vertices in S, exactly once each:
    # A[S][j] =   min   (A[S-{k}][k] + c[k][j] , where S - set of vertices
    #           k in S                         , where j,k - vertices
    #           k != j
    for m in range(1, n): # number of vertices in the path.
        for s in itertools.combinations(S_without_first, m): # all vertex combinations of size m.
            s = list(s)
            s.insert(0, first_vertex)
            s = tuple(sorted(s))
            for j in s:
                if j == first_vertex:
                    continue
                s_without_j = tuple(sorted(x for x in s if x != j))

                min_cost = float('inf')
                for k in s:
                    if k == j:
                        continue

                    tmp_cost = get_nested(A, s_without_j, k) + g.get_edge_value((k,j))
                    if min_cost > tmp_cost:
                        min_cost = tmp_cost
                set_nested(A, s, j, min_cost)
        clear_level(A, m-1)

    # 2. Compute the optimal solution: the min path from start vertex to any
    # other vertex traversing all other vertices only once. To that we add the
    # final hop back to first vertex.
    min_cost = float('inf')
    min_path = ()
    for vertex in S:
        if vertex == first_vertex:
            continue
        tmp_cost = get_nested(A, S, vertex) + g.get_edge_value((vertex, first_vertex))
        if tmp_cost < min_cost:
            min_cost = tmp_cost

    # 3. Return the final solution.
    # TODO compute the min path as well.
    return (min_cost, min_path)
