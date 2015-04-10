# -*- coding: utf-8 -*-

import unittest

from src.traveling_salesman import traveling_salesman
from src.graph import Graph


class TravelingSalesmanTest(unittest.TestCase):

    def test_traveling_salesman(self):
        """ Given the following graph:
                     2
                (a)----(b)
                 | \4 / |
                 |  \/  |5
                1|  /\  |
                 | /3 \ |
                 |/    \|
                (c)----(d)
                    6
        """
        g = Graph.build(edges=[
                ('a', 'b', 2), ('a', 'd', 4), ('a', 'c', 1),
                ('b', 'd', 5), ('b', 'c', 3), ('d', 'c', 6)
            ], directed=False)
        actual = traveling_salesman(g)
        expected = ('a', 'd', 'b', 'c', 'a')
        self.assertEqual(actual, expected,
            'should return the correct succession of vertices')
