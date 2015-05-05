# -*- coding: utf-8 -*-

import unittest

from src.traveling_salesman import traveling_salesman
from src.graph import Graph


class TravelingSalesmanTest(unittest.TestCase):

    def x_test_traveling_salesman(self):
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
        (actual_min_cost, actual_min_path) = traveling_salesman(g)
        expected_min_path = ('a', 'd', 'b', 'c', 'a')
        expected_min_cost = 13
        self.assertEqual(actual_min_cost, expected_min_cost,
                'should compute the correct min cost')
        #self.assertEqual(actual_min_path, expected_min_path,
        #        'should compute the correct min path')

    def x_test_traveling_salesman_with_coordinates_instead_of_edges(self):
        points = [('a', 0, 0), ('b', 0, 2), ('c', 0, 4), ('d', 0, 6)]
        g = Graph.build_from_coords(points, directed=False)
        (actual_min_cost, _) = traveling_salesman(g)
        expected_min_cost = 12
        self.assertEqual(actual_min_cost, expected_min_cost,
                'should produce the min circuit')

        points = [('a', 0, 0), ('b', 0, 1), ('c', 0, 2), ('d', 0, 3),
                  ('e', 0, 4), ('f', 1, 4), ('g', 1, 3), ('h', 1, 2),
                  ('i', 1, 1), ('j', 1, 0)]
        g = Graph.build_from_coords(points, directed=False)
        (actual_min_cost, _) = traveling_salesman(g)
        expected_min_cost = 10
        self.assertEqual(actual_min_cost, expected_min_cost,
                'should produce the min circuit')

    def test_traveling_salesman_with_large_data_set(self):
        """ Try the correctness of the algorithm for 18 points. """
        points = [
            ('a', 0.328521, 0.354889),
            ('b', 0.832, 0.832126),
            ('c', 0.680803, 0.865528),
            ('d', 0.734854, 0.38191),
            ('e', 0.14439, 0.985427),
            ('f', 0.90997, 0.587277),
            ('g', 0.408464, 0.136019),
            ('h', 0.896868, 0.916344),
            ('i', 0.991904, 0.383134),
            ('j', 0.451197, 0.741267),
            ('k', 0.825205, 0.761446),
            ('l', 0.421804, 0.0374936),
            ('m', 0.332503, 0.26436),
            ('n', 0.107117, 0.51559),
            ('o', 0.845227, 0.21359),
            ('p', 0.880095, 0.593086),
            ('q', 0.454773, 0.834355),
            ('r', 0.7464, 0.363176)
        ]
        g = Graph.build_from_coords(points, directed=False)
        (actual_min_cost, _) = traveling_salesman(g)
        actual_min_cost = '{0:.5f}'.format(actual_min_cost)
        expected_min_cost = '{0:.5f}'.format(3.50115607151)
        self.assertEqual(actual_min_cost, expected_min_cost,
                'should product the expected min cost')
