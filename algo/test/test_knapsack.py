# -*- conding:utf-8 -*-

import unittest

from src.knapsack import knapsack_dynamic_programming, \
                         knapsack_three_step_heuristic, \
                         knapsack_arbitrarely_close_approximation, \
                         knapsack_dynamic_programming_small_values


class KnapsackTest(unittest.TestCase):

    def test_knapsack_dynamic_programming(self):
        items = [('a', 3, 2), ('b', 4, 4), ('c', 2, 4), ('d', 1, 4)]
        capacity = 6
        (max_value, picked_items) = knapsack_dynamic_programming(items, capacity)

        expected_value = 7
        self.assertEqual(max_value, expected_value,
            'max value for the given capacity')

        expected_items = [('a', 3, 2), ('b', 4, 4)]
        self.assertEqual(set(picked_items), set(expected_items),
            'should have picked the correct items')

    def test_knapsack_three_step_heuristic(self):
        items = [('a', 3, 2), ('b', 4, 4), ('c', 2, 4), ('d', 1, 4)]
        capacity = 6
        (max_value, picked_items) = knapsack_three_step_heuristic(items, capacity)

        expected_value = 7
        self.assertEqual(max_value, expected_value,
            'max value for the given capacity')

        expected_items = [('a', 3, 2), ('b', 4, 4)]
        self.assertEqual(set(picked_items), set(expected_items),
            'should have picked the correct items')

    def test_knapsack_dynamic_programming_small_values(self):
        items = [('a', 3, 2), ('b', 4, 4), ('c', 2, 4), ('d', 1, 4)]
        capacity = 6
        (max_value, picked_items) = knapsack_dynamic_programming_small_values(items, capacity)

        expected_value = 7
        self.assertEqual(max_value, expected_value,
            'max value for the given capacity')

        expected_items = [('a', 3, 2), ('b', 4, 4)]
        self.assertEqual(set(picked_items), set(expected_items),
            'should have picked the correct items')

    def test_knapsack_arbitrarely_close_approximation(self):
        items = [('a', 3, 2), ('b', 4, 4), ('c', 2, 4), ('d', 1, 4)]
        capacity = 6
        (max_value, picked_items) = knapsack_arbitrarely_close_approximation(items, capacity)

        expected_value = 7
        self.assertEqual(max_value, expected_value,
            'max value for the given capacity')

        expected_items = [('a', 3, 2), ('b', 4, 4)]
        self.assertEqual(set(picked_items), set(expected_items),
            'should have picked the correct items')
