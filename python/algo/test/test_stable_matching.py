# -*- coding: utf-8 -*-

import unittest

from src.stable_matching import stable_matching


class StableMatchingTest(unittest.TestCase):

    def test_stable_matching(self):
        u = {
            'A': ['D', 'E', 'F'],
            'B': ['D', 'E', 'F'],
            'C': ['D', 'E', 'F']
        }
        v = {
            'D': ['A', 'B', 'C'],
            'E': ['B', 'C', 'A'],
            'F': ['C', 'A', 'B']
        }

        expected = [{'A', 'D'}, {'B', 'E'}, {'C', 'F'}]
        actual= stable_matching(u, v)
        self.assertItemsEqual(expected, actual,
            'should compute the perfect matching')
