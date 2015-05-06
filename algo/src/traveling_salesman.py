# -*- conding: utf-8 -*-

import array
import itertools
import math


class Store(object):

    def __init__(self, vertices):
        self.data = {}
        self.vertices = vertices
        self.first_vertex = vertices[0]

    def get(self, t, i):
        """ Returns A[t][i] where t is a tuple containing the last i-1 vertices
        and i is the last vertex.
        """
        if t not in self.data:
            self.data[t] = {}
        if i not in self.data[t]:
            if i == self.first_vertex and t == tuple(self.first_vertex):
                self.data[t][i] = 0
            else:
                self.data[t][i] = float('inf')
        return self.data[t][i]

    def set(self, t, i, value):
        """ Sets the value of A for vertices tuple t and last vertex i. """
        if t not in self.data:
            self.data[t] = {}
        self.data[t][i] = value

    def clear(self, m):
        if m <= 0:
            return
        for t in itertools.combinations(self.vertices, m):
            if t in self.data:
                del self.data[t]


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
    vertices = sorted(g.get_vertices())
    n = len(vertices)
    A = Store(vertices)
    first_vertex = vertices[0]
    S = tuple(vertices)
    S_without_first = tuple([i for i in vertices if i != first_vertex])


    # 1. Corresponding Recurrence:
    # A[S][j] - minimum length of a path from first_vertex to vertex j that
    # visits precisely the vertices in S, exactly once each:
    # A[S][j] =   min   (A[S-{k}][k] + c[k][j] , where S - set of vertices
    #           k in S                         , where j,k - vertices
    #           k != j
    for m in range(1, n): # number of vertices in the path.
        for s in itertools.combinations(S_without_first, m): # all vertex combinations of size m.
            s = (first_vertex,) + s
            for j in s:
                if j == first_vertex:
                    continue

                s_without_j = tuple([i for i in s if i != j])
                min_cost = float('inf')

                for k in s:
                    if k == j:
                        continue

                    tmp_cost = A.get(s_without_j, k) + g.get_edge_value((k,j))
                    if min_cost > tmp_cost:
                        min_cost = tmp_cost
                A.set(s, j, min_cost)
        A.clear(m-1)

    # 2. Compute the optimal solution: the min path from start vertex to any
    # other vertex traversing all other vertices only once. To that we add the
    # final hop back to first vertex.
    min_cost = float('inf')
    min_path = ()
    for vertex in S:
        if vertex == first_vertex:
            continue
        tmp_cost = A.get(S, vertex) + g.get_edge_value((vertex, first_vertex))
        if tmp_cost < min_cost:
            min_cost = tmp_cost

    # 3. Return the final solution.
    # TODO compute the min path as well.
    return (min_cost, min_path)
