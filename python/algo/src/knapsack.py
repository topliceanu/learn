# -*- coding: utf-8 -*-


# Indexes for the tuple which represents an input item.
NAME = 0
VALUE = 1
WEIGHT = 2

def knapsack_dynamic_programming(items, capacity):
    """ Naively solves the knapsack problem given a capacity and a set of items.

    The knapsack problem is defined as follows: given a list of items with
    values and weights a knapsack with a given weight, optimize the knapsack usage,
    such that you maximize the value of the items in the knapsack.

    We assume item sizes and knapsack capacity are small integers in order to
    obtain polinomial running time.

    Complexity: O(n*W), n - num of items, W - num of distinct capacity values.
                This is NP-complete in the input weight. Complexity is polinomial
                only if the capacity W is not too big compared to n number of items.

    Args:
        items: list of tuples, format [(name: str, value: int, weight: int)]
        capacity: int, total capacity of the knapsack

    Returns:
        tuple, format (max_value, items)
            max_value: int, represents the max value that fits in the given weight.
            picked_items: list of tuples, with the items picked to maximize the
                knapsack usage. format [(name: str, value: int, weight: int)]
    """

    # 0. Initialization: let V[i][x] be the max value, such that it
    # only uses the first i items and has at most x weight.
    n = len(items)
    V = [[0]*(capacity+1) for __ in xrange(n+1)] # Max value for all solutions w/ 0 items is 0.

    # 1. Compute the max possible value that fits in the knapsack.
    for i in xrange(1, n+1):
        for x in xrange(capacity+1):
            [__, vi, wi] = items[i-1]
            if wi > x:
                V[i][x] = V[i-1][x]
            else:
                V[i][x] = max(V[i-1][x], V[i-1][x-wi] + vi)
    max_value = V[n][capacity]

    # 2. Reconstruct the solution.
    picked_items = []
    i = n
    x = capacity
    while True:
        [__, vi, wi] = items[i-1]
        if wi > x:
            i -= 1
        else:
            if V[i-1][x-wi] + vi > V[i-1][x]:
                picked_items.insert(0, items[i-1])
                i -= 1
                x -= wi
            else:
                i -= 1
        if i < 0 or x < 0:
            break

    return (max_value, picked_items)

def knapsack_dynamic_programming_for_two_knapsacks(items, capacity1, capacity2):
    """ What if you had two knapsacks. How do you fill them optimally. """
    # TODO

def knapsack_dynamic_programming_memory_efficient(items, capacity):
    """ The same API as the method above but with a focus on better memory
    utilization.

    Memory improvements are achived by exploiting the observation that we for
    each step of the computation we require partial results of the previous step.

    Args:
        items: list of tuples, format [(name: str, value: int, weight: int)]
        capacity: int, total capacity of the knapsack

    Returns:
        tuple, format (max_value, items)
            max_value: int, represents the max value that fits in the given weight.
            picked_items: list of tuples, with the items picked to maximize the
                knapsack usage. format [(name: str, value: int, weight: int)]
    """

    # 0. Initialization: let V[i][x] be the max value, such that it
    # only uses the first i items and has at most x weight.
    n = len(items)
    V = [[0]*(capacity+1) for __ in xrange(2)] # Max value for all solutions w/ 0 items is 0.

    # 1. Compute the max possible value that fits in the knapsack.
    for i in xrange(1, n+1):
        for x in xrange(capacity+1):
            [__, vi, wi] = items[i-1]
            if wi > x:
                V[1][x] = V[0][x]
            else:
                V[1][x] = max(V[0][x], V[0][x-wi] + vi)
        # Move the partial results in the first row.
        V[0] = V[1]
        V[1] = [0]*(capacity+1)

    max_value = V[0][capacity]

    # 2. TODO Reconstruct the solution by storing values for intermediate solutions.
    picked_items = []

    return (max_value, picked_items)


