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

def max_weighted_independent_set_in_tree(g):
    """ Computes the max weight independent set of vertices for a tree.

    Args:
        g: object, instance of src.graph.Graph

    Returns:
        list, format [max_weight: int, vertices: list]
    """
    # TODO

def sequence_alignment(X, Y, mismatch_penality, gap_penalty):
    """ Computes the similarity measure between the two strings.

    The method is called the Needleman-Wunsch score. Penaties are applied when
    inserting gaps (if strings are not of equal size) and for missmatches
    (characters at corresponding indexes are different). The score is the
    minimum sum of such penalties which can express the diff between strings.

    Creators: Saul B. Needleman and Christian D. Wunsch

    Complexity: O(m*n) where m - length of X, n - lenght of Y

    Args:
        X: str, first string
        Y: str, second string
        gap_penalty: function, returns the penalty for a gap insertion in
            either of the strings.
        mismatch_penalty: function, returns the penalty for two different
            characters.

    Returns:
        tuple, format (total_penalty, x, y)
        total_penalty: float, the sum of penalties associated with dissimilarity
            between the strings. If 0 then the inputs are identical.
        X_mod: str, the modified version of X with introduced gaps
        Y_mod: str, the modified version of Y with introduced gaps
    """
    # 0. Initialization. A[i][j] is penalty for the optimal alignment between
    # X[i] and Y[j]
    A = [[0]*(len(Y)+1) for __ in xrange(len(X)+1)]

    # 1. Pad the array with the penalties when comparing a full string with an
    # empty string.
    for j in xrange(len(Y)+1):
        A[0][j] = j * gap_penalty()
    for i in xrange(len(X)+1):
        A[i][0] = i * gap_penalty()

    # 2. Compute all the subproblems.
    for i in xrange(1, len(X)+1):
        for j in xrange(1, len(Y)+1):
            A[i][j] = min(A[i-1][j-1] + mismatch_penality(X[i-1], Y[j-1]),
                          A[i-1][j] + gap_penalty(),
                          A[i][j-1] + gap_penalty())

    # 3. Compute total penalty.
    total_penalty = A[len(X)][len(Y)]

    # 4. Implement trace-back to build up the modifications with produce
    # optimal penalties.
    X_mod = ''
    Y_mod = ''
    i = len(X)
    j = len(Y)
    while True:
        a = A[i-1][j-1] + mismatch_penality(X[i-1], Y[j-1])
        b = A[i-1][j] + gap_penalty()
        c = A[i][j-1] + gap_penalty()
        if A[i][j] == a: # There is missmatch between X and Y at position i.
            X_mod = X[i-1] + X_mod
            Y_mod = Y[j-1] + Y_mod
            i -= 1
            j -= 1
        elif A[i][j] == b: # There is a gap in Y at position j.
            X_mod = X[i-1] + X_mod
            Y_mod = '-' + Y_mod
            i -= 1
        elif A[i][j] == c: # There is a gap in X at position i.
            X_mod = '-' + X_mod
            Y_mod = Y[j-1] + Y_mod
            j -= 1
        if i == 0 or j == 0:
            break

    # Add the left over gaps in front, if any.
    if i == 0:
        X_mod = ''.join(['-' for __ in range(j)]) + X_mod
        Y_mod = ''.join(Y[:j]) + Y_mod
    if j == 0:
        X_mod = ''.join(X[:i]) + X_mod
        Y_mod = ''.join(['-' for __ in range(i)]) + Y_mod

    # 5. Return the results.
    return (total_penalty, X_mod, Y_mod)


# From Skienna: The Algorithm Design Manual, Dynamic Programming chapter.

def match_substring(needle, haystack):
    """ Find best approximate match of substring needle in a larger haystack.

    Params:
        needle: str, a pattern to look for.
        haystack: str, a corpus to search for the pattern in.

    Return:
        str, the closest string to the pattern needle found in haystack.
    """
    pass # TODO

def longest_common_subsequence(str1, str2):
    """ Find the longest scattered substrings included in both inputs. """
    pass # TODO

def maximum_monotone_sequence(s):
    """ Remove the fewest number of characters from input so that it leaves a
    monotonically increasing subsequence.

    Params:
        s: str, input string

    Returns:
        tuple, format (max_length, max_sequence)
        max_length: int, number of characters in subsequence
        max_sequence: str, monotonically increasing subsequence.
    """
    # Initialize: A[i] is the length of the maximum increasing subsequence in
    # the first i elements.
    # B holds the predecessors for each value.
    A = [1]*len(s)
    B = [None]*len(s)

    for i in range(1, len(s)):
        max_length_so_far = 0
        precedessor = None
        for j in range(0, i):
            if s[i] > s[j] and max_length_so_far < A[j]:
                max_length_so_far = A[j]
                precedessor = j
        A[i] = max_length_so_far + 1
        B[i] = precedessor

    # Rebuild the solution.
    max_length = A[len(s)-1]
    max_sequence = ''
    i = len(s) - 1
    while i != None:
        max_sequence = s[i] + max_sequence
        i = B[i]

    return (max_length, max_sequence)

