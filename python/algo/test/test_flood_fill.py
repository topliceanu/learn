# -*- coding: utf-8 -*-

import unittest

from src.flood_fill import flood_fill, scanline_fill


class FloodFillTest(unittest.TestCase):

    def test_flood_fill_center(self):
        space = [
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0],
            [1,1,0,0,0,1,1],
            [0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
        ]

        expected = [
            [0,0,0,1,1,1,1],
            [0,0,0,1,1,1,1],
            [0,0,1,1,1,1,1],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,0,0],
            [1,1,1,1,0,0,0],
            [1,1,1,1,0,0,0],
        ]
        flood_fill(space, (3, 3), 0, 1)

        self.assertItemsEqual(space, expected,
            'should have filled every position reachable')

    def test_flood_fill_top_left(self):
        space = [
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0],
            [1,1,0,0,0,1,1],
            [0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
        ]

        expected = [
            [1,1,1,1,0,0,0],
            [1,1,1,1,0,0,0],
            [1,1,1,0,0,0,0],
            [1,1,0,0,0,1,1],
            [0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
        ]
        flood_fill(space, (0, 0), 0, 1)

        self.assertItemsEqual(space, expected,
            'should have filled every position reachable')

    def test_scanline_fill(self):
        space = [
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0],
            [1,1,0,0,0,1,1],
            [0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
        ]

        expected = [
            [1,1,1,1,0,0,0],
            [1,1,1,1,0,0,0],
            [1,1,1,0,0,0,0],
            [1,1,0,0,0,1,1],
            [0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
        ]
        scanline_fill(space, (0, 0), 0, 1)

        self.assertItemsEqual(space, expected,
            'should have filled every position reachable')
