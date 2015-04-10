#-*- coding: utf-8 -*-

import unittest

from src.graph import Graph
from src.vertex_cover import vertex_cover


class VertexCoverTest(unittest.TestCase):

    def x_test_vertex_cover_for_a_star_graph(self):
        """ Given this graph:
             (b)(c)(d)
               \ | /
            (i)-(a)-(e)
               / | \
             (h)(g)(f)

            TODO Fix this!
        """
        g = Graph.build(edges=[
            ('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'),
            ('a', 'f'), ('a', 'g'), ('a', 'h'), ('a', 'i')
        ], directed=False)
        actual = vertex_cover(g)
        expected = ['a']
        self.assertEqual(actual, expected, 'should compute vertex cover')

    def x_test_vertex_cover_for_a_clique_graph(self):
        """ Given this graph:
            (a)---(b)
             | \  /|
             |  X  |
             | / \ |
            (c)---(d)

            TODO Fix this!
        """
        g = Graph.build(edges=[
            ('a', 'b'), ('a', 'c'), ('a', 'd'),
            ('b', 'd'), ('b', 'c'), ('d', 'c')
        ], directed=False)
        actual = vertex_cover(g)
        expected = ['a', 'b', 'c', 'c']
        self.assertEqual(actual, expected, 'should compute vertex cover')


