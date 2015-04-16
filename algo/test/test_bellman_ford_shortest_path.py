# -*- coding: utf-8 -*-

import unittest

from src.bellman_ford_shortest_path import shortest_path
from src.graph import Graph


class BellmanFordTest(unittest.TestCase):

    def test_bellman_ford_for_positive_edge_lengths(self):
        """ Given the following graph:
           /--2-->(v)---2--->(w)--2--\v
        (s)        1\v               (t)
          \----4--->(x)------4------/^
        """
        g = Graph.build(edges=[
                ('s', 'v', 2), ('s', 'x', 4), ('v', 'w', 2),
                ('w', 't', 2), ('v', 'x', 1), ('x', 't', 4)
            ],
            directed=True)
        (costs, paths) = shortest_path(g, 's')
        expected_costs = {'x': 3, 's': 0, 't': 6, 'w': 4, 'v': 2}
        expected_paths = {'x': ['v'], 's': [], 't': ['v', 'w'], 'w': ['v'], 'v': []}
        self.assertEqual(costs, expected_costs,
            'should return the correct minimum paths costs')
        self.assertEqual(paths, expected_paths,
            'should return the correct minimum paths vertices')

    def test_bellman_ford_with_non_negative_cycle(self):
        """ Given the following graph:
           /--2-->(v)---2--->(w)--2--\v
        (s)        \^      /        (t)
          \         \1  v/-5        /^
           \---4---->(x)------4---/
        """
        g = Graph.build(edges=[
                ('s', 'v', 2), ('v', 'w', 2), ('w', 't', 2),
                ('s', 'x', 4), ('x', 'v', 1), ('w', 'x', -5),
                ('x', 't', 4)
            ],
            directed=True)
        no_negative_cycles = shortest_path(g, 's')
        self.assertFalse(no_negative_cycles, 'should detect no negative cycles')
