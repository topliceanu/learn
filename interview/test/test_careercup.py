# -*- coding: utf-8 -*-

import unittest

from careercup import *


class TestCareerCup(unittest.TestCase):

    def test_find_pairs_in_list(self):
        arr = [1,2,3,4,5,6,7,8]
        k = 3
        l = 2
        actual = find_pairs_in_list(arr, k, l)
        self.assertTrue(actual, 'should have found at least one pair for k,l')

    def test_farm_rain_fall(self):
        plots = [
            [2, 5, 2],
            [2, 4, 7],
            [3, 6, 9]
        ]
        expected = [
            ['A', 'B', 'B'],
            ['A', 'A', 'B'],
            ['A', 'A', 'A']
        ]
        actual = farm_rainfall(plots)
        self.assertEqual(actual, expected, 'should produce the correct syncs')

        plots = [
            [10]
        ]
        expected = [
            ['A']
        ]
        actual = farm_rainfall(plots)
        self.assertEqual(actual, expected, 'should produce the correct syncs')

        plots = [
            [1, 0, 2, 5, 8],
            [2, 3, 4, 7, 9],
            [3, 5, 7, 8, 9],
            [1, 2, 5, 4, 2],
            [3, 3, 5, 2, 1]
        ]
        expected = [
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A'],
            ['B', 'B', 'A', 'C', 'C'],
            ['B', 'B', 'B', 'C', 'C'],
            ['B', 'B', 'C', 'C', 'C']
        ]
        actual = farm_rainfall(plots)
        self.assertEqual(actual, expected, 'should produce the correct syncs')

        plots = [
            [0, 2, 1, 3],
            [2, 1, 0, 4],
            [3, 3, 3, 3],
            [5, 5, 2, 1]
        ]
        expected = [
            ['A', 'A', 'B', 'B'],
            ['A', 'B', 'B', 'B'],
            ['A', 'B', 'B', 'C'],
            ['A', 'C', 'C', 'C']
        ]
        actual = farm_rainfall(plots)
        self.assertEqual(actual, expected, 'should produce the correct syncs')
