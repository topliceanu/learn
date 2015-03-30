# -*- coding: utf-8 -*-

import unittest

from src.trie import Trie


class TrieTest(unittest.TestCase):

    def test_insert(self):
        t = Trie()
        t.insert('alexandru')
        t.insert('alexandra')

        expected = {'a': {'l': {'e': {'x': {'a': {'n': {'d': {'r': {'u': {'END': 'END'}, 'a': {'END': 'END'}}}}}}}}}}
        self.assertEqual(t.root, expected, 'should build the correct tree')

    def test_contains(self):
        t = Trie()
        t.insert('home')
        t.insert('homework')

        self.assertFalse(t.contains('ho'), 'prefix does not count as a key')
        self.assertTrue(t.contains('home'), 'should have found key')
        self.assertTrue(t.contains('homework'), 'should have found key')
        self.assertFalse(t.contains('homeworker'), 'should have found key')

    def test_list_sorted(self):
        keys = ['foo', 'bar', 'baz', 'barz']
        t = Trie()
        map(lambda k: t.insert(k), keys)

        actual = t.list_sorted()
        expected = ['barz', 'bar', 'baz', 'foo']
        self.assertEqual(expected, actual,
            'should return the keys in a sorted lexicographical order')

    def test_with_prefix(self):
        keys = ['foo', 'bar', 'baz', 'barz']
        t = Trie()
        map(lambda k: t.insert(k), keys)

        actual = t.with_prefix('ba')
        expected = ['barz', 'bar', 'baz']
        self.assertEqual(expected, actual,
            'should return all keys with prefix ba')
