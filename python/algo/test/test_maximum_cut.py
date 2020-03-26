# -*- coding: utf-8 -*-

import unittest

from src.graph import Graph
from src.maximum_cut import maximum_cut, maximum_cut_for_bipartite_graph


class MaximumCut(unittest.TestCase):

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

    def test_maximum_cut_for_larger_bipartite_graphs(self):
        """ A sligthly larger graph:
        (a)   (c)
         | \  /|
         |  x  |
         | / \ |
        (b)   (d)
         | \  /|
         |  x  |
         | / \ |
        (e)   (f)
        """
        g = Graph.build(edges=[('a', 'b'), ('a', 'd'), ('c', 'b'), ('c', 'd'),
                               ('b', 'e'), ('b', 'f'), ('d', 'e'), ('d', 'f')],
                        directed=False)
        (left, right) = maximum_cut_for_bipartite_graph(g)
        self.assertIn(set(left), [set(['a', 'c', 'e', 'f']), set(['b', 'd'])])
        self.assertIn(set(right), [set(['a', 'c', 'e', 'f']), set(['b', 'd'])])
        self.assertNotEqual(left, right, 'not the same subsets')

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

    def test_weighted_maximum_cut(self):
        """ Given the following weighted graph.
            (u)-3-(v)
             | \  / |
             | 5\/1 4
             2  /\  |
             | /  \ |
            (w)-6-(x)
        """
        g = Graph.build(edges=[
                ('u', 'v', 3), ('u', 'w', 2), ('u', 'x', 5),
                ('v', 'x', 4),('w', 'x', 6)],
            directed=False)
        (left, right) = maximum_cut(g)
        self.assertEqual(2, len(left), 'left should contain 2 vertices')
        self.assertEqual(2, len(right), 'right should contain 2 vertices')
