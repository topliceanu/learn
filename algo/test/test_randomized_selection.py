# -*- coding: utf-8 -*-

import unittest

from src.randomized_selection import randomized_selection


class RandomizedSelection(unittest.TestCase):

    def test_randomized_selection(self):
        arr = [10, 8, 2, 4]
        actual = randomized_selection(arr, len(arr), 2)
        expected = 8
        self.assertEqual(actual, expected, 'should select the third position')

    def test_randomized_selection_to_produce_median(self):
        arr = [8,2,1,7,4,5,3,0,6,9]
        actual = randomized_selection(arr, len(arr), 5)
        expected = 5
        self.assertEqual(actual, expected, 'should produce the arrays median')
