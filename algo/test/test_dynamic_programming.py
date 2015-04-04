# -*- conding:utf-8 -*-

import unittest

from src.dynamic_programming import max_weighted_independent_set_in_path_graph, \
                    knapsack, sequence_alignment, optimal_binary_search_tree, \
                    binomial_coefficient


class DynamicProgrammingTest(unittest.TestCase):

    def test_max_weighted_independent_set_in_path_graph(self):
        weights = [1, 4, 5, 4]

        actual = max_weighted_independent_set_in_path_graph(weights)
        expected = [8, [4, 4]]
        self.assertEqual(actual, expected, 'should compute the max weight '
                                           'of the independent set of vertices')

    def test_max_weighted_independent_set_in_path_graph_2(self):
        weights = [1, 4, 5, 4, 6, 3, 9]

        actual = max_weighted_independent_set_in_path_graph(weights)
        expected = [21, [1,5,6,9]]
        self.assertEqual(actual, expected, 'should compute the max weight '
                                           'of the independent set of vertices')

    def test_knapsack(self):
        items = [('a', 3, 2), ('b', 4, 4), ('c', 2, 4), ('d', 1, 4)]
        capacity = 6
        (max_value, picked_items) = knapsack(items, capacity)

        expected_value = 7
        self.assertEqual(max_value, expected_value,
            'max value for the given capacity')

        #expected_items = [('a', 3, 2), ('b', 4, 4)]
        #self.assertEqual(picked_items, expected_items,
        #    'should have picked the correct items')

    def test_sequence_alignment(self):

        def gap_penalty():
            return 10

        def mismatch_penalty(x, y):
            if x == y:
                return 0
            return 5

        X = 'AGGGCT'
        Y = 'AGGCA'
        actual = sequence_alignment(X, Y, mismatch_penalty, gap_penalty)
        expected = 15 # one gap and one mismatch.
        self.assertEqual(actual, expected, 'strings are pretty close')

        X = 'AGGCA'
        Y = 'AGGCA'
        actual = sequence_alignment(X, Y, mismatch_penalty, gap_penalty)
        expected = 0
        self.assertEqual(actual, expected, 'strings are identical')

    def test_optimal_binary_search_tree(self):
        frequencies = [0.8, 0.1, 0.1]
        optimal = 0.9
        actual = optimal_binary_search_tree(frequencies)
        self.assertEqual(optimal, actual, 'should not return the best tree')


    def test_binomial_coefficient(self):
        actual = binomial_coefficient(2, 4)
        self.assertEqual(actual, expected, 'should compute the correct value')

