# -*- coding: utf-8 -*-

import unittest

from src.prefix_free_codes import HuffmanCode


class PrefixFreeTest(unittest.TestCase):

    def test_huffman_decode(self):
        symbol_table = {
            'A': 0.6,
            'B': 0.25,
            'C': 0.10,
            'D': 0.05
        }
        hc = HuffmanCode(symbol_table)
        encoded = '0110111'
        expected = 'ADC'
        actual = hc.decode(encoded)
        self.assertEqual(expected, actual, 'should correctly decode the data')

    def test_huffman_encode(self):
        symbol_table = {
            'A': 0.6,
            'B': 0.25,
            'C': 0.10,
            'D': 0.05
        }
        hc = HuffmanCode(symbol_table)
        original = 'ABCD'
        expected = '010111110'
        actual = hc.encode(original)
        self.assertEqual(expected, actual, 'should correctly encode the data')
