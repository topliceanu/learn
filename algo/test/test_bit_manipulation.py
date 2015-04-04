# -*- coding: utf-8 -*-

import unittest

from src.bit_manipulation import add, is_power_of_two, in_place_swap, is_even, \
    min_value, max_value, is_bit_set, subsets


class BitManipulation(unittest.TestCase):

    def test_add_positive_numbers(self):
        a = 10
        b = 22
        actual = add(a, b)
        expected = a+b
        self.assertEqual(actual, expected, 'should compute correct sum')

    def test_add_positive_numbers(self):
        a = 123
        b = 456
        actual = add(a, b)
        expected = a+b
        self.assertEqual(actual, expected, 'should compute correct sum')

    def test_add_negative_numbers(self):
        a = 123
        b = -456
        actual = add(a, b)
        expected = a+b
        self.assertEqual(actual, expected, 'should compute correct sum')

    def test_is_power_of_two(self):
        a = 256
        self.assertTrue(is_power_of_two(a), 'it is a power of two')

        a = 124
        self.assertFalse(is_power_of_two(a), 'not a power of two')

    def test_is_odd(self):
        a = 123
        self.assertFalse(is_even(a), 'not even')

    def test_is_even(self):
        a = 120
        self.assertTrue(is_even(a), 'even')

    def test_min(self):
        a = 159801
        b = 212354
        actual = min_value(a, b)
        self.assertEqual(actual, a, 'should find min')

    def test_max(self):
        a = 159801
        b = 212354
        actual = max_value(a, b)
        self.assertEqual(actual, b, 'should find max')

    def test_is_bit_set(self):
        a = 122
        self.assertTrue(is_bit_set(a, 3), 'third bit is 1')

    def test_subsets(self):
        a = range(5)
        # TODO make this work!
        actual = subsets(a)
