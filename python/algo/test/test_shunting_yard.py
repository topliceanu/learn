# -*- coding:utf-8 -*-

import unittest

from src.shunting_yard import shunting_yard, parse

class TestShuntingYard(unittest.TestCase):

    def test_shunting_yard(self):
        tests = [
            (['3', '+', '4'],
             ['+', '4', '3']),
            (['3', '+', '4', '*', '(', '2', '-', '1', ')'],
             ['+', '*', '-', '1', '2', '4', '3']),
            (['3', '+', '4', '*', '2', '/', '(', '1', '-', '5', ')', '^', '2', '^', '3'],
             ['+', '/', '^', '^', '3', '2', '-', '5', '1', '*', '2', '4', '3']),
        ]
        for test in tests:
            actual = shunting_yard(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))

    def test_parse(self):
        root = parse(['3', '+', '4'])
        self.assertEqual(root.token, '+')
        self.assertEqual(root.left.token, '4')
        self.assertEqual(root.right.token, '3')
