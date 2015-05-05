#-*- coding: utf-8 -*-

import unittest

from src.graph import Graph
from src.vertex_cover import vertex_cover


class VertexCoverTest(unittest.TestCase):

    def test_vertex_cover_for_a_star_graph(self):
        """ Given this graph:
             (b)(c)(d)
               \ | /
            (i)-(a)-(e)
               / | \
             (h)(g)(f)
        """
        g = Graph.build(edges=[
            ('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'),
            ('a', 'f'), ('a', 'g'), ('a', 'h'), ('a', 'i')
        ], directed=False)
        actual = vertex_cover(g)
        expected = ['a']
        self.assertEqual(actual, expected, 'should compute vertex cover')

    def test_vertex_cover_for_a_clique_graph(self):
        """ Given this graph:
            (a)---(b)
             | \  /|
             |  X  |
             | / \ |
            (c)---(d)
        """
        g = Graph.build(edges=[
            ('a', 'b'), ('a', 'c'), ('a', 'd'),
            ('b', 'd'), ('b', 'c'), ('d', 'c')
        ], directed=False)
        actual = vertex_cover(g)
        expected = ['a', 'b', 'c', 'd']
        self.assertEqual(set(actual), set(expected),
            'should compute vertex cover')

    def test_vertex_cover_for_a_larger_clique_graph(self):
        """ Given a clique graph, ie. a complete graph. with vertices:
                (a), (b), (c), (d), (e), (f), (g), (h)
        """
        g = Graph.build(edges=[
            ('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('a', 'f'), ('a', 'g'), ('a', 'h'),
            ('b', 'c'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('b', 'g'), ('b', 'h'),
            ('c', 'd'), ('c', 'e'), ('c', 'f'), ('c', 'g'), ('c', 'h'),
            ('d', 'e'), ('d', 'f'), ('d', 'g'), ('d', 'h'),
            ('e', 'f'), ('e', 'g'), ('e', 'h'),
            ('f', 'g'), ('f', 'h'),
            ('g', 'h')
        ], directed=False)
        actual = vertex_cover(g)
        expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.assertEqual(set(actual), set(expected),
            'should compute vertex cover')