def knapsack_three_step_heuristic(items, capacity):
    """ Solves the knapsack problem given a capacity and a set of items using
    a three-step greedy heuristic:

    1. compute values/weight ratio for each item, then sort the items by ratio.
    2. pack as many items as they fit in the knapsack in the order sorted in 1.
    3. compare the values of the solutions picked in 2. with the item with the
    maximum value which fits in the knapsack. Pick the better one.

    Complexity: O(n), n - num of items
    Correctness: this algo is correct above 50% of the cases but, in 50% of
        the cases, it can be arbitrarly bad!!!

    Params:
        items: list of tuples, format [(name: str, value: int, weight: int)]
        capacity: int, total capacity of the knapsack

    Returns:
        tuple, format (max_value, items)
            max_value: int, represents the max value that fits in the given weight.
            picked_items: list of tuples, with the items picked to maximize the
                knapsack usage. format [(name: str, value: int, weight: int)]
    """
    # 1. and 2.
    sorted(items, key=lambda i: float(i[VALUE])/float(i[WEIGHT]), reverse=True)

    # 3.
    solution_one = []
    w = capacity
    i = 0
    while i < len(items):
        if items[i][WEIGHT] <= w:
            w -= items[i][WEIGHT]
            solution_one.append(items[i])
            i += 1
        else:
            break
    solution_two = [max(items, key=lambda i: i[VALUE])]

    # Figure out which is the largest solution.
    value_solution_one = sum([i[VALUE] for i in solution_one])
    value_solution_two = sum([i[VALUE] for i in solution_two])

    if value_solution_one > value_solution_two:
        return (value_solution_one, solution_one)
    else:
        return (value_solution_two, solution_two)

def knapsack_dynamic_programming_small_values(items, capacity):
    """ Solves the knapsack problem using dynamic programming with the focus
    on value not weight.

    We assume the item values are integers and small. This is then used in the
    arbitrary approximation version of the knapsack solution.

    Complexity: O(n^2*Vmax), where Vmax is the maximum value and n is the
                             number of items.
    Args:
        items: list of tuples, format [(name: str, value: int, weight: int)]
        capacity: int, total capacity of the knapsack

    Returns:
        tuple, format (fit_value, items)
            fit_value: int, represents the max value that fits in the given weight.
            picked_items: list of tuples, with the items picked to maximize the
                knapsack usage. format [(name: str, value: int, weight: int)]
    """
    # 0. Initialization
    n = len(items)
    # Max imaginable value is the sum of values for all items.
    max_value = sum([i[VALUE] for i in items])
    A = [[0] * (max_value+1) for __ in range(n+1)]
    for x in range(1, max_value+1):
        A[0][x] = float('inf')

    # 1. Recurrence. The subproblems are A[i][x] which represents the minimum
    # total weight that is sufficient to achieve a value larger than x while using
    # only the first i items. If that is impossible set it to +inf.
    for i in range(1, n+1):
        for x in range(max_value+1):
            [__, vi, wi] = items[i-1]
            if vi >= x:
                A[i][x] = min(A[i-1][x], wi)
            else:
                A[i][x] = min(A[i-1][x], A[i-1][x-vi] + wi)

    # 2. Find the intermediary problem composed of all n items and which fits
    # in the knapsack.
    x = max_value
    while A[n][x] > capacity:
        x -= 1
    fit_value = x

    # 3. Trace back to compute the optimal solution.
    picked_items = []
    i = n
    j = x # value
    while True:
        [__, vi, wi] = items[i-1]
        if j < vi:
            i -= 1
        else:
            if A[i-1][j-vi] + wi < A[i-1][j]:
                picked_items.insert(0, items[i-1])
                i -= 1
                j -= vi
            else:
                i -= 1
        if i < 0 or j < 0:
            break

    return (fit_value, picked_items)

def knapsack_arbitrarely_close_approximation(items, capacity, epsilon=0.1):
    """ Solve the knapsack problem with an accuracy specified in input.

    The total value of the solution produced by this algorithm is at least
    (1-epsilon) times the optimal solution.

    Algorithm:
    1. divide each item i's value by m and round down to the nearest int. (m is a function of epsilon):
    2. run knapsack_dynamic_programming_small_values routine on the transformed items.

    Complexity: O(n^2*Vmax) where Vmax is the largest item value in input set.

    Params:
        items: list of tuples, format [(name: str, value: int, weight: int)]
        capacity: int, total capacity of the knapsack
        epsilon: float, accuracy parameter supplied by the client. If epsilon is
            small, the error will be small but the running time will be higher.

    Returns:
        tuple, format (max_value, items)
            max_value: int, represents the max value that fits in the given weight.
            picked_items: list of tuples, with the items picked to maximize the
                knapsack usage. format [(name: str, value: int, weight: int)]
    """
    # Remove items larger than the knapsack capacity.
    items = [i for i in items if i[WEIGHT] <= capacity]

    # Modify the item values to make them small integers.
    Vmax = max(items, key=lambda i: i[VALUE])[VALUE]
    n = len(items)
    m = epsilon * Vmax / n
    modified = [(i[NAME], int(i[VALUE]/m), i[WEIGHT]) for i in items]

    (max_value, picked_items) = knapsack_dynamic_programming_small_values(modified, capacity)

    # Format output.
    max_value = int(float(max_value) * m)
    picked_names = [i[NAME] for i in picked_items]
    picked_items = [i for i in items if i[NAME] in picked_names]
    return (max_value, picked_items)
