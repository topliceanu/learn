import unittest

from src.graph import Graph
from src.minimum_spanning_tree import prims_suboptimal_mst


class TestMinimunSpanningTree(unittest.TestCase):

    def test_mst(self):
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
        expected = [('a', 'b', 1), ('a', 'c', 4), ('b', 'd', 2)]
        mst = prims_suboptimal_mst(g)
        actual = sorted(mst.get_edges())
        self.assertEqual(actual, expected, 'should have computed correct mst')
