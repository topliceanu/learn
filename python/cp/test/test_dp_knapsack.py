import unittest

from src.dp_knapsack import knapsack_0_1 

class TestKnapsack(unittest.TestCase):

    def test_knapsack_0_1(self):
        for (capacity, weights, values, expected) in [
            (7, [1,3,4,5], [1,4,5,7], [0,1,1,0]),
            (6, [2,4,4,4], [3,4,2,1], [1,1,0,0])
        ]:
            actual = knapsack_0_1(capacity, weights, values)
            self.assertEqual(expected, actual)