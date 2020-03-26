# -*- coding: utf-8 -*-

import unittest

from src.lossless_compression import run_length_encode, run_length_decode, \
                                     lz77_encode, lz77_decode


class TestLosslessCompression(unittest.TestCase):

    def test_run_length_encode(self):
        data = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
        actual = run_length_encode(data)
        expected = [12, 'W', 1, 'B', 12, 'W', 3, 'B', 24, 'W', 1, 'B', 14, 'W']
        self.assertEqual(actual, expected, 'should correctly compress')

    def test_run_length_decode(self):
        data = [12, 'W', 1, 'B', 12, 'W', 3, 'B', 24, 'W', 1, 'B', 14, 'W']
        actual = run_length_decode(data)
        expected = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
        self.assertEqual(actual, expected, 'should correctly decompress data')

    def test_lz77_encode(self):
        data = ['a','a','c','a','a','c','a','b','c','a','b','a','a','a','c']
        actual = lz77_encode(data)
        expected = [(0, 0, "a"), (1, 1, "c"), (3, 4, "b"),
                    (3, 3, "a"), (12, 3, "$")]
        self.assertListEqual(actual, expected, 'should product the correct output')

    def test_lz77_decode(self):
        data = [(0, 0, "a"), (1, 1, "c"), (3, 4, "b"),
                    (3, 3, "a"), (12, 3, "$")]
        actual = lz77_decode(data)
        expected = ['a','a','c','a','a','c','a','b','c','a','b','a','a','a','c']
        self.assertListEqual(actual, expected, 'should product the correct output')
