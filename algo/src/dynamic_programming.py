# -*- coding:utf-8 -*-


def max_weighted_independent_set_in_path_graph(weights):
    """ Computes the independent set with maximum total weight for a path graph.

    A path graph has all vertices are connected in a single path, without cycles.
    An independent set of vertices is a subset of the graph vertices such that
    no two vertices are adjacent in the path graph.

    Args:
        weights: list, of vertex weights in the order they are present in the
            graph.

    Returns:
        list, format [max_weight: int, vertices: list]
    """
    a = [0] * len(weights)
    a[0] = weights[0]
    a[1] = max(weights[0], weights[1])
    for i in range(2, len(weights)):
        a[i] = max(a[i-1], a[i-2]+weights[i])

    max_weight = a[len(weights)-1]
    vertices = []

    # Hack! left-pad with a 0 to make the algorithm select the initial weight.
    weights.insert(0, 0)

    i = len(weights) - 1
    while (i>1):
        if a[i-2] + weights[i] >= a[i-1]:
            vertices.insert(0, weights[i])
            i -= 1
        i -= 1

    return [max_weight, vertices]

def knapsack(items, capacity):
    """ Solves the knapsack problem given a capacity and a set of items.

    The knapsack problem is defined as follows: given a list of items with
    values and sizes a knapsack with a given size, optimize the knapsack usage,
    such that you maximize the value of the items in the knapsack.

    Complexity: O(n*W), n - num of items, W - num of distinct capacity values.

    Args:
        items: list of tuples, format [(name: str, value: int, size: int)]
        capacity: int, total capacity of the knapsack

    Returns:
        list of tuples, with the items picked to maximize the knapsack usage.
            format [(name: str, value: int, size: int)]
    """
    # Indexes in the tuple.
    NAME = 0
    VALUE = 1
    SIZE = 2

    # Compute the max possible value of the knapsack.
    n = len(items)
    A = [[0]*capacity for __ in xrange(n)]

    for i in xrange(1, n):
        for x in xrange(capacity):
            if items[i][SIZE] > x:
                index = x
            else:
                index = x - items[i][SIZE]
            A[i][x] = max(A[i-1][x], A[i-1][index] + items[i][VALUE])

    max_value = A[n-1][capacity-1]

    # TODO Reconstruct the solution.
    return max_value

def sequence_alignment(X, Y, gap_penalty=10, mismatch_penality=10):
    """ Computes the similarity measure between the two strings.

    The method is called the Needleman-Wunsch score. Penaties are applied when
    inserting gaps (if strings are not of equal size) and for missmatches
    (characters at corresponding indexes are different). The score is the
    minimum sum of such penalties which can express the diff between strings.

    Creators: Saul B. Needleman Christian D. Wunsch

    Args:
        X: str, first string
        Y: str, second string
        gap_penalty: float, penalty for a gap insertion in either of the strings.
        mismatch_penalty: float, penalty for two different characters.

    Returns:
        float, the sum of penalties associated with dissimilarity between the
            strings. If 0 then the inputs are identical.
    """
    A = [[0]*len(X) for __ in xrange(len(Y))]
    for i in xrange(len(X)):
        A[i][0] = A[0][i] = i * gap_penalty

    for i in xrange(1, len(X)):
        for j in xrange(1, len(Y)):
            if X[i] != Y[j]:
                instance_mismatch_penality = mismatch_penality
            else:
                instance_mismatch_penality = 0
            A[i][j] = min(A[i-1][j-1] + instance_mismatch_penality,
                          A[i-1][j] + gap_penalty,
                          A[i][j-1] + gap_penalty)

    return A[len(X)-1, len(Y)-1]
