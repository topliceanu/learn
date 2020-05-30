# -*- coding: utf-8 -*-

def triple_step(num_steps):
    """ 8.1 Triple Step: A child is running up a staircase with n steps and can
    hop either 1 step, 2 steps, or 3 steps at a time.
    Implement a method to count how many possible ways the child can run up the
    stairs.

    Solution: the idea is that at step t(i) we need to know how many ways the child can
    get to t(i-1), how many steps to get to t(i-2), then t(i-3).
    - From t(i-1) the child can only make one more step to get to t(i).
    - From t(i-2) the child can do a (1,1) or a 2 extra. However the (1,1) case is
    covered in getting from t(i-1) to t(i). So we will only count all the ways to get t(i-2) once.
    - From t(i-3) the child can do (1,1,1), (1,2), (2,1) and (3). (1,1,1) and (1,2)
    are covered by t(i-1) case, (2, 1) is covered by t(i-2) case so only (3) is not counted.
    In conclussion t(i) = t(i-1) + t(i-2) + t(i-3), an extension of Fibonacci
    """
    if num_steps <= 0:
        raise Exception("num_steps needs to be positive")
    arr = [1, 2, 4]
    if num_steps < 4:
        return arr[num_steps - 1]
    steps = 4
    while steps <= num_steps:
        arr[0], arr[1], arr[2] = arr[1], arr[2], arr[0] + arr[1] + arr[2]
        steps += 1
    return arr[2]

def robot_in_a_grid(grid):
    """ 8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of
    grid with r rows and c columns. The robot can only move in two directions,
    right and down, but certain cells are "off limits" such that the robot cannot
    step on them. Design an algorithm to find a path for the robot from the top
    left to the bottom right

    Complexity: O(n^2)

    Returns:
        list of pairs, each pair is (i, j), the box in the grid visited by the
            robot on it's way from source to destination.
            The list is empty if no path was found!
    """
    def rec_robot(grid, i, j):
        if i == 0 and j == 0:
            return ([(0, 0)], True)
        source_in_above = False
        if i - 1 >= 0 and grid[i - 1][j] != 1:
            from_above, source_in_above = rec_robot(grid, i - 1, j)
        source_in_left = False
        if j - 1 >= 0 and grid[i][j - 1] != 1:
            from_left, source_in_left = rec_robot(grid, i, j - 1)
        if source_in_above and source_in_left:
            from_above.append((i, j))
            return (from_above, True) # Optionally, we can return the shortes path.
        if not source_in_above and not source_in_left:
            return ([], False)
        if source_in_above:
            from_above.append((i, j))
            return (from_above, True)
        if source_in_left:
            from_left.append((i, j))
            return (from_left, True)

    path, _ = rec_robot(grid, len(grid) - 1, len(grid[0]) - 1)
    return path

def magic_index(arr):
    """ 8.3 Magic Index: A magic index in an array A [ 0... n -1] is defined
    to be an index such that A[i] = i.
    Given a sorted array of distinct integers, write a method to find a magic
    index, if one exists, in array A.

    FOLLOW UP
    What if the values are not distinct?

    For distinct values we can recurse on the half of the array which is smaller,
    all the time. For non-distinct values, we have to recurse on all elements.
    """
    def rec_magic_index(arr, left, right):
        if right < left:
            return []
        if right - left == 0:
            if arr[right] == right:
                return [right]
            else:
                return []

        middle = (right + left) / 2
        left_magic_indices = rec_magic_index(arr, left, middle)
        right_magic_indices = rec_magic_index(arr, middle + 1, right)
        return left_magic_indices + right_magic_indices

    return rec_magic_index(arr, 0, len(arr) - 1)

def power_set(arr):
    """ 8.4 Power Set: Write a method to return all subsets of a set. """
    if len(arr) == 0:
        return [ [] ] # only the empty set
    head, tail = arr[0], arr[1:]
    tail_subsets = power_set(tail)
    head_subsets = []
    for sub in tail_subsets:
        new_sub = sub[:]
        new_sub.append(head)
        head_subsets.append(new_sub)
    return tail_subsets + head_subsets

def recursive_multiply(a, b):
    """ 8.5 Recursive Multiply: Write a recursive function to multiply two
    positive integers without using the '*' operator.You can use addition,
    subtraction, and bit shifting, but you should minimize the number
    of those operations.
    """
    pass

def towers_of_hanoi(n):
    """ 8.6 Towers of Hanoi:
    In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
    different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
    of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
    constraints:
    (1) Only one disk can be moved at a time.
    (2) A disk is slid off the top of one tower onto another tower.
    (3) A disk cannot be placed on top of a smaller disk.
    Write a program to move the disks from the first tower to the last using stacks.
    """
    pass

def permutations_without_dups(string):
    """ 8.7. Permutations without Dups: Write a method to compute all
    permutations of a string of unique characters.

    Complexity: O(n^3)
    """
    def expand_perms(y, xs):
        out = []
        for x in xs:
            for i in range(len(x) + 1):
                copy = x[:]
                copy.insert(i, y)
                out.append(copy)
        return out

    def permutations_rec(arr):
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return [arr]
        head, tail = arr[0], arr[1:]
        perms = permutations_rec(tail)
        return expand_perms(head, perms)

    out = permutations_rec(list(string))
    return [''.join(o) for o in out]

