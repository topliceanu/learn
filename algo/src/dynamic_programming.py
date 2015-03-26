# -*- coding:utf-8 -*-


def max_weighted_independent_set_in_path_graph(weights):
    """ Computes the independent set with maximum total weight for a path graph.

    A path graph has all vertices are connected in a single path, without cycles.
    An independent set of vertices is a subset of the graph vertices such that
    no two vertices are adjacent in the path graph.

    Complexity: O(n); Space: O(n)

    Args:
        weights: list, of vertex weights in the order they are present in the
            graph.

    Returns:
        list, format [max_weight: int, vertices: list]
    """

    # 0. Initialization.
    a = [0] * (len(weights)+1)
    a[0] = 0 # Max weight for empty graph.
    a[1] = weights[0] # Max weight for the graph with only the first weight.

    # 1. Compute the max total weight possible for any independent set.
    for i in range(2, len(weights)+1):
        a[i] = max(a[i-1], a[i-2]+weights[i-1])

    max_weight = a[len(weights)]

    # 2. Trace back from the solution through the subproblems to compute the
    # vertices in the independent set.
    vertices = []
    i = len(weights)
    while (i>0):
        if a[i-2] + weights[i-1] >= a[i-1]:
            vertices.insert(0, weights[i-1])
            i -= 2
        else:
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
        tuple, format (max_value, items)
            max_value: int, represents the max value that fits in the given size.
            picked_items: list of tuples, with the items picked to maximize the
                knapsack usage. format [(name: str, value: int, size: int)]
    """
    # Indexes in the tuple.
    NAME = 0
    VALUE = 1
    SIZE = 2

    # 0. Initialization: let V[i][x] be the intermediary solution, such that it
    # only uses the first i items and has at most x size.
    n = len(items)
    V = [[0]*(capacity+1) for __ in xrange(n+1)] # Max value for all solutions w/ 0 items is 0.

    # 1. Compute the max possible value of the knapsack.
    for i in xrange(1, n+1):
        for x in xrange(capacity+1):
            wi = items[i-1][SIZE]
            vi = items[i-1][VALUE]
            if wi > x:
                V[i][x] = V[i-1][x]
            else:
                V[i][x] = max(V[i-1][x], V[i-1][x-wi] + vi)
    max_value = V[n][capacity]

    # 2. Reconstruct the solution.
    picked_items = []
    # TODO fix this.
    #i = n
    #x = capacity
    #for i in xrange(n, 0, -1):
    #    for x in xrange(capacity, 0, -1):
    #        wi = items[i-i][SIZE]
    #        vi = items[i-i][VALUE]
    #        if wi < x and V[i-1][x-wi] + vi > V[i-1][x]:
    #            #print '>>>>', i, x
    #            picked_items.append(items[i-1])

    return (max_value, picked_items)

def sequence_alignment(X, Y, mismatch_penality, gap_penalty):
    """ Computes the similarity measure between the two strings.

    The method is called the Needleman-Wunsch score. Penaties are applied when
    inserting gaps (if strings are not of equal size) and for missmatches
    (characters at corresponding indexes are different). The score is the
    minimum sum of such penalties which can express the diff between strings.

    Creators: Saul B. Needleman Christian D. Wunsch

    Args:
        X: str, first string
        Y: str, second string
        gap_penalty: function, returns the penalty for a gap insertion in
            either of the strings.
        mismatch_penalty: function, returns the penalty for two different
            characters.

    Returns:
        float, the sum of penalties associated with dissimilarity between the
            strings. If 0 then the inputs are identical.
    """
    # 0. Initialization. A[i][j] is penalty for the optimal alignment between
    # X[i] and Y[j]
    A = [[0]*(len(X)+1) for __ in xrange(len(Y)+1)]

    for i in xrange(len(X)+1):
        A[0][i] = i * gap_penalty()
    for j in xrange(len(Y)+1):
        A[j][0] = j * gap_penalty()

    for i in xrange(1, len(X)+1):
        for j in xrange(1, len(Y)+1):
            A[j][i] = min(A[j-1][i-1] + mismatch_penality(X[i-1], Y[j-1]),
                          A[j-1][i] + gap_penalty(),
                          A[j][i-1] + gap_penalty())

    return A[len(X)-1][len(Y)-1]
