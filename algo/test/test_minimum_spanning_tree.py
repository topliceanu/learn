import unittest

from minimum_spanning_tree import mst
from graph import Graph


class TestMinimunSpanningTree(unittest.TestCase):

    def mst(self):
        """ Compute minimal spanning tree given this graph:
            (a)----1----(b)
             | \         |
             4  \--3--\  2
             |         \ |
            (c)----5----(d)
        """
        g = Graph.build(edges=[('a', 'b', 1), ('a', 'c', 4), ('a', 'd', 3),
                               ('b', 'd', 2), ('c', 'd', 5)],
                        directed=False)
        actual = mst(g)
        expected = []
