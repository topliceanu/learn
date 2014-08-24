# -*- coding: utf-8 -*-

import unittest

from src.graph import Graph
from src.minimum_cut import pick_random_edge, contract, minimum_cut


class MinimumCutTest(unittest.TestCase):

    def test_pick_random_edge(self):
        g = Graph.build(edges=[(1,2), (2,3), (3,1)])
        edge = pick_random_edge(g)
        self.assertTrue(edge, 'should return an edge')

    def test_contract(self):
        g = Graph.build(edges=[(1,2), (2,3), (3,1)])
        g = contract(g, (1,2))

        self.assertIn('1_2', g.table, '1 and 2 have fused')
        self.assertIn(3, g.table['1_2'], '1 and 2 have fused')
        self.assertIn(3, g.table, '1 and 2 have fused')
        self.assertIn('1_2', g.table[3], '1 and 2 have fused')
        self.assertNotIn(2, g.get_vertices(), 'no more 2 vertex')

    def test_minimum_cut(self):
        """ Tests that the following graph is split correctly.
        (a)--(c)
         |  / |
        (b)--(d)
        """
        g = Graph.build(edges = [('a', 'b'), ('a', 'c'),
                                 ('b', 'c'), ('b', 'd'),
                                 ('c', 'd')])
        compacted = minimum_cut(g)
        self.assertEqual(len(compacted.get_vertices()), 2,
                'should have compacted to only 2 vertices')

    def test_minimum_cut_for_larger_graph(self):
        """ Test minimum cut for a larger graph.
        (a)--(b)--(e)--(f)
         |  X |    |  X |
        (c)--(d)--(g)--(h)
        """
        g = Graph.build(edges = [('a', 'b'), ('a', 'c'), ('a', 'd'),
                                 ('b', 'c'), ('b', 'd'), ('b', 'e'),
                                 ('c', 'd'), ('d', 'g'),
                                 ('e', 'g'), ('e', 'f'), ('e', 'h'),
                                 ('f', 'g'), ('f', 'h'), ('g', 'h')])
        compacted = minimum_cut(g)
        self.assertEqual(len(compacted.get_vertices()), 2,
                'should have compacted to only 2 vertices')
