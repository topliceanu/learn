# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/4sum/

import unittest

from generate_parantheses import generate_parantheses

class TestGenerateParanthese(unittest.TestCase):
    def test_generate_paranthese(self):
        tests = [
            (1, ['()']),
            (3, [
                    "((()))",
                    "(()())",
                    "(())()",
                    "()(())",
                    "()()()"
                ]),
            (4, [
                    "(((())))",
                    "((()()))",
                    "((())())",
                    "((()))()",
                    "(()(()))",
                    "(()()())",
                    "(()())()",
                    "(())(())",
                    "(())()()",
                    "()((()))",
                    "()(()())",
                    "()(())()",
                    "()()(())",
                    "()()()()"
                ]),

        ]
        for test in tests:
            actual = generate_parantheses(test[0])
            expected = test[1]
            for e in expected:
                self.assertIn(e, actual, 'expected {} should be in {}'.format(e, actual))
            for a in actual:
                self.assertIn(a, expected, 'actual {} should be in {}'.format(a, expected))
