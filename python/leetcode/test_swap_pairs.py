# -*- coding: utf-8 -*-

import unittest

from swap_pairs import swap_pairs
from helpers import make_linked_list, from_linked_list

class TestSwapPairs(unittest.TestCase):
    def test_swap_pairs(self):
        tests = [
            ([], []),
            ([1], [1]),
            ([1,2], [2,1]),
            ([1,2,3], [2,1,3]),
            ([1,2,3,4], [2,1,4,3]),
        ]
        for test in tests:
            ls = make_linked_list(test[0])
            result = swap_pairs(ls)
            actual = from_linked_list(result)
            expected = test[1]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))


