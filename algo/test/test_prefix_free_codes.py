# -*- coding: utf-8 -*-

import unittest

from src.prefix_free_codes import HuffmanCode, LEFT, RIGHT, SYMBOL, PARENT


class PrefixFreeTest(unittest.TestCase):

    def test_build_tree(self):
        symbol_table = {
            'A': 15,
            'B': 7,
            'C': 6,
            'D': 6,
            'E': 5
        }
        hc = HuffmanCode(symbol_table)
        self.assertIsNone(hc.tree[SYMBOL], 'root has no symbol')
        self.assertEqual(hc.tree[LEFT][SYMBOL], 'A')
        self.assertEqual(hc.tree[LEFT][PARENT], hc.tree,
            'should have the correct parent wired')
        self.assertIsNone(hc.tree[RIGHT][SYMBOL], 'node has no symbol')
        self.assertEqual(hc.tree[RIGHT][PARENT], hc.tree,
            'should have the correct parent wired')
        self.assertIsNone(hc.tree[RIGHT][LEFT][SYMBOL], 'node has no symbol')
        self.assertEqual(hc.tree[RIGHT][LEFT][PARENT], hc.tree[RIGHT],
            'should have the correct parent wired')
        self.assertEqual(hc.tree[RIGHT][LEFT][LEFT][SYMBOL], 'E')
        self.assertEqual(hc.tree[RIGHT][LEFT][LEFT][PARENT], hc.tree[RIGHT][LEFT],
            'should have the correct parent wired')
        self.assertEqual(hc.tree[RIGHT][LEFT][RIGHT][SYMBOL], 'C')
        self.assertEqual(hc.tree[RIGHT][LEFT][RIGHT][PARENT], hc.tree[RIGHT][LEFT],
            'should have the correct parent wired')
        self.assertIsNone(hc.tree[RIGHT][RIGHT][SYMBOL], 'node has no symbol')
        self.assertEqual(hc.tree[RIGHT][RIGHT][PARENT], hc.tree[RIGHT],
            'should have the correct parent wired')
        self.assertEqual(hc.tree[RIGHT][RIGHT][LEFT][SYMBOL], 'D')
        self.assertEqual(hc.tree[RIGHT][RIGHT][LEFT][PARENT], hc.tree[RIGHT][RIGHT],
            'should have the correct parent wired')
        self.assertEqual(hc.tree[RIGHT][RIGHT][RIGHT][SYMBOL], 'B')
        self.assertEqual(hc.tree[RIGHT][RIGHT][LEFT][PARENT], hc.tree[RIGHT][RIGHT],
            'should have the correct parent wired')

    def test_huffman_encode(self):
        symbol_table = {
            'A': 0.6,
            'B': 0.25,
            'C': 0.10,
            'D': 0.05
        }
        hc = HuffmanCode(symbol_table)
        original = 'ABCD'
        expected = '010110111'
        actual = hc.encode(original)
        self.assertEqual(expected, actual, 'should correctly encode the data')

    def test_huffman_decode(self):
        symbol_table = {
            'A': 0.6,
            'B': 0.25,
            'C': 0.10,
            'D': 0.05
        }
        hc = HuffmanCode(symbol_table)
        encoded = '0110111'
        expected = 'ACD'
        actual = hc.decode(encoded)
        self.assertEqual(expected, actual, 'should correctly decode the data')

    def test_static_encode_decode_large_text(self):
        text = 'Flux is an application architecture for building complex user '\
            'interfaces. It eschews MVC in favor of unidirectional data flow. '\
            'What this means is that data enters through a single place (your '\
            'actions) and then flows outward through to their state manager '\
            '(the store) and finally onto the view. The view can then restart '\
            'the flow by calling other actions in response to user input.'\

        encoded = HuffmanCode.encode_text(text)
        symbol_table = HuffmanCode.extract_frequencies(text)
        decoded = HuffmanCode.decode_text(symbol_table, encoded)
        self.assertEqual(text, decoded,
            'should encode and decode to the same text')