def permutations_with_dups(string):
    """ 8.8 Permutations with Dups: Write a method to compute all permutations
    of a string whose characters are not necessarily unique.
    The list of permutations should not have duplicates.
    """
    def expand_perms(y, xs):
        out = []
        for x in xs:
            for i in range(len(x) + 1):
                if i == 0 or x[i - 1] != y:
                    copy = x[:]
                    copy.insert(i, y)
                    out.append(copy)
        return out

    def permutations_rec(arr):
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return [arr]
        head, tail = arr[0], arr[1:]
        perms = permutations_rec(tail)
        return expand_perms(head, perms)

    out = permutations_rec(list(string))
    return [''.join(o) for o in out]

def parens(n):
    """ 8.9 Parens: Implement an algorithm to print all valid
    (e.g., properly  opened and closed) combinations of n pairs of parentheses.
    Example:
    Input: 3
    Output: ( ( () ) ) , ( () () ) , ( () ) () , () ( () ) , () () ()
    """
    if n <= 0:
        return []
    if n == 1:
        return ['()']
    rest = parens(n-1)
    out = []
    for p in rest:
        out.append('()'+p)
        if '()' + p != p + '()':
            out.append(p+'()')
        out.append('('+p+')')
    return out

def paint_fill(screen):
    """ 8.1 O Paint Fill: Implement the "paint fill" function that one might see
    on many image editing programs. That is, given a screen (represented by a
    two-dimensional array of colors), a point, and a new color, fill in the
    surrounding area until the color changes from the original color.
    """
    pass

def coins(change):
    """ 8.11 Coins: Given an infinite number of quarters (25 cents),
    dimes (10 cents), nickels (5 cents), and pennies (1 cent), write
    code to calculate the number of ways of representing n cents.

    Using dynamic programming.
    The recursivity is:

        t(n, c) = t(n, sc), where sc is a coin smaller than k
                + t(n-i*c), where i is from 0 to n/c

    The memoization array A[i][j] is the number of combinations of coins using
    coins smaller or equal to i that sum up to j change.

    TODO FIXME
    """
    arr = [ [ 0 for _ in range(n+1) ] for _ in range(4) ]
    arr[0] = [1] * n # all changes can be produces in one way using 1s.

    for coin_index in range(1, 4):
        coin_val = [1, 5, 10, 25][coin_index]
        for sub_change in range(change):
            arr[coin_index][sub_change] = 0
            smaller_coins = filter((lambda c: c < coin_val), [1, 5, 10, 25])
            for smaller_coin_index in range(len(smaller_coins)):
                arr[coin_index][sub_change] += arr[smaller_coin_index][sub_change]
            times = sub_change / coin_val
            prev_coin_index = coin_index - 1
            prev_coin_val = [1, 5, 10, 25][prev_coin_index]
            for i in range(times):
                arr[coin_index][sub_change] += arr[prev_coin][sub_change - i * prev_coin_val]
    return arr[25][change]

def eight_queens():
    """ 8.12 Eight Queens: Write an algorithm to print all ways of arranging
    eight queens on an 8x8 chess board so that none of them share the same row,
    column, or diagonal. In this case, "diagonal" means all diagonals, not just
    the two that bisect the board.
    """
    def is_valid(candidate, current_queen_id):
        current_col = candidate[current_queen_id]
        for queen_id in range(0, current_queen_id):
            col = candidate[queen_id]
            if current_col == col:
                return False
            if abs(current_col - col) == current_queen_id - queen_id:
                return False
        return True

    def arrange_queen(queen_id, candidate, results):
        if queen_id == 8:
            results.add(candidate[:])
            return
        for pos in range(1, 8):
            candidate[queen_id] = pos
            if is_valid(candidate, queen_id):
                arrange_queen(queen_id + 1, candidate, results)

    results = []
    arrange_queen(0, [0] * 8, results)
    return results

def travelling_salesman(verties, edges):
    """ Implements a naive solution for the NP-complete problems of travelling
    salesman using backtracking.
    I'm assuming the graph is connected.
    Args:
        vertices, list of all ids of all vertices in the graph
        edges, list of triplets (src_vertex, dest_vertex, edge_cost), all ints
    Returns:
        path, list of vertex ids corresponding to the optimal path in the graph.
    """
    def is_solution(path, all_vertices):
        # when I visited all the edges and only once.
        edges = {}
        for edge in path:
            if edge in edges:
                return False
            edges[edge] = True
        return len(edges) == len(all_vertices)

    def next_vertex_options(edges, current_vertex, path_so_far):
        linked_edges = [ edge[1] for edge in edges if edge[0] == current_vertex ]
        return [ edge for edge in linked_edges if edge not in path_so_far ]

    def travelling_salesman_path(vertices, edges, current_vertex, path_so_far, results):
        if is_solution(path_so_far, vertices):
            results.add(path_so_far)
            return
        options = next_vertex_options(edges, current_vertex, path_so_far)
        for option in options:
            new_path = path_so_far[:]
            new_path.push(option)
            travelling_salesman_path(vertices, edges, option, new_path, results)

    results = []
    travelling_salesman_path(vertices, edges, 1, [1], results)
    return results

def stack_of_boxes(boxes):
    """ 8.13 Stack of Boxes: You have a stack of n boxes, with widths w i ,
    heights h i , and depths d i . The boxes cannot be rotated and can only
    be stacked on top of one another if each box in the stack is strictly
    larger than the box above it in width, height, and depth. Implement a
    method to compute the height of the tallest possible stack. The height of
    a stack is the sum of the heights of each box.
    """
    pass
