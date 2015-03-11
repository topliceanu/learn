# -*- coding: utf-8 -*-

import unittest

from src.graph import Graph
from src.depth_first_search import dfs



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
