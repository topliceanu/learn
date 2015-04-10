# -*- conding: utf-8 -*-

import itertools


def traveling_salesman(g):
    """ Solve the traveling salesman problem faster than brute force search.

    This gets solved by dynamic programming. The subproblems L[S][j] is the
    shortest path from vertex 1 to vertex j with where the visited vertex are
    in the set S (S includes 1 and j).

    Complexity: O(n^2*2^n) far better than brute force O(n!)

    Params:
        g: object, instance of src.graph.Graph class

    Returns:
        tuple, of vertices representing a tour of all vertices in the graph.
    """

    # 0. Initialization:
    A = {}
    S = tuple(g.get_vertices())
    n = len(S)
    first_vertex = S[0]
    S_without_first = tuple(i for i in S if i != first_vertex)

    def get_nested(A, t, i):
        """ Returns A[t][i] where t is a tuple and i is the last vertex. """
        if i == first_vertex:
            if t == tuple(first_vertex):
                return 0
            else:
                return float('inf')
        if t not in A:
            A[t] = {}
        if i not in A[i]:
            A[t][i] = float('inf')
        return A[t][i]

    def set_nested(A, t, i, value):
        if t not in A:
            A[t] = {}
        A[t][i] = value

    # 1. Corresponding Recurrence:
    #
    # A[S][j] =   min   (A[S-{k}][k] + c[k][j] , where S - set of vertices
    #           k in S                         , where j,k - vertices
    #           k != j
    for m in range(2, n):
        for s in itertools.combinations(S_without_first, m):
            s = tuple(list(s).insert(0, first_vertex))
            for j in s:
                if j == first_vertex:
                    continue

                min_cost = float('-inf')
                for k in s:
                    if k == j:
                        continue
                    s_without_k = tuple(x for x in s if x != k)
                    tmp_cost = get_nested(A, s_without_k, k) + g.get_edge_cost((k,j))
                    if min_cost > tmp_cost:
                        min_cost = tmp_cost
                set_nested(A, s, j, min_cost)

    # 2. Compute the optimal solution.
    min_cost = float('inf')
    min_path = ()
    for vertex in g.incident(first_vertex):
        S_without_vertex = set(x for x in S if x != vertex)
        tmp_cost = get_nested(A, S_without_vertex, vertex) + g.get_edge_cost((vertex, first_vertex))
        tmp_path = list(S_without_vertex).append(first_vertex)

    # 3. Return the final solution.
    return (min_cost, min_path)
