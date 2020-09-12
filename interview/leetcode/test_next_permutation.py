# -*- coding: utf-8 -*-

import unittest

from next_permutation import next_permutation

class TestNextPermutation(unittest.TestCase):
    def test_next_permutation(self):
        tests = [
            ([1,2,3], [1,3,2]),
            ([3,2,1], [1,2,3]),
            ([1,1,5], [1,5,1]),
        ]
        for test in tests:
            actual = next_permutation(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))
