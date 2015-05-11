# -*- coding: utf-8 -*-

import unittest

from src.graph import Graph
from src.maximum_cut import maximum_cut, maximum_cut_for_bipartite_graph


class MaximumCut(unittest.TestCase):

    def test_maximum_cut(self):
        """ Given a graph:
        (u)----(v)
         | \  / |
         |  \/  |
         |  /\  |
         | /  \ |
        (w)---(x)

        """
        g = Graph.build(edges=[
            ('u', 'v'), ('u', 'w'), ('u', 'x'), ('v', 'x'),('w', 'x')],
            directed=False)
        (left, right) = maximum_cut(g)
        expected = [{'u', 'v'}, {'w', 'x'}, {'x', 'u'}, {'w', 'v'}]
        self.assertNotEqual(left, right, 'no common vertices between cuts')
        self.assertIn(set(left), expected, 'should correctly split the graph')
        self.assertIn(set(right), expected, 'should correctly split the graph')

    def test_maximum_cut_for_bipartite_graphs(self):
        """ Given the following bipartite graph.
            (a)-----(b)
              \
               \----(c)
            (d)-----(e)
                    /
            (f)----/
              \
               \----(g)
        """
        g = Graph.build(edges=[('a', 'b'), ('a', 'c'),
                               ('d', 'e'), ('f', 'e'), ('f', 'g')],
                        directed=False)

        (left, right) = maximum_cut_for_bipartite_graph(g)
        self.assertIn(len(left), [3,4], 'either 3 or 4')
        self.assertIn(len(right), [3,4], 'eighter 3 or 4')
        self.assertEqual(7, len(left)+len(right), 'no vertex counted twice')
