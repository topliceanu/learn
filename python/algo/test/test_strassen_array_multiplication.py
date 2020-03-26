# -*- coding: utf-8 -*-

import unittest

from src.strassen_array_multiplication import strassen_array_multiplication


class TestStrassenArrayMultiplication(unittest.TestCase):

    def test_multiplication_for_square_arrays(self):
        x = [
            [1,2,3,4],
            [2,3,4,5],
            [3,4,5,6],
            [7,8,9,10]
        ]
        y = [
            [8,9,10,11],
            [9,10,11,12],
            [10,11,12,13],
            [11,12,13,14]
        ]
        z = [
            [100, 110, 120, 130],
            [138, 152, 166, 180],
            [176, 194, 212, 230],
            [328, 362, 396, 430]
        ]
        actual = strassen_array_multiplication(x, y)
        self.assertEqual(z, actual, 'should correctly multiply the arrays')

    def test_multiplications_for_vectors(self):
        x = [
            [1,2],
            [3,4]
        ]
        y = [
            [5,6],
            [7,8]
        ]
        z = [
            [19, 22],
            [43, 50]
        ]
        actual = strassen_array_multiplication(x, y)
        self.assertEqual(z, actual, 'should multiply arrays')