def linear_partition(values, num_partitions):
    """ Fairly partition a set of integers without rearrangement.

    Formally: Given an arrangement s of non-negative numbers and an integer k,
    partition s into k or fewer ranges, to minimize the maximum sum over all
    ranges, without reordering the numbers.

    Params:
        values: list, of non-negative integers representing job costs.
        num_partitions: int, number of partitions in which to re-arrange the set

    Return:
        tuple, format (min_max_sum, partitions)
            min_max_sum: the min of max of the sums of elements in each partition.
            partitions: list, of lists, representing the partitioned jobs.
    """
    # 0. Initialization
    # A[i][j] - the min of max of sums of values for each
    # partition, given that there are i partition in the first j elements in
    # the set.
    # - for 0 partitions, the value of A[0][j] = sum(v[0->j])
    # - for 0 elements, the value of A[i][0] = 0
    N = len(values)
    A = [[0] * (N+1) for __ in range(num_partitions)]

    for j in range(N+1):
        A[0][j] = sum(values[:j])
    for i in range(num_partitions):
        A[i][0] = 0

    # 1. Compute the partial subproblems. The Recurstion is the following:
    #            j                   j
    # A[i][j] = min[ max(A[i-1][k], sum(v[p])) ]
    #           k=0                 p=k
    for i in range(1, num_partitions):
        for j in range(N+1):
            # Split the [0,j] interval in two. Compute sum of the right
            # elements and compare with the min of max sums computed in the
            # previous step for the left elements.
            minimum = float('inf')
            for k in range(j):
                sum_last_partition = sum(values[k:j])
                maximum = max(A[i-1][k], sum_last_partition)
                if maximum < minimum:
                    minimum = maximum
            A[i][j] = minimum
    min_max_sum = A[num_partitions-1][N]

    # 2. Trace-back to compute the actual partition.
    # TODO this is not correct!
    partitions = []
    last_partition = []
    for i in range(N):
        if sum(last_partition) + values[i] <= min_max_sum:
            last_partition.append(values[i])
        else:
            partitions.append(last_partition[:])
            last_partition = [values[i]]
    if len(last_partition) > 0:
        partitions.append(last_partition)

    # 3. Return results.
    return (min_max_sum, partitions)

def optimal_binary_search_tree(items):
    """ Build up an optimal search tree given a set of items and known
    frequency of access for each of them.

    The subproblems are all the contiguous subsets [i, j] of the
    items list, thus creating an array of results, ie. C.

    Complexity: O(n^3) better then O(2^n) for brute force search.

    Args:
        items: list, of tuples, format (key, access_frequency)

    Returns:
        tuple, format (search_cost, pre_order)
            optimal_search_cost: int, the weighted search cost for an optimized BST
            pre_order: list, of tuples, format (key, access_frequency)
                arrangement of tuples in pre-order which makes it easy to
                reconstruct an optimal BST.
    """
    # 0. Initialization: sort items by key, not access frequency.
    items = sorted(items, key=lambda t: t[0])
    n = len(items)

    # C[i][j] is the weighted search cost of an optimal BST for items with indexes i to j.
    C = [[0]*n for __ in xrange(n)]
    # R[i][j] holds the optimal root for the optimal BST for items i to j.
    R = [[None]*n for __ in xrange(n)]

    # 1. Compute all the subproblems:
    # C[i][j] =  min   (sum(pk) + C[i][r-1] + C[r+1][j])  , given that i>=j
    #           r=i->j  k=i->j
    # C[i][j] = 0  , if j < i
    # C[i][j] is the total weighted access time for a BST with elements [i:j] and root r, i<=r<=j
    for s in range(0, n): # s is the size of the problem, therefor j=i+s
        for i in range(n): # i is the first index of the contiguous loop.
            if i + s >= n:
                continue

            min_cost = float('inf')
            root = None

            for r in range(i, i+s+1):
                if r-1 < 0:
                    left_cost = 0
                else:
                    left_cost = C[i][r-1]
                if r+1 > n-1:
                    right_cost = 0
                else:
                    right_cost = C[r+1][i+s]
                tmp_min_cost = sum([j[1] for j in items[i:i+s+1]]) + \
                        left_cost + right_cost
                if tmp_min_cost < min_cost:
                    min_cost = tmp_min_cost
                    root = r

            C[i][i+s] = min_cost
            R[i][i+s] = root

    # The end result is the value for the entire list of access frequencies.
    optimal_search_cost = C[0][n-1]

    # 2. Build up the optimal tree structure.
    pre_order = []

    def traverse(i, j):
        """ Traverse the R array to compute the pre-order traversal of the
        optimal binary search tree.

        The items list is traversed recursively in intervals [i,j]. For each
        invocation the root position is extracted from R array.

        Args:
            i: int, the left side of the subtree
            j: int, the right side of the subtree

        Returns:
            list, pre-order traversal of the optimal bst.
        """
        if i > j:
            return

        r = R[i][j]
        if r == None:
            return

        pre_order.append(items[r])
        traverse(i, r-1)
        traverse(r+1, j)
    traverse(0, n-1)

    return (optimal_search_cost, pre_order)

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


