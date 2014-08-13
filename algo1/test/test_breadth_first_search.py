import unittest

from src.graph import Graph
from src.breadth_first_search import bfs


class BreadthFirstSearchTest(unittest.TestCase):

    def test_bfs_parses_the_graph_in_order(self):
        """
            Correctly explore the following graph:
                  _(a)--(c)--(e)
                /   | /    \  |
             (s)--(b)-------(d)
        """
        edges = [('s', 'a'), ('s', 'b'), ('a', 'b'), ('a', 'c'), ('b', 'd'),
                 ('c', 'e'), ('c', 'd'), ('e', 'd')]
        graph = Graph.build(edges=edges)
        expected = ['s', 'a', 'b', 'c', 'd', 'e']
        actual = bfs(graph, 's')
        self.assertEqual(actual, expected,
                'should have visited the graph in correct order')
