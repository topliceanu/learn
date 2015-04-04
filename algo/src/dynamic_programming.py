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

    # 0. Initialization: A[i] - max total weight of the independent set for
    # the first i vertices in the graph.
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
                NP-complete in the input size.

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

    # 1. Pad the array with the penalties when comparing a full string with an
    # empty string.
    for i in xrange(len(X)+1):
        A[0][i] = i * gap_penalty()
    for j in xrange(len(Y)+1):
        A[j][0] = j * gap_penalty()

    # 2. Compute all the subproblems.
    for i in xrange(1, len(X)+1):
        for j in xrange(1, len(Y)+1):
            A[j][i] = min(A[j-1][i-1] + mismatch_penality(X[i-1], Y[j-1]),
                          A[j-1][i] + gap_penalty(),
                          A[j][i-1] + gap_penalty())

    # 3. Return the value
    return A[len(X)-1][len(Y)-1]

    # 4. Implement trace-back to build up the modifications with produce
    # optimal penalties. TODO

def optimal_binary_search_tree(access_frequencies):
    """ Build up an optimal search tree given a set of items and known
    frequency of access for each of them.

    The subproblems are all the contiguous subsets [i, j] of the
    access_frequencies list, thus creating an array of results, ie. C.

    Complexity: O(n^3) better then O(2^n) for brute force search.

    Args:
        access_frequencies: dict, format {key: access_frequency}

    Returns:
        object, an optimized binary search tree.
    """
    # 0. Initialization
    n = len(access_frequencies)

    # C[i][j] is the weighted search cost of an optimal BST for items i to j.
    C = [[0]*n for __ in xrange(n)]

    # 1. Compute all the subproblems:
    # C[i][j] =  min   (sum(pk) + C[i][r-1] + C[r+1][j])  , given that i>=j
    #           r=i->j  k=i->j
    # C[i][j] = 0  , if i < j
    for i in range(n): # i is the first index of the contiguous loop.
        for s in range(n): # s is the size of the problem, ie j-i
            if i+s >= n:
                continue
            min_cost = float('inf')
            for r in range(i, i+s):
                if r-1 < 0:
                    left_cost = 0
                else:
                    left_cost = C[i][r-1]
                if r+1 > n:
                    right_cost = 0
                else:
                    right_cost = C[r+1][i+s]
                tmp_min_cost = sum(access_frequencies[i:i+s]) + left_cost + right_cost
                if tmp_min_cost < min_cost:
                    min_cost = tmp_min_cost
            C[i][i+s] = min_cost

    # The end result is the value for the entire list of access frequencies.
    return C[0][n-1]

def binomial_coefficient(m, n):
    """ Given the equation (x+1)^n, return the coefficing of x^m.

    Use as reference the triangle of Pascal:
                1
               1 1
              1 2 1
             1 3 3 1
            1 4 6 4 1

    Params:
        m, int
        n, int

    Returns:
        int
    """
    N = n+1
    A = [[0]*N for __ in range(N)]

    for i in range(N):
        A[i][0] = 1
        A[i][i] = 1

    for i in range(1, N):
        for j in range(1, i):
            A[i][j] = A[i-1][j-1] + A[i-1][j]

    return A[n][m]

    # Recursive version.
    #if n == 0:
    #    return 1
    #if m == 0 or m == n:
    #    return 1
    #return binomial_coefficient(m-1 , n-1) + binomial_coefficient(m, n-1)
