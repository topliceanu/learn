# -*- coding: utf-8 -*-

import unittest

from recursion_and_dynamic_programming import triple_step, robot_in_a_grid, \
    magic_index, power_set, permutations_without_dups, permutations_with_dups, \
    parens, eight_queens

class TestRecursingAndDynamicProgramming(unittest.TestCase):
    def test_triple_step(self):
        tests = [
            (1, 1),
            (2, 2),
            (3, 4),
            (4, 7),
        ]
        for test in tests:
            actual = triple_step(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, 'failed test={}, actual={}'
                    .format(test, actual))

    def test_robot_in_a_grid(self):
        grid = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
        ]
        expected = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3)]
        actual = robot_in_a_grid(grid)
        self.assertEqual(actual, expected,
                'failed with actual={}, expected={}'
                .format(actual, expected))

    def test_magic_index(self):
        tests = [
            ([], []),
            ([0], [0]),
            ([0, 1, 2, 3], [0, 1, 2, 3]),
            ([0, 1, 4, 5, 6], [0, 1]),
            ([1, 1, 3, 3, 4], [1, 3, 4]),
        ]
        for test in tests:
            actual = magic_index(test[0])
            expected = test[1]
            self.assertEqual(actual, expected,
                'failed test={} with actual={}'.format(test, actual))

    def test_power_set(self):
        tests = [
            ([], [[]]),
            ([1], [[], [1]]),
            ([1, 2], [[], [2], [1], [2, 1]]),
            ([1, 2, 3], [[], [3], [2], [3, 2], [1], [3, 1], [2, 1], [3, 2, 1]]),
        ]
        for test in tests:
            actual = power_set(test[0])
            expected = test[1]
            self.assertEqual(len(actual), len(expected),
                    'do not have the same length')
            self.assertEqual(actual, expected,
                    'fail test={} with actual={}'
                    .format(test, actual))

    def test_permutations_without_dups(self):
        tests = [
            ("", []),
            ("a", ["a"]),
            ("ab", ["ab", "ba"]),
            ("aa", ["aa", "aa"]), # duplicates
        ]
        for test in tests:
            actual = permutations_without_dups(test[0])
            expected = test[1]
            self.assertEqual(actual, expected,
                    'fail test={} with actual={}'
                    .format(test, actual))

    def test_permutations_with_dups(self):
        tests = [
            ("", []),
            ("a", ["a"]),
            ("ab", ["ab", "ba"]),
            ("aa", ["aa"]), # duplicates
            ("aab", ['aab', 'aba', 'aba', 'baa']), # duplicates
            # TODO FIXME
            ("aabb", ['aabb', 'abab', 'abba', 'abab', 'baab', 'baba', 'abba', 'baba', 'bbaa']) # duplicates
        ]
        for test in tests:
            actual = permutations_with_dups(test[0])
            expected = test[1]
            self.assertEqual(actual, expected,
                    'fail test={} with actual={}'
                    .format(test, actual))

    def test_parens(self):
        tests = [
            (0, []),
            (1, ['()']),
            (2, ['()()', '(())']),
            (3, ['()()()', '(()())', '()(())', '(())()', '((()))']),
        ]
        for test in tests:
            actual = parens(test[0])
            expected = test[1]
            self.assertEqual(actual, expected,
                    'fail test={} with actual={}'
                    .format(test, actual))

    def test_eight_queens(self):
        solutions = eight_queens()
        #self.assertEquals(len(solutions), 10, 'failed with solutions={}'.format(solutions))