# See topcoder tutorial on Dynamic Programming.

def min_coins(coins, total):
    """ Computes the minimum number of coins which sum up to total.

    Params:
        coins: list of non-negative integers representing the values of the coins.
        total: int, in fact it has to be a non-negative integer.

    Returns
        tuple: (min_num_coins, picked_coins)
            min_num_coins: int, the min number of coins
            picked_coins: list, which coins are used which sum up to total.
    """
    # Initialize A[i] - the number of coins needed to sum up to value i.
    # B[i] the coin chosen which yealds the min number of other coins to reach i.
    A = [float('inf')] * (total + 1)
    A[0] = 0
    B = [None] * (total + 1)

    # Compute subproblems.
    for intermediary_total in range(1, total+1):
        for coin in coins:
            if coin > intermediary_total:
                continue
            if A[intermediary_total] > A[intermediary_total - coin] + 1:
                A[intermediary_total] = A[intermediary_total - coin] + 1
                B[intermediary_total] = coin

    min_num_coins = A[total]

    # Pick the last coin picked.
    picked_coins = []
    i = total
    while i >= 0:
        coin = B[i]
        if coin == None:
            break
        picked_coins.append(coin)
        i -= coin

    return (min_num_coins, picked_coins)

def zig_zag(numbers):
    """ Determine the longest subsequence of numbers in input which form a
    zig-zag sequence.

    A sequence is zig-zag if the difference between successive numbers
    alternates strictly between positive and negative.

    See: http://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
    for problem statement and test cases.

    Params:
        numbers: list, of ints.

    Returns:
        tuple, format (max_length, subsequence)
            max_length: int, max length of a zig-zag sequence.
            subsequence: list, the actual numbers.
    """
    # In the case where the numbers list is smaller than 2, simply return it.
    if len(numbers) <= 2:
        return (len(numbers), numbers)

    # Initialization:
    # A is a list of one and two elements is always zig-zag.
    # B is a list which maintains for each i the previous position in the input
    # which forms the longest zig-zag
    A = [0] * len(numbers)
    A[0] = 1
    A[1] = 2
    B = [None] * len(numbers)
    B[1] = 0

    def is_zig_zag(a, i, j, k):
        """ Checks whether a[i], a[j] and a[k] are zig-zag. """
        if i is None:
            return True
        return (a[i] - a[j] > 0 and a[j] - a[k] < 0) or \
               (a[i] - a[j] < 0 and a[j] - a[k] > 0)

    # Compute the max length zig-zag sequence.
    for i in range(2, len(numbers)):
        max_length = float('-inf')
        predecessor = None
        for j in range(i):
            if is_zig_zag(numbers, B[j], j, i) and max_length < A[j] + 1:
                max_length = A[j] + 1
                predecessor = j
        A[i] = max_length
        B[i] = predecessor

    max_index = A.index(max(A))

    # Trace-back to compute one possible solution for longest zig-zag string.
    i = max_index
    subsequence = []
    while i >= 0 and i != None:
        subsequence.insert(0, numbers[i])
        i = B[i]

    return (A[max_index], subsequence)

def bad_neighbours(values):
    """ Maximize the values choosen from a circular list such that no two
    values are neighbours.

    See: http://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009
    for problem statement and test cases.

    Params:
        values: list, of integers

    Returns:
        tuple, format (max_value, picked_values)
            max_value: int,
            picked_values: list
    """
    def max_donations(values):
        """ Reduces the original problem to a non-circular list, ie. last and
        first element are not considered neighbours.

        Same input and output.
        """
        if len(values) < 2:
            return

        # 0. Initialization:
        # A[i] - max donations which include the ith element.
        # B[i] - for the max donation which includes ith element which was the
        # position of the previous element which composes the solution.
        N = len(values)
        A = [0]*N
        A[0] = values[0]
        A[1] = values[1]
        B = [None]*N

        # 1. Compute the max donations values and remember choises made to
        # help with rebuilding the solution.
        for i in range(2, N):
            maximum = float('-inf')
            for j in range(i-1):
                if maximum < A[j]:
                    maximum = A[j]
                    B[i] = j
            A[i] = maximum + values[i]
        maximum_donations = A[N - 1]

        # 2. Compose the donations selection.
        donations = []
        i = N -1
        while i != None:
            donations.insert(0, values[i])
            i = B[i]

        # 3. Return the original values.
        return (maximum_donations, donations)

    # Because the list is circular, we will compute the result
    # twice once for values[0:n-1] and once for values[1:n].
    one = values[:-1] # exclude last value
    two = values[1:] # exclude first value

    (one_max_donation, one_donations) = max_donations(one)
    (two_max_donation, two_donations) = max_donations(two)

    if one_max_donation > two_max_donation:
        return (one_max_donation, one_donations)
    else:
        return (two_max_donation, two_donations)

def flower_garden(values):
    """
    See: http://community.topcoder.com/stat?c=problem_statement&pm=1918&rd=5006
    for problem statement and test cases.
    """
    pass # TODO
