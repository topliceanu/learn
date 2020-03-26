# -*- coding: utf-8 -*-

import unittest

from src.bipartite_matching import bipartite_matching
from src.graph import Graph


class TestBipartiteMatching(unittest.TestCase):

    def test_bipartite_matching(self):
        """ Given the graph below:
            (a)-(b)
              \_/
              / \
            (d)-(c)
                /
             (e)
                  (h)
                 /
              (f)--(g)
        """
        g = Graph.build(edges=[('a', 'b'), ('a', 'c'), ('d', 'c')
                        ('d', 'b'), ('e', 'c'), ('f', 'h'), ('f', 'g')],
                    directed=False)
        pairs = bipartite_matching(g)
        self.assertEqual(len(pairs), 3, 'should produce three pairs')
