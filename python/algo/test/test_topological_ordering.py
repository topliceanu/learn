import unittest

from src.graph import Graph
from src.topological_ordering import dfs_loop, get_sync_vertices, \
                                     less_efficient_topological_ordering


class TestTopologicalSort(unittest.TestCase):

    def test_get_sync_vertices(self):
        """ Given the graph below it should find 1 and 2 as sync vertices:
        (1) <- (3)
               /
        (2) <-/
        """
        g = Graph.build(edges=[(3,1), (3,2)], directed=True)
        actual = get_sync_vertices(g)
        expected = [1, 2]
        self.assertEqual(actual, expected, 'found sync vertices')

    def test_less_efficient_topological_ordering(self):
        """ Given the following graph:
          /-->(b)-->\
        (a)         (d)
          \-->(c)-->/
        """
        g = Graph.build(edges=[('a','b'), ('a', 'c'), ('b', 'd'), ('c', 'd')],
                        directed=True)
        ordering = less_efficient_topological_ordering(g)
        self.assertEqual(ordering['a'], 1)
        self.assertIn(ordering['b'], [2,3])
        self.assertIn(ordering['c'], [2,3])
        self.assertEqual(ordering['d'], 4)

    def test_topological_ordering(self):
        """ Given the following graph:
          /-->(b)-->\
        (a)         (d)
          \-->(c)-->/
        """
        g = Graph.build(edges=[('a','b'), ('a', 'c'), ('b', 'd'), ('c', 'd')],
                        directed=True)
        ordering = dfs_loop(g)
        self.assertEqual(ordering['a'], 1)
        self.assertIn(ordering['b'], [2,3])
        self.assertIn(ordering['c'], [2,3])
        self.assertEqual(ordering['d'], 4)

    def test_topological_ordering_on_a_cyclic_graph(self):
        """ Given the following graph:
                /-->(v)---\
              /      |     \v
            (s)------+----->(w)
             ^\      v      /
               \----(t)<---/
        """
        g = Graph.build(edges=[('s', 'v'), ('v', 'w'),
                               ('w', 't'), ('t', 's'),
                               ('s', 'w'), ('v', 't')],
                        directed=True)
        ordering = dfs_loop(g)
        self.assertEqual(ordering['s'], 1)
        self.assertEqual(ordering['t'], 4)
        self.assertEqual(ordering['w'], 3)
        self.assertEqual(ordering['v'], 2)
