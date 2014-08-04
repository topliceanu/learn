import unittest

import src.graph
import src.breadth_first_search


class BreadthFirstSearch(unittest.TestCase):

    def test_bfs(self):
        """
            Correctly explore the following graph:
                  _(a)--(c)--(e)
                /   | /    \  |
             (s)--(b)-------(d)
        """
        vertices = ['s', 'a', 'b', 'c', 'd', 'e']
        edges = [('s', 'a'), ('s', 'b'), ('a', 'b'), ('a', 'c'), ('b', 'd'),
                 ('c', 'e'), ('c', 'd'), ('e', 'd')]
        graph = graph.Graph(vertices, edges)
        expected = ['s', 'a', 'b', 'c', 'd', 'e']
        actual = breadth_first_search.bfs(graph, 's')
        assertEqual(actual, expected, 'should have visited '+
                                      'the graph in correct order')
