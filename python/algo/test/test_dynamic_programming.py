# -*- conding:utf-8 -*-

import unittest

from src.graph import Graph
from src.dynamic_programming import max_weighted_independent_set_in_path_graph, \
                sequence_alignment, optimal_binary_search_tree, \
                binomial_coefficient, maximum_monotone_sequence, min_coins, \
                zig_zag, bad_neighbours, linear_partition, \
                max_weighted_independent_set_in_tree, longest_common_subsequence


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

    def test_max_weighted_independed_set_in_tree(self):
        tree = Graph.build(directed=True, edges=[
                ('r', 'a'), ('r', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'),
                ('d', 'h'), ('d', 'i'), ('b', 'f'), ('b', 'g'), ('g', 'j')
            ])
        values = {'r': 10, 'a': 5, 'c': 3, 'd': 4, 'e': 9, 'h': 2, 'i': 7,
                  'b': 8, 'f': 3, 'g': 11, 'j': 8}
        for (vertex, value) in values.iteritems():
            tree.set_vertex_value(vertex, value)

        (actual_max_weight, actual_vertex_set) = \
            max_weighted_independent_set_in_tree(tree)

        expected_max_weight = 40
        expected_vertex_set = set(['c', 'e', 'g', 'f', 'i', 'h', 'r'])
        self.assertEqual(actual_max_weight, expected_max_weight, \
                'should compute the correct max weight')
        self.assertEqual(actual_vertex_set, expected_vertex_set, \
                'should compute the correct included vertex set')

    def test_sequence_alignment(self):
        def gap_penalty():
            return 10

        def mismatch_penalty(x, y):
            if x == y:
                return 0
            return 5

        X = 'ABC'
        Y = 'AC'
        (penalty, X_mod, Y_mod) = sequence_alignment(X, Y, mismatch_penalty, gap_penalty)
        self.assertEqual(penalty, 10, 'one gap')
        self.assertEqual(X_mod, 'ABC', 'same as input')
        self.assertEqual(Y_mod, 'A-C', 'added a gap for alignment')

        X = 'AGGGCT'
        Y = 'AGGCA'
        (penalty, X_mod, Y_mod) = sequence_alignment(X, Y, mismatch_penalty, gap_penalty)
        self.assertEqual(penalty, 15, 'one gap and one mismatch')
        self.assertEqual(X_mod, 'AGGGCT', 'same as input')
        self.assertEqual(Y_mod, 'A-GGCA', 'added a gap for alignment')

        X = 'AGGCA'
        Y = 'AGGCA'
        (penalty, X_mod, Y_mod) = sequence_alignment(X, Y, mismatch_penalty, gap_penalty)
        self.assertEqual(penalty, 0, 'strings are identical')
        self.assertEqual(X_mod, X, 'no changes')
        self.assertEqual(Y_mod, Y, 'no changes')

        X = 'AB'
        Y = 'CAB'
        (penalty, X_mod, Y_mod) = sequence_alignment(X, Y, mismatch_penalty, gap_penalty)
        self.assertEqual(penalty, 10, 'completely different')
        self.assertEqual(X_mod, '-AB', 'one gap are inserted in the front')
        self.assertEqual(Y_mod, 'CAB', 'no changes')

    def test_longest_common_subsequence(self):
        str1 = 'alexandru'
        str2 = 'topliceanu'
        (penalty, common) = longest_common_subsequence(str1, str2)
        expected_penalty = 12
        print '>>>>>>>>', penalty

    def test_maximum_monotone_subsequence(self):
        s = '243517698'
        (max_length, max_sequence) = maximum_monotone_sequence(s)
        self.assertEqual(max_length, 5, 'should be the max sequence')
        possible_solutions = ['24568', '23569', '23579', '23578'
                              '24568', '24569', '24579', '24578']
        self.assertIn(max_sequence, possible_solutions,
            'should be one of the solutions')

    def test_linear_partitions(self):
        values = [100, 200, 300, 400, 500, 600, 700, 800, 900]
        num_partitions = 3
        expected_min_max_sum = 1700
        expected_partitions = [[100, 200, 300, 400, 500], [600, 700], [800, 900]]

        (min_max_sum, partitions) = linear_partition(values, num_partitions)
        self.assertEqual(min_max_sum, expected_min_max_sum,
            'should compute the expected min max sum of partition values')
        self.assertEqual(partitions, expected_partitions,
            'should return the correct partitions')

    def test_optimal_binary_search_tree(self):
        items = [('a', 0.1), ('b', 0.1), ('c', 0.8)]
        (optimal_search_cost, pre_order) = optimal_binary_search_tree(items)

        expected_optimal_cost = 1.3
        self.assertEqual(optimal_search_cost, expected_optimal_cost,
            'should not return the best tree')

        expected_pre_order = [('c', 0.8), ('a', 0.1), ('b', 0.1)]
        self.assertEqual(pre_order, expected_pre_order,
            'the vertices are in preorder so to easily to build an optimal BST')

    def test_optimal_binary_search_tree_2(self):
        items = [('1', 0.05), ('2', 0.4), ('3', 0.08), ('4', 0.04),
                 ('5', 0.1), ('6', 0.1), ('7', 0.223)]
        (optimal_search_cost, pre_order) = optimal_binary_search_tree(items)

        expected_optimal_cost = 2.166
        self.assertEqual(optimal_search_cost, expected_optimal_cost,
            'should not return the best tree')

        expected_pre_order = [('2', 0.4), ('1', 0.05), ('7', 0.223),
                              ('5', 0.1), ('3', 0.08), ('4', 0.04), ('6', 0.1)]
        self.assertEqual(pre_order, expected_pre_order,
            'the vertices are in preorder so to easily to build an optimal BST')

    def test_optimal_binary_search_tree_from_final_exam(self):
        items = [('1', 0.2), ('2', 0.05), ('3', 0.17), ('4', 0.1),
                 ('5', 0.2), ('6', 0.03), ('7', 0.25)]
        (optimal_search_cost, _) = optimal_binary_search_tree(items)

        expected_optimal_cost = 2.23
        self.assertEqual(optimal_search_cost, expected_optimal_cost,
            'should not return the best tree')

    def test_binomial_coefficient(self):
        actual = binomial_coefficient(2, 4)
        expected = 6
        self.assertEqual(actual, expected, 'should compute the correct value')

    def test_min_coins(self):
        coins = [1, 3, 5]
        total = 11
        (min_num_coins, picked_coins) = min_coins(coins, total)
        self.assertEqual(min_num_coins, 3, 'only three coins')
        self.assertEqual(set(picked_coins), set([5,5,1]), 'picked the correct coins')

    def test_is_zig_zag(self):
        numbers = [1,7,4,9,2,5]
        (max_length, subsequence) = zig_zag(numbers)
        self.assertEqual(max_length, 6, 'the whole sequence is zig-zag')
        self.assertEqual(subsequence, numbers, 'the whole sequence is zig-zag')

        numbers = [1,4,7,2,5,1]
        (max_length, subsequence) = zig_zag(numbers)
        self.assertEqual(max_length, 5, 'the whole sequence is zig-zag')
        possibilities = [[1,4,2,5,1], [1,7,2,5,1]]
        self.assertIn(subsequence, possibilities, 'one of the subsequences')

        sets = [
            [ 1, 7, 4, 9, 2, 5 ],
            [ 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 ],
            [ 44 ],
            [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
            [ 70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19,
              7, 5, 5, 5, 1000, 32, 32 ],
            [ 374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
              600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
              67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
              477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
              249, 22, 176, 279, 23, 22, 617, 462, 459, 244 ]
        ]
        expected = [6, 7, 1, 2, 8, 36]

        for index in range(len(sets)):
            (max_length, seq) = zig_zag(sets[index])
            self.assertEqual(max_length, expected[index], 'correct value')

    def test_bad_neighbours(self):
        sets = [
            {'data': [10,3,2,5,7,8], 'max': 19, 'picked': [10,2,7]},
            {'data': [1,2,3,4,5,1,2,3,4,5], 'max': 16, 'picked': [3,5,3,5]}
        ]
        for i in range(len(sets)):
            (max_value, picked_values) = bad_neighbours(sets[i]['data'])
            self.assertEqual(max_value, sets[i]['max'],
                'computes max possible obtainable donations')
            self.assertEqual(picked_values, sets[i]['picked'],
                'computes the selected donations')
