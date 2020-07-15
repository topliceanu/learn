# -*- coding: utf-8 -*-

import unittest

from max_area import max_area

class TestMaxArea(unittest.TestCase):

    def test_max_area(self):
        tests = [
            ([1,8,6,2,5,4,8,3,7], 49),
        ]
        for test in tests:
            actual = max_area(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))
