# -*- coding: utf-8 -*-

import unittest

from three_sum import three_sum

class Test3Sum(unittest.TestCase):
    def test_three_sum(self):
        tests = [
            ([], []),
            ([-1,0,1,0], [(-1,0,1)]),
            ([-1,-1,1,0], [(-1,0,1)]),
            ([-1,1,1,0], [(-1,0,1)]),
            ([0, 0, 0], [(0, 0, 0)]),
            ([-1, 0, 1, 2, -1, -4], [(-1, 0, 1), (-1, -1, 2)]),
            ([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], [(-4,-2,6),(-4,0,4),(-4,1,3),(-4,2,2),(-2,-2,4),(-2,0,2)]),
            ([5,4,3,2,1,0,-1,-2,-3,-4,-5], [(-5, 0, 5), (-5, 1, 4), (-5, 2, 3), (-4, -1, 5), (-4, 0, 4), (-4, 1, 3), (-3, -2, 5), (-3, -1, 4), (-3, 0, 3), (-3, 1, 2), (-2, -1, 3), (-2, 0, 2), (-1, 0, 1)]),
        ]
        for test in tests:
            actual = three_sum(test[0], 0)
            expected = test[1]
            self.assertEqual(len(actual), len(expected), \
                'failed test={} with actual={}'.format(test, actual))
            for a in actual:
                self.assertIn(a, expected, \
                    'failed test={} since {} is not expected'.format(test, a, expected))
