# -*- coding: utf-8 -*-

import unittest

from src.bfs_shortest_path import bfs_shortest_path_distance
import src.graph


class TestBfsShortestPath(unittest.TestCase):

    def test_bfs_shortest_path_distance(self):
        """ Compute the shortest path distance from start to end vertices.
            /(a)--(c)--(e)
          /     /  |  /
        (s)--(b)--(d)
        """
        vertices = ['s', 'a', 'b', 'c', 'd', 'e']
        edges = [('s', 'a'), ('s', 'b'), ('a', 'c'),
                 ('c', 'b'), ('c', 'd'), ('d', 'e')]
        g = graph.Graph(vertices, edges)

        expected = 3
        actual = bfs_shortest_path_distance(g, 's', 'e')
        assert.equal(actual, expected, 'should compute correct distance')
