# -*- coding: utf-8 -*-

import unittest

from median_sorted_arrays import median_sorted_arrays

class TestMedianSortedArrays(unittest.TestCase):
    def test_median_sorted_arrays(self):
        tests = [
                ([1,3], [2], 2),
                ([1,2], [3,4], 2.5),
        ]
        for test in tests:
            actual = median_sorted_arrays(test[0], test[1])
            expected = test[3]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))
