# -*- coding: utf-8 -*-

import unittest

from letter_combinations import letter_combinations

class TestLetterCombinations(unittest.TestCase):
    def test_letter_combinations(self):
        tests = [
            ('', []),
            ('9', ["w", "x", "y", "z"]),
            ('91', ["w", "x", "y", "z"]),
            ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ('213', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ('123', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ('231', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ('111111', []),
        ]
        for test in tests:
            actual = letter_combinations(test[0])
            expected = test[1]
            self.assertEqual(len(actual), len(expected), \
                    'expected {} should have the same length as actual {}'\
                    .format(test, actual))
            for exp in expected:
                self.assertIn(exp, actual, \
                    'expected {} to be in actual {}'.format(exp, actual))

