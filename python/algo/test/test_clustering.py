# -*- coding: utf8 -*-

import unittest
import math

from src.clustering import single_link, cluster_k_means, cluster_graph
from src.graph import Graph


def distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


class TestClustering(unittest.TestCase):

    def test_cluster_using_single_link_method(self):
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
            (7, 7, 'c'): [(7, 7, 'c'), (8, 8, 'e'), (7, 3, 'd'), (8, 2, 'f')]
        }
        self.assertEqual(actual, expected, 'should return correct clusters')

    def test_cluster_graph(self):
        """ The graph is specified in distances but it should look something
        like this:
        | *a
        |                                *e
        |                          *c
        |
        |
        |
        |
        |                          *d
        |                                *f
        | *b
        +--------------------------------------------->
        """
        g = Graph.build(edges=[
            ('a', 'e', 8), ('a', 'c', 7), ('a', 'd', 9), ('a', 'f', 10), ('a', 'b', 8),
            ('e', 'f', 6), ('e', 'd', 5), ('e', 'b', 10), ('e', 'c', 1),
            ('c', 'f', 5), ('c', 'd', 4), ('c', 'b', 9),
            ('d', 'f', 1), ('d', 'b', 7),
            ('f', 'b', 8)
        ], directed=False)

        (clusters, distances) = cluster_graph(g, 4)
        expectedClusters = {
            'a': ['a'],
            'c': ['c', 'e'],
            'b': ['b'],
            'd': ['d', 'f']
        }
        expectedDistances = {
            ('b', 'c'): 9,
            ('c', 'd'): 4,
            ('a', 'd'): 9,
            ('a', 'b'): 8,
            ('a', 'c'): 7,
            ('b', 'd'): 7
        }
        self.assertEqual(clusters, expectedClusters,
            'should return correct clusters')
        self.assertEqual(distances, expectedDistances,
            'should compute distances')

        (clusters, distances) = cluster_graph(g, 3)
        expectedClusters = {
            'a': ['a'],
            'b': ['b'],
            'c': ['c', 'e', 'd', 'f']
        }
        expectedDistances = {
            ('b', 'c'): 7,
            ('a', 'b'): 8,
            ('a', 'c'): 7
        }
        self.assertEqual(clusters, expectedClusters,
            'should return correct clusters')
        self.assertEqual(distances, expectedDistances,
            'should compute distances')

    def test_cluster_k_means(self):
        points = [(1,9,'a'), (1,1,'b'), (7,7,'c'), (8,8,'e'), (7,3,'d'), (8,2,'f')]

        clusters = cluster_k_means(points, 4, distance, num_iterations=30)
        actual = clusters.values()

        self.assertIn([(1, 9, 'a')], actual, 'node a is in its own cluster')
        self.assertIn([(7, 7, 'c'), (8, 8, 'e')], actual, 'nodes c and e form a cluster')
        self.assertIn([(1, 9, 'a')], actual, 'node a is in its own cluster')
        self.assertIn([(1, 1, 'b')], actual, 'nodes b is in its own cluster')
