# -*- coding: utf-8 -*-

import unittest

from roman_to_integer import roman_to_integer

class TestRomanToInteger(unittest.TestCase):
    def test_roman_to_integer(self):
        tests = [
            ('', 0),
            ('I', 1),
            ('III', 3),
            ('IV', 4),
            ('VIII', 8),
            ('IX', 9),
            ('XIV', 14),
            ('XC', 90),
            ('MCMXCIX', 1999),
            # Invalid sequences
            ('IM', None),
            ('XM', None),
        ]
        for test in tests:
            actual = roman_to_integer(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))
