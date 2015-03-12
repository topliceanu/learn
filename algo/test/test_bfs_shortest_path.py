# -*- coding: utf-8 -*-

import unittest

from src.bfs_shortest_path import bfs_shortest_path_distance
from src.graph import Graph


class TestBfsShortestPath(unittest.TestCase):

    def test_bfs_shortest_path_distance(self):
        """ Compute the shortest path distance from start to end vertices.
            /(a)--(c)--(e)
          /     /  |  /
        (s)--(b)--(d)
        """
        edges = [('s', 'a'), ('s', 'b'), ('a', 'c'), ('b', 'd'),
                 ('c', 'b'), ('c', 'd'), ('c', 'e'), ('d', 'e')]
        g = Graph.build(edges=edges, directed=False)

        g = bfs_shortest_path_distance(g, 's')

        self.assertEqual(g.get_vertex_value('s'), 0, 'correct distance')
        self.assertEqual(g.get_vertex_value('a'), 1, 'correct distance')
        self.assertEqual(g.get_vertex_value('b'), 1, 'correct distance')
        self.assertEqual(g.get_vertex_value('c'), 2, 'correct distance')
        self.assertEqual(g.get_vertex_value('d'), 2, 'correct distance')
        self.assertEqual(g.get_vertex_value('e'), 3, 'correct distance')
