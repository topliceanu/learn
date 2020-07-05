# -*- coding: utf-8 -*-

import unittest

from longest_substr_no_repeating_chars import length_of_longest_substr

class TestLongestSubstrNoRepeatingChars(unittest.TestCase):

    def test_solution(self):
        tests = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            ("aaaaab", 2),
            ("abbbbb", 2),
        ]
        for test in tests:
            actual = length_of_longest_substr(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))
