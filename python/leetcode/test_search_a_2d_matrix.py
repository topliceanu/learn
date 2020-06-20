# -*- coding: utf-8 -*-

import unittest

from search_a_2d_matrix import Solution

global s
s = Solution()

class TestLongestSubstrNoRepeatingChars(unittest.TestCase):
    def test_search(self):
        tests = [
            ([], 10, False),
            ([[1]], 1, True),
            ([[1]], 2, False),
            ([
              [1,   4],
              [2,   5]
            ], 2, True),
            ([
              [1,   1,  1],
              [1,   1,  1],
              [1,   1,  1]
            ], 2, False),
            ([
              [1,   2,  3],
              [2,   3,  4],
              [3,   4,  5]
            ], 0, False),
            ([
              [1,   2,  3],
              [2,   3,  4],
              [3,   4,  5]
            ], 0, False),
            ([
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ], 5, True),
            ([
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ], 18, True),
            ([
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ], 20, False),
            ([
              [ 1, 2, 3, 4, 5],
              [ 6, 7, 8, 9,10],
              [11,12,13,14,15],
              [16,17,18,19,20],
              [21,22,23,24,25]
             ], 5, True),
        ]
        for test in tests:
            actual = s.searchMatrix(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))
