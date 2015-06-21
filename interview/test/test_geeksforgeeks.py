# -*- coding: utf-8 -*-

import unittest

from geeksforgeeks import *


class TestGeeksForGeeks(unittest.TestCase):

    def test_towers_holding_water(self):
        heights = [1, 5, 3, 7, 2]
        expected = 2
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'one small gap')

        heights = [5, 1, 2, 3, 4]
        expected = 6
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'large ascending gap')

        heights = [5, 4, 3, 2, 1, 6]
        expected = 10
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'large descending gap')

        heights = [1, 3, 4, 2]
        expected = 0
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'no gap')

        heights = [5, 3, 3, 3, 4]
        expected = 3
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'large gap, multiple minima')

        heights = [5, 5, 5, 3, 4, 4]
        expected = 1
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'large gap, multiple minima')

        heights = [5, 1, 2, 3, 2, 1, 4]
        expected = 11
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'large gap, both descending and ascending')

        heights = [5, 1, 5, 2, 5, 3, 5]
        expected = 9
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'multiple small gaps')

        heights = [4, 2, 3, 1, 2, 1, 2, 1, 3, 2, 4]
        expected = 19
        actual = towers_holding_water(heights)
        self.assertEqual(expected, actual, 'multiple small gaps')
