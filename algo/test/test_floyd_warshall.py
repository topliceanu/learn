# -*- coding: utf-8 -*-

import unittest

from src.floyd_warshall import all_pairs_shortest_path
from src.graph import Graph


class FloydWarshalTest(unittest.TestCase):

    def test_all_pairs_shortest_path(self):
        """ Given the following graph from the lecture:
                  -2
            (a)-------->(b)
            ^|           |
             |           |
             4\       -1/
               \       /
                \(c)</
                 /  \
               2/    \-3
              v/      \v
             (x)       (y)
              \^       /^
               \      /
               1\    /-4
                 \  /
                 (z)
        """
        g = Graph.build(edges=[('a', 'b', -1), ('c', 'a', 4), ('b', 'c', -1),
                ('c', 'x', 2), ('c', 'y', -3), ('z', 'x', 1), ('z', 'y', -4)],
                directed=True)

        actual = all_pairs_shortest_path(g)
        print '>>>>', actual
        INF = float('inf')
        expected = {
            'a': {'a': 0, 'c': -2, 'b': -1, 'y': -5, 'x': 0, 'z': INF},
            'c': {'a': 4, 'c': 0, 'b': 3, 'y': -3, 'x': 2, 'z': INF},
            'b': {'a': 3, 'c': -1, 'b': 0, 'y': -4, 'x': 1, 'z': INF},
            'y': {'a': INF, 'c': INF, 'b': INF, 'y': 0, 'x': INF, 'z': INF},
            'x': {'a': INF, 'c': INF, 'b': INF, 'y': INF, 'x': 0, 'z': INF},
            'z': {'a': INF, 'c': INF, 'b': INF, 'y': -4, 'x': 1, 'z': 0}
        }
        self.assertEqual(actual, expected,
            'should return correct all pairs shortest path distances')
