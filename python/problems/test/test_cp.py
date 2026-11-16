import unittest

from src.cp.dp_knapsack import knapsack_0_1

class TestCP(unittest.TestCase):
    # FIXME
    def _test_knapsack_0_1(self):
        tests = [
            (7, [1,3,4,5], [1,4,5,7], [0,1,1,0]),
            (6, [2,4,4,4], [3,4,2,1], [1,1,0,0]),
        ]
        for (capacity, weights, values, expected) in tests:
            actual = knapsack_0_1(capacity, weights, values)
            self.assertEqual(expected, actual)