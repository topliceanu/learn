# -*- coding: utf-8 -*-

import unittest

from src.deterministic_selection import deterministic_selection, \
    deterministic_pick_pivot, pick_middle, split_chunks


class TestDeterministicSelection(unittest.TestCase):

    def test_split_chunks(self):
        a = [1,8,3,2,9,5,4,7,6,0,11,12,13]
        actual = split_chunks(a, 5)
        expected = [[1,8,3,2,9],
                    [5,4,7,6,0],
                    [11,12,13]]
        self.assertEqual(actual, expected,
                'should split input in equal chunks')

    def test_pick_middle(self):
        a = [1,8,3,2,9,5,4,7,6,0,11,12,13]
        actual = pick_middle(a)
        expected = 8
        self.assertEqual(actual, expected, 'should pick the correct middle')

    def test_deterministic_pick_pivot(self):
        a = [11,8,3,12,9,5,4,7,6,0,1,2,13]
        actual = deterministic_pick_pivot(a)
        expected = 2
        self.assertEqual(actual, expected, 'should pick the best pivot')

        a = [10, 8, 2, 4]
        actual = deterministic_pick_pivot(a)
        expected = 1
        self.assertEqual(actual, expected, 'should pick the best pivot')

    def test_deterministic_selection(self):
        arr = [10, 8, 2, 4]
        actual = deterministic_selection(arr, len(arr), 2)
        expected = 8
        self.assertEqual(actual, expected, 'should select the third position')

    def test_deterministic_selection_to_produce_median(self):
        arr = [8,2,1,7,4,5,3,0,6,9]
        actual = deterministic_selection(arr, len(arr), 5)
        expected = 5
        self.assertEqual(actual, expected, 'should produce the arrays median')
