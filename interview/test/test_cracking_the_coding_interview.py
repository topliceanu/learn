# -*- coding: utf-8 -*-

import unittest

from cracking_the_coding_interview import *


class BitManipulation(unittest.TestCase):

    def test_problem_5_1(self):
        n = int('10000000000', 2)
        m = int('10101', 2)
        i = 2
        j = 6
        actual = problem_5_1(n, m, i, j)
        expected = int('10001010100', 2)
        self.assertEqual(actual, expected, 'should produce the correct value')

        n = int('11111111111', 2)
        m = int('10101', 2)
        i = 2
        j = 6
        actual = problem_5_1(n, m, i, j)
        expected = int('11111010111', 2)
        self.assertEqual(actual, expected, 'should produce the correct value')

    def x_test_problem_5_2(self):
        n = 3.17
        actual = problem_5_2(n)
        expected = False
        self.assertEqual(actual, expected, 'should return the correct value')
