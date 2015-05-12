# -*- coding: utf-8 -*-

import unittest

from src.graph import Graph
from src.depth_first_search import dfs, dfs_paths



class DepthFirstSearch(unittest.TestCase):

    def test_depth_first_search_for_simple_connected_non_directed_graph(self):
        """ Given this graph to explore:
            /-(a)---(d)---(e)
          /    |     |    /
        (s)---(b)---(c)-/
        """
        g = Graph.build(edges=[('s', 'a'), ('s', 'b'), ('a', 'b'), ('a', 'd'),
                               ('b', 'c'), ('d', 'c'), ('d', 'e'), ('c', 'e')],
                        directed=False)
        path = dfs(g, 's')

    def test_depth_first_search_returning_paths(self):
        """ Given this graph to explore:
            />(a)-->(d)-->(e)
          /    |v    |v   /^
        (s)-->(b)-->(c)-/
        """
        g = Graph.build(edges=[('s', 'a'), ('a', 'd'), ('d', 'e'), ('s', 'b'),
                               ('b', 'c'), ('c', 'e'), ('a', 'b'), ('d', 'c')],
                        directed=True)
        paths = dfs_paths(g, 's', 'e')
        expected_paths = [
            ['s', 'b', 'c', 'e'], ['s', 'a', 'd', 'e'],
            ['s', 'a', 'd', 'c', 'e'], ['s', 'a', 'b', 'c', 'e']
        ]
        self.assertEqual(paths, expected_paths,
                'should produce the expected paths')

