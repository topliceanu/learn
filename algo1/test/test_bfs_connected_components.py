# -*- coding: utf-8 -*-

import unittest

import src.graph
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
        vertices = [1,2,3,4,5,6,7,8,9,10]
        edges = [(1,3), (1,5), (3,5), (5,7), (5,9), (2,4), (6,8), (6,10)]
        g = graph.Graph(vertices, edges)

        expected = [[1,3,5,7,9], [2,4], [6,8,10]]
        actual = bfs_connected_components(vertices, edges)
        self.assertEqual(actual, expected, 'should correctly determine subgraphs')
