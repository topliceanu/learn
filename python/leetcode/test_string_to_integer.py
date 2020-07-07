# -*- coding: utf-8 -*-

import unittest

from string_to_integer import atoi

class TestStringToInteger(unittest.TestCase):
    def test_atoi(self):
        tests = [
            ("", 0),
            ("42", 42),
            ("-42", -42),
            ("+42", 42),
            ("  -42blabla  ", -42),
            ("4193 with words", 4193),
            ("words then 4193", 0),
            ("    -words then 4193", 0),
            ("12312312313123123123", pow(2, 31)-1),
            ("-12312312312312312312", -pow(2, 31)),
        ]
        for test in tests:
            actual = atoi(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))

