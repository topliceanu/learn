# -*- coding: utf-8 -*-

import unittest

from three_sum_closest import three_sum_closest

class Test3SumClosest(unittest.TestCase):
    def test_three_sum_closest(self):
        tests = [
            ([-1,0,1,0], 0, 0),
            ([-1,-1,1,0], -1, -1),
            ([1, 2, 3, 4], 5, 6),
            ([1, 1, 1, 0], 100, 3),
            ([1,2,4,8,16,32,64,128], 82, 82),
            ([4,0,5,-5,3,3,0,-4,-5], -2, -2),
        ]
        for test in tests:
            actual = three_sum_closest(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected, \
                'failed test={}, actual={}'.format(test, actual))
