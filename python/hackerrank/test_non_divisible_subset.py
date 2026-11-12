import unittest

from non_divisible_subset import non_divisible_subset

class TestNonDivisibleSubset(unittest.TestCase):
    def test_non_divisible_subset(self):
        tests = [
            ([1, 7, 2, 4], 3, 3),
            ([19, 10, 12, 10, 24, 25, 22], 4, 3),
            ([278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436], 7, 11),
        ]
        for (s, k, expected) in tests:
            actual = non_divisible_subset(s, k)
            self.assertEqual(actual, expected, 'failed s={}, k={} with actual={}'.format(s, k, actual))