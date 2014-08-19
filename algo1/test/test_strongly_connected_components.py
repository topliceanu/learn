import unittest

from src.graph import Graph
from src.strongly_connected_components import scc


class TestStronglyConnectedComponents(unittest.TestCase):

    def test_scc(self):
        """ Given the following graph it computes SCCs in it.

             />(2)---------->(8)----------v
            /   |               \     /->(10)
          (1)   |                v  /      |
            ^\  v          /---->(9)<-\    v
              \(3)----->(4)            \-(11)
                 \      ^| \            /^
                  \    / |  v         /
                   >(5)  |   (7)----/
                      ^\ |   /
                        \v  v
                         (6)
        """
        g = Graph.build(edges=[(1,2), (3,2), (2,3), (3,4), (3,5), (5,4),
                               (4,6), (4,7), (7,6), (6,5), (4,9), (7, 11),
                               (11,9), (9,10), (10,11), (2,8), (8,9), (8,10)],
                        directed=True)
        connected_components = scc(g)
        expected = [[8], [1], [2, 3], [9, 10, 11], [4, 5, 6, 7]]

        self.assertEqual(len(connected_components), len(expected),
                'should return the same number of components')
        for component in connected_components:
            self.assertIn(component, expected,
                'should detect strongly connected components')

    def test_scc_on_simpler_graph(self):
        """ Given the following graph it computes SCCs in it.

        (1)--->(7)--->(9)--->(6)--->(8)<---(5)
         ^\     |      ^\    /       |    /^
           \    v        \  v        v  /
            \--(4)        (3)       (2)
        """
        g = Graph.build(edges=[(1,7), (4,1), (7,4), (7,9), (9,6), (6,3),
                               (3,9), (6,8), (8,2), (2,5), (5,8)],
                        directed=True)
        connected_components = scc(g)
        expected = [[2, 5, 8], [3, 6, 9], [1, 4, 7]]

        self.assertEqual(len(connected_components), len(expected),
                'should return the same number of components')
        for component in connected_components:
            self.assertIn(component, expected,
                'should detect strongly connected components')
