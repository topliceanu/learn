# -*- coding: utf-8 -*-

import unittest

import src.graph
from src.minimum_cut import pick_random_edge, contract, minimum_cut


class MinimumCutTest(unittest.TestCase):

    def test_pick_random_edge(self):
        pass

    def test_contract(self):
        pass

    def test_minimum_cut(self):
        """ Tests that the following graph is split correctly.
        (a)--(c)
         |  / |
        (b)--(d)
        """
        g = graph.Graph(['a', 'b', 'c', 'd'], [('a', 'b'), ('a', 'c'),
                                               ('b', 'c'), ('b', 'd'),
                                               ('c', 'd')])
        left, right = minimum_cut(g)
        print 'left: ', left
        print 'right: ', right

    def test_minimum_cut_for_larger_graph(self):
        """ Test minimum cut for a larger graph.
        (a)--(b)--(e)--(f)
         |  X |    |  X |
        (c)--(d)--(g)--(h)
        """
        pass
