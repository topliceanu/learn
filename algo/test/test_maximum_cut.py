# -*- coding: utf-8 -*-

import unittest

from src.graph import Graph
from src.maximum_cut import maximum_cut


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
