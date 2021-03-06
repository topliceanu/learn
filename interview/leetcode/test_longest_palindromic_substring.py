# -*- coding: utf-8 -*-

import unittest

from longest_palindromic_substring import longest_palindrome2

class TestLongestPalindromicSubstring (unittest.TestCase):
    def test_longest_palindrome(self):
        tests = [
            ("", [""]), # empty
            ("a", ["a"]), # single string
            ("aa", ["aa"]), # full match
            ("aaaaa", ["aaaaa"]), # longerfull match
            ("abc", ["a", "b", "c"]), # first match
            ("cbbd", ["bb"]), # middle, length 2
            ("cbab", ["bab"]), # end, length 2
            ("babad", ["bab", "aba"]), # middle, length 3
            ("abac", ["aba"]), # beginning, length 3
            ("zabacdad", ["aba", "dad"]), # 2 palindromes, same length
            ("abacdeed", ["deed"]), # 2 palindromes, different length
            ("abaaaa", ["aaaa"]), # off ballance
            ("aaabaaaa", ["aaabaaa"]),
            ("abacabacabb", ["bacabacab"]),
            ("abaabac", ["abaaba"]),
        ]
        for test in tests:
            actual = longest_palindrome2(test[0])
            expected = test[1]
            self.assertIn(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))
