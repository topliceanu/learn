# -*- coding: utf-8 -*-

import unittest

from src.graph import Graph
from src.bfs_connected_components import bfs_connected_components


class TestBfsConnectedComponents(unittest.TestCase):

    def test_bfs_connected_components(self):
        """ Test the connected graphs algorithm for the folowing setup.
        (1)--(3)    (2)--(4)      (6)
          \  /                   /  \
          (5)                  (8) (10)
         /   \
        (7)  (9)
        This should return the nodes in three subgraphs.
        """
        edges = [(1,3), (1,5), (3,5), (5,7), (5,9), (2,4), (6,8), (6,10)]
        g = Graph.build(edges=edges)

        expected = [[1,3,5,9,7], [2,4], [6,8,10]]
        actual = bfs_connected_components(g)
        self.assertEqual(actual, expected, 'should correctly determine subgraphs')
