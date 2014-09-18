# -*- coding: utf-8 -*-

import unittest

from src.closest_pair import closest_pair


class TestClosestPair(unittest.TestCase):

    def test_closest_pair(self):
        """ Compute the closest pair of a set of given pairs. """
        points = [(1,1), (1,2), (1,4), (1,6), (1, 10), (1,16), (1,26)]
        actual = closest_pair(points)
        expected = [(1,1), (1,2)]
        self.assertItemsEqual(actual, expected, 'compute expected closest points')

    def test_closest_non_obvious_pair(self):
        points = [(9, 3), (-2, -2), (6, 4), (-6, -1), (3, 5), (-4, 2)]
        actual = closest_pair(points)
        expected = [(3,5), (6,4)]
        self.assertItemsEqual(actual, expected, 'compute expected closest points')
