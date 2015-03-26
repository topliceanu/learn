# -*- conding:utf-8 -*-

import unittest

from src.dynamic_programming import max_weighted_independent_set_in_path_graph, \
                                    knapsack, sequence_alignment


class DynamicProgrammingTest(unittest.TestCase):

    def test_max_weighted_independent_set_in_path_graph(self):
        weights = [1, 4, 5, 4]

        actual = max_weighted_independent_set_in_path_graph(weights)
        expected = [8, [4, 4]]
        self.assertEqual(actual, expected, 'should compute the max weight '
                                           'of the independent set of vertices')

    def xtest_max_weighted_independent_set_in_path_graph_2(self):
        weights = [1, 4, 5, 4, 6, 3, 9]

        actual = max_weighted_independent_set_in_path_graph(weights)
        expected = [21, [1,5,6,9]]
        self.assertEqual(actual, expected, 'should compute the max weight '
                                           'of the independent set of vertices')

    def test_knapsack(self):
        items = [('a', 3, 2), ('b', 4, 4), ('c', 2, 4), ('d', 1, 4)]
        capacity = 6

        max_value = knapsack(items, capacity)
        self.assertEqual(max_value, 7, 'max value for the given capacity')

    def test_sequence_alignment(self):
        X = 'AGGGCT'
        Y = 'AGGCA'
        actual = sequence_alignment(X,Y)
        expected = d
        self.assertEqual(actual, expected, 'strings are pretty close')

        X = 'AGGCA'
        Y = 'AGGCA'
        actual = sequence_alignment(X,Y)
        expected = 0
        self.assertEqual(actual, expected, 'strings are identical')
