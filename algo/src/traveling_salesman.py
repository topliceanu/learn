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


def fast_traveling_salesman(points):
    """ Solves the travelling salesman problem for large data sets.

    Args:
        points: list of tuples, format (x:int, y:int)

    Returns:
        float, min cost of a tour passing through all points in the graph

    """

    INF = float('inf')
    n = len(points)
    start_point = 0

    def to_tuple(index):
        """ Transforms a index into it's corresponding tuple. """
        out = []
        for i in range(n):
            if index & (1 << i) != 0:
                out.append(i)
        return tuple(out)

    def to_index(tup):
        """ Transforms a tuple of numbers into it's corresponding index. """
        out = 0
        for i in tup:
            out = out | (1<<i)
        return out

    # 1. Hash table holding all permutations of point names without the first point.
    tuples = {}
    k = 0
    for size in xrange(1, n+1):
        for combination in itertools.combinations(range(n), size):
            tuples[combination] = k
            k += 1

    # 2. Precompute distances.
    distances = {}
    for i in xrange(n):
        for j in xrange(n):
            if i == j:
                continue
            if i not in distances:
                distances[i] = {}
            if j not in distances[i]:
                distances[i][j] = float(math.sqrt((points[i][0] - points[j][0])**2 +
                                                  (points[i][1] - points[j][1])**2))

    # 3. Initialize the container array.
    A = [[INF]*2 for __ in range(2**n)]
    A[0][0] = 0 # Corresponding to the path to the same start vertex.

    # 4. Main loop.
    for size in xrange(1, n):

        for s in itertools.combinations(range(1, n), size):
            s = (0,) + s
            index_s = tuples[s]
            for j in s:
                if j == start_point:
                    continue

                s_without_j = tuple([i for i in s if i != j])
                index_s_without_j = tuples[s_without_j]

                min_cost = float('inf')
                for k in s:
                    if k == j:
                        continue

                    tmp_cost = A[index_s_without_j][0] + distances[k][j]
                    if min_cost > tmp_cost:
                        min_cost = tmp_cost
                A[index_s][1] = float(min_cost)

        for i in xrange(2**n):
            A[i][0] = A[i][1]
            A[i][1] = INF

    # 5. Compute the min length circuit.
    min_cost = float('inf')
    min_path = ()
    index_all = 2**n - 2

    for point in range(n):
        if point == start_point:
            continue
        tmp_cost = A[index_all][0] + distances[point][start_point]
        if tmp_cost < min_cost:
            min_cost = tmp_cost

    return min_cost
