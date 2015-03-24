# -*- coding: utf8 -*-

import unittest
import math

from src.clustering import single_link, cluster_k_means


class Clustering(unittest.TestCase):

    def test_cluster_using_distance_function(self):
        """ The point space looks like this:
        | *a(9,1)
        |                                *e(8,8)
        |                          *c(7,7)
        |
        |
        |
        |
        |                          *d(7,3)
        |                                *f(8,2)
        | *b(1,1)
        +--------------------------------------------->
        """
        points = [(1,9,'a'), (1,1,'b'), (7,7,'c'), (8,8,'e'), (7,3,'d'), (8,2,'f')]

        def distance(x, y):
            return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

        actual = single_link(points, 4, distance)
        expected = {
            (1, 1, 'b'): [(1, 1, 'b')],
            (1, 9, 'a'): [(1, 9, 'a')],
            (7, 3, 'd'): [(7, 3, 'd'), (8, 2, 'f')],
            (7, 7, 'c'): [(7, 7, 'c'), (8, 8, 'e')]
        }
        self.assertEqual(actual, expected, 'should return correct clusters')

        actual = single_link(points, 3, distance)
        expected = {
            (1, 1, 'b'): [(1, 1, 'b')],
            (1, 9, 'a'): [(1, 9, 'a')],
            (7, 7, 'c'): [(7, 7, 'c'), (7, 3, 'd')]
        }
        self.assertEqual(actual, expected, 'should return correct clusters')

    def test_cluster_k_means(self):
        points = [(1,9,'a'), (1,1,'b'), (7,7,'c'), (8,8,'e'), (7,3,'d'), (8,2,'f')]
        def distance(x, y):
            return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

        clusters = cluster_k_means(points, 4, distance, num_iterations=30)
        actual = clusters.values()

        self.assertIn([(1, 9, 'a')], actual, 'node a is in its own cluster')
        self.assertIn([(7, 7, 'c'), (8, 8, 'e')], actual, 'nodes c and e form a cluster')
        self.assertIn([(1, 9, 'a')], actual, 'node a is in its own cluster')
        self.assertIn([(1, 1, 'b')], actual, 'nodes b is in its own cluster')
