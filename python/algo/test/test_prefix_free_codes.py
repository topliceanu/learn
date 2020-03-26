# -*- coding: utf-8 -*-

import unittest

from src.prefix_free_codes import Huffman


class PrefixFreeTest(unittest.TestCase):

    def test_build_tree(self):
        symbol_table = {
            'A': 15,
            'B': 7,
            'C': 6,
            'D': 6,
            'E': 5
        }
        hc = Huffman(symbol_table)
        self.assertEqual(hc.root.left.symbol, 'A')
        self.assertEqual(hc.root.left.parent, hc.root,
            'should have the correct parent wired')
        self.assertEqual(hc.root.right.parent, hc.root,
            'should have the correct parent wired')
        self.assertEqual(hc.root.right.left.parent, hc.root.right,
            'should have the correct parent wired')
        self.assertEqual(hc.root.right.left.left.symbol, 'E')
        self.assertEqual(hc.root.right.left.left.parent, hc.root.right.left,
            'should have the correct parent wired')
        self.assertEqual(hc.root.right.left.right.symbol, 'C')
        self.assertEqual(hc.root.right.left.right.parent, hc.root.right.left,
            'should have the correct parent wired')
        self.assertEqual(hc.root.right.right.parent, hc.root.right,
            'should have the correct parent wired')
        self.assertEqual(hc.root.right.right.left.symbol, 'D')
        self.assertEqual(hc.root.right.right.left.parent, hc.root.right.right,
            'should have the correct parent wired')
        self.assertEqual(hc.root.right.right.right.symbol, 'B')
        self.assertEqual(hc.root.right.right.left.parent, hc.root.right.right,
            'should have the correct parent wired')

    def test_huffman_encode(self):
        symbol_table = {
            'A': 0.6,
            'B': 0.25,
            'C': 0.10,
            'D': 0.05
        }
        hc = Huffman(symbol_table)
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
        hc = Huffman(symbol_table)
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

        encoded = Huffman.encode_text(text)
        symbol_table = Huffman.extract_frequencies(text)
        decoded = Huffman.decode_text(symbol_table, encoded)
        self.assertEqual(text, decoded,
            'should encode and decode to the same text')
