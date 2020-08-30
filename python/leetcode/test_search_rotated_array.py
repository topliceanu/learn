# -*- coding: utf-8 -*-

import unittest

from search_rotated_array import search_rotated_array

class TestSearchRotatedArray(unittest.TestCase):
    def test_atoi(self):
        tests = [
            ([], 4, -1),
            ([1], 0, -1),
            ([1,3], 3, 1),
            ([1,2,3], 2, 1),
            ([4,5,6,7,0,1,2], 0, 4),
            ([4,5,6,7,0,1,2], 3, -1),
            ([1,1,1,1,1,1], 1, 2),
            ([1,1,1,1,1,1], 2, -1),
            ([4,5,6,7,8,1,2,3], 8, 4),

        ]
        for test in tests:
            actual = search_rotated_array(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))


