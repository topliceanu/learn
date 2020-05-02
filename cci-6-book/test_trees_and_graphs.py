# -*- coding: utf-8 -*-

import unittest

from trees_and_graphs import build_order

class TestTreesAndGraphs(unittest.TestCase):
    pass


class TestRecapGraphAlgorithsm(unittest.TestCase):
    def test_build_order(self):
        tests = [
            {
                "projects": ['a', 'b', 'c', 'd', 'e', 'f'],
                "dependencies": [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')],
                "output": ['f', 'e', 'b', 'a', 'd', 'c'],
            }
        ]
        for test in tests:
            actual = build_order(test["projects"], test["dependencies"])
            expected = test["output"]
            self.assertEqual(actual, expected, "failed test={} with actual={}".format(test, actual))
