# -*- coding: utf-8 -*-

import unittest

from src.closest_pair import closest_pair, euclidean_distance


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

    def test_closest_pair_from_clustering(self):
        """ The point space looks like this:
        | *a(9,1)
        |                                *e(8,8)
        |                            *c(7,7)
        |
        |
        |
        |
        |                            *d(7,3)
        |                                *f(8,2)
        | *b(1,1)
        +--------------------------------------------->
        """
        points = [(1,9,'a'), (1,1,'b'), (7,7,'c'), (8,8,'e'), (7,3,'d'), (8,2,'f')]
        actual = closest_pair(points)
        expected = ((7, 3, 'd'), (8, 2, 'f'))
        self.assertEqual(actual, expected, 'should find the first closest pair')

        points = [(1,9,'a'), (1,1,'b'), (8,2,'f'), (7,7,'c'), (8,8,'e')]
        actual = closest_pair(points)
        expected = ((7, 7, 'c'), (8, 8, 'e'))
        self.assertEqual(actual, expected, 'should find the first closest pair')

        def modified_distance(p1, p2):
            if (p1[2] in ['d', 'f'] and p2[2] in ['d', 'f']):
                dist = 100
            else:
                dist = euclidean_distance(p1, p2)
            return dist

        points = [(1,9,'a'), (1,1,'b'), (7,7,'c'), (8,8,'e'), (7,3,'d'), (8,2,'f')]
        actual = closest_pair(points, distance=modified_distance)
        expected = ((7, 7, 'c'), (8, 8, 'e'))
        self.assertEqual(actual, expected, 'should find the first closest pair')
