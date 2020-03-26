# -*- coding: utf-8 -*-

import unittest
import random

from src.heap import Heap
from src.graph import Graph
from src.strongly_connected_components import scc


class TheoryProblems(unittest.TestCase):

    def test_problem_1(self):
        """ You are given as input an unsorted array of n distinct numbers,
        where n is a power of 2. Give an algorithm that identifies the
        second-largest number in the array, and that uses at most
        n+log2n−2 comparisons.

        Solution: use a hash data structure.
        """
        numbers = [5,1,2,5,1,2,3,54,6,7,1,3,3,5,6,2,3,4,56,6]
        h = Heap()
        for number in numbers:
            h.insert(-number)

        h.extract_min()
        actual = -h.extract_min()
        self.assertEqual(actual, 54, 'found the second largest number')

    def test_problem_2(self):
        """ You are a given a unimodal array of n distinct elements, meaning
        that its entries are in increasing order up until its maximum element,
        after which its elements are in decreasing order. Give an algorithm
        to compute the maximum element that runs in O(log n) time.

        Solution: use divide and conquer and stop when
        """
        def find_max(data, left, right):
            if right - left == 1:
                return None
            if right - left == 2:
                if data[left] <= data[left+1] > data[right]:
                    return data[left+1]
                else:
                    return None

            middle = (left + right) / 2
            left_max = find_max(data, left, middle)
            right_max = find_max(data, middle, right)

            if left_max != None:
                return left_max
            if right_max != None:
                return right_max

        numbers = [1,2,3,4,5,6,7,8,9,10,9,8,7,4,3,2,1]
        actual = find_max(numbers, 0, len(numbers)-1)
        self.assertEqual(actual, 10, 'should have found the max')

    def test_problem_3(self):
        """ You are given a sorted (from smallest to largest) array A of n
        distinct integers which can be positive, negative, or zero. You want
        to decide whether or not there is an index i such that A[i] = i.
        Design the fastest algorithm that you can for solving this problem.

        Solution: binary search.
        """
        def find_same_index_and_value(data, left, right):
            if left == right:
                if data[left] == left:
                    return left
                else:
                    return None

            middle = (left + right) / 2
            left_find = find_same_index_and_value(data, left, middle)
            right_find = find_same_index_and_value(data, middle+1, right)

            if left_find != None:
                return left_find
            if right_find != None:
                return right_find

        numbers = [-5, -3, 0, 3, 5, 7, 9]
        actual = find_same_index_and_value(numbers, 0, len(numbers)-1)
        self.assertEqual(actual, 3, 'finds the correct position in the list '
                                    'with index the same as value')

        numbers = [-5, -3, 0, 2, 5, 7, 9]
        actual = find_same_index_and_value(numbers, 0, len(numbers)-1)
        self.assertIsNone(actual, 'fails to find any number in the input array')

    def test_problem_5(self):
        """ You are given an n by n grid of distinct numbers. A number is a
        local minimum if it is smaller than all of its neighbors. (A neighbor
        of a number is one immediately above, below, to the left, or the right.
        Most numbers have four neighbors; numbers on the side have three; the
        four corners have two.) Use the divide-and-conquer algorithm design
        paradigm to compute a local minimum with only O(n) comparisons between
        pairs of numbers. (Note: since there are n^2 numbers in the input, you
        cannot afford to look at all of them. Hint: Think about what types of
        recurrences would give you the desired upper bound.)

        Solution: Divide and conquer similar to the closest pair problem.
        See: http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf
        In master method, if d = 0 and a = b, then O(n) - split the array in
            four at each recursion. In combine step simply concat the resulting
            lists of local mins.
        Also, we need to find __any__ local minimum!
        """
        #def add_padding(arr):
        #    INF = floag('-inf')
        #    n = len(arr)

        #    out = []
        #    out.append(INF * (n+2))
        #    for lin in arr:
        #        out.append([INF].extend(line).append(INF))
        #    out.append(INF * (n+2))
        #    return out

        #def find_min(arr):
        #    pass

        #def recurse_local_minimum(arr, li, ri, lj, rj):
        #    if ri-li <= 1 and rj - lj <= 1:
        #        return

        #    center_row_index = (ri-li)/2
        #    center_col_index = (rj-lj)/2
        #    center_row = arr[center_row_index][lj:rj]
        #    center_col = arr[li:ri][center_col_index]

        #    (min_row, min_row_index) = find_min(center_row)
        #    (min_col, min_col_index) = find_min(center_col)

        #    if is_local_min(arr, center_row_index, min_row_index):
        #        return arr[center_row_index][min_row_index]

        #    if is_local_min(arr, min_col_index, center_col_index):
        #        return arr[min_col_index][center_col_index]

        #    return recurse_local_minimum(arr)

        #def find_local_minimum(arr):
        #    arr = add_padding(arr)
        #    n = len(arr) - 1
        #    m = len(arr[0]) - 1
        #    return recurse_local_minimum(arr, 0, n, 0, m)

        ## A corner local minimum.
        #numbers = [
        #    [1,2,3,4],
        #    [2,3,4,5],
        #    [3,4,5,6],
        #    [4,5,6,5]
        #]
        #expected = [1, 5]
        #actual = find_local_minimum(numbers)
        #self.assertIn(actual, expected, 'should have found a local minima')

        ## An edge local minimum
        #numbers = [
        #    [2,2,3,4],
        #    [1,3,4,5],
        #    [3,4,5,3],
        #    [4,5,6,7]
        #]
        #expected = [1, 3]
        #actual = find_local_minimum(numbers)
        #self.assertIn(actual, expected, 'should have found a local minima')

        ## A center local minimum.
        #numbers = [
        #    [1,2,3,4],
        #    [2,3,2,5],
        #    [3,1,5,6],
        #    [4,5,6,7]
        #]
        #expected = [1, 2]
        #actual = find_local_minimum(numbers)
        #self.assertIn(actual, expected, 'should have found a local minima')

    def test_problem_8(self):
        """ Given an array of n distinct (but unsorted) elements x1,x2,...,xn
        with positive weights w1,w2,...,wn such that sum(wi)=W, where i in [1,n].

        A weighted median is an element xk for which the total weight of all
        elements with value less than xk (i.e., sum(wi), where xi<xk) is at most
        W/2, and also the total weight of elements with value larger than xk
        (i.e., sum(wi), where xi>xk) is at most W/2. Observe that there are at
        most two weighted medians.

        Show how to compute all weighted medians in O(n) worst-case time.

        Solution: Modified RSelect (randomized selection).
        """
        #def modified_partition(arr, l, r, p):
        #    arr[l], arr[p] = arr[p], arr[l]
        #    pos = l # pos denotes the position of the pivot.
        #    i = pos + 1
        #    for j in xrange(pos+1, r+1):
        #        if arr[j][1] < arr[pos][1]:
        #            arr[i], arr[j] = arr[j], arr[i]
        #            i += 1
        #    # Finally move the pivot from the first position into it's correct order.
        #    (arr[i-1], arr[pos]) = (arr[pos], arr[i-1])
        #    return (i - 1)

        #def compute_weight(start_weight, arr, pivot):
        #    if pivot is 0:
        #        return start_weight
        #    return sum(i for __, i in arr)

        #def modified_randomized_select(arr, left, right, weight, left_weight, right_weight):
        #    pivot = random.randint(left, right)
        #    pivot = modified_partition(arr, left, right, pivot)

        #    if pivot is 0:
        #        tmp_left_weight = left_weight
        #    else:
        #        tmp_left_weight = left_weight + sum(i for __, i in arr[:pivot-1])
        #    tmp_right_weight = right_weight + sum(i for __, i in arr[pivot+1:])

        #    if tmp_left_weight <= weight/2 and tmp_right_weight <= weight/2:
        #        return arr[pivot]
        #    elif tmp_left_weight > weight/2:
        #        return modified_randomized_select(arr, left, pivot, weight, left_weight, tmp_right_weight)
        #    elif tmp_right_weight > weight/2:
        #        return modified_randomized_select(arr, pivot, right, weight, tmp_left_weight, right_weight)

        #pairs = [('a', 5), ('b', 1), ('c', 3), ('d', 7),
        #         ('e', 4), ('f', 8), ('g', 2), ('h', 6)]
        #actual = modified_randomized_select(pairs, 0, len(pairs)-1, 30, 0, 0)
        #self.assertIn(actual, [('h', 6), ('d', 7)], 'should find the weighted median')

    def test_problem_11(self):
        """ In the 2SAT problem, you are given a set of clauses, where each
        clause is the disjunction of two literals (a literal is a Boolean
        variable or the negation of a Boolean variable). You are looking for a
        way to assign a value "true" or "false" to each of the variables so
        that all clauses are satisfied --- that is, there is at least one true
        literal in each clause. For this problem, design an algorithm that
        determines whether or not a given 2SAT instance has a satisfying
        assignment. (Your algorithm does not need to exhibit a satisfying
        assignment, just decide whether or not one exists.) Your algorithm
        should run in O(m+n) time, where m and n are the number of clauses and
        variables, respectively. [Hint: strongly connected components.]

        Solution: strongly connected components on a graph representation of
        the set of clauses: the vertices are variables, the edges are ORs. A
        solution exists iff there is no variable that belongs to the same SCC
        as it's negotiation.

        See http://en.wikipedia.org/wiki/2-satisfiability

        Example:
        (x_0 or x_2) and (x_0 or not x_3) and (x_1 or not x_3) and (x_1 or not x_4) and
        (x_2 or not x_4) and (x_0 or  not x_5) and (x_1 or not x_5) and (x_2 or not x_5) and
        (x_3 or x_6) and (x_4 or x_6) and (x_5 or x_6).
        """
        def is_2sat_solution(g):
            connected_components = scc(g)
            for vertices in connected_components:
                # Performance boost: a set in python uses hashtables
                # (unlike a list which uses an array) so lookup is O(1)
                s = set(vertices)
                for vertex in s:
                    if '!{vertex}'.format(vertex=vertex) in s:
                        return False
            return True

        g = Graph.build(edges=[('x0', 'x2'), ('x0', '!x3'), ('x1', '!x3'),
            ('x1', 'x4'), ('x2', '!x4'), ('x0', '!x5'), ('x1', '!x5'),
            ('x2', '!x5'), ('x3', 'x6'), ('x4', 'x6'), ('x5', 'x6')],
            directed=True)
        self.assertTrue(is_2sat_solution(g), 'should have a solution')

    def test_problem_12(self):
        """ In lecture we define the length of a path to be the sum of the
        lengths of its edges. Define the bottleneck of a path to be the maximum
        length of one of its edges. A mininum-bottleneck path between two
        vertices s and t is a path with bottleneck no larger than that of any
        other s-t path. Show how to modify Dijkstra's algorithm to compute a
        minimum-bottleneck path between two given vertices. The running time
        should be O(mlogn), as in lecture.

        Solution: Dijkstra but instead of keeping the Dijkstra score for each
        node, store the bottleneck of the path thus far. Always pick the path
        with the shortest bottleneck.
        """

    def test_problem_13(self):
        """ We can do better. Suppose now that the graph is undirected. Give
        a linear-time (O(m)) algorithm to compute a minimum-bottleneck path
        between two given vertices.

        Solution: ?
        """

    def test_problem_14(self):
        """ What if the graph is directed? Can you compute a minimum-bottleneck
        path between two given vertices faster than O(mlogn)?
        """
