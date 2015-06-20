# -*- coding: utf-8 -*-

import unittest

from src.trie import Trie, END


class TrieTest(unittest.TestCase):

    def test_insert(self):
        t = Trie()
        t.insert('alexandru')
        t.insert('alexandra')

        expected = {'a': {'l': {'e': {'x': {'a': {'n': {'d': {'r': {'u': {END: None}, 'a': {END: None}}}}}}}}}}
        self.assertEqual(t.root, expected, 'should build the correct tree')

    def test_insert_with_two_different_words_with_same_prefix(self):
        t = Trie()
        t.insert('alexandru')
        t.insert('alexandra')
        t.insert('alexandrul')

        expected = {'a': {'l': {'e': {'x': {'a': {'n': {'d': {'r': {'a': {END: None}, 'u': {END: None, 'l': {END: None}}}}}}}}}}}
        self.assertEqual(t.root, expected, 'should build the correct tree')

    def test_insert_with_a_key_value_pair(self):
        t = Trie()
        t.insert('alexandru', True)
        t.insert('alexandra', False)

        expected = {'a': {'l': {'e': {'x': {'a': {'n': {'d': {'r': {'u': {END: True}, 'a': {END: False}}}}}}}}}}
        self.assertEqual(t.root, expected, 'should build the correct tree')

    def test_lookup(self):
        t = Trie()
        for (k, v) in [('bar', 1), ('baz', 2), ('buf', 3), ('buz', 4)]:
            t.insert(k, v)

        self.assertEqual(t.lookup('bar'), 1, 'should find the correct key')
        self.assertIsNone(t.lookup('bus'), 'detect when a key is not present')
        self.assertIsNone(t.lookup('foo'), 'detect when a key is not present')
        self.assertIsNone(t.lookup('bazar'), 'key prefix is present but not key')
        self.assertIsNone(t.lookup('ba'), 'prefix of existing key does not have a value')

    def test_contains(self):
        t = Trie()
        t.insert('home')
        t.insert('homework')

        self.assertFalse(t.contains('ho'), 'prefix does not count as a key')
        self.assertTrue(t.contains('home'), 'should have found the key')
        self.assertTrue(t.contains('homework'), 'should have found the key')
        self.assertFalse(t.contains('homeworker'), 'should have found the key')

    def test_traverse(self):
        keys = ['foo', 'bar', 'baz', 'barz']
        t = Trie()
        map(lambda k: t.insert(k), keys)

        actual = t.traverse()
        expected = [('barz', None), ('bar', None), ('baz', None), ('foo', None)]
        self.assertEqual(expected, actual,
            'should return the keys in a sorted lexicographical order')

    def test_with_prefix(self):
        t = Trie()
        for (k, v) in [('foo', 1), ('bar', 2), ('baz', 3), ('bat', 4)]:
            t.insert(k, v)

        actual = t.with_prefix('ba')
        expected = [('bar', 2), ('baz', 3), ('bat', 4)]
        self.assertItemsEqual(actual, expected,
            'should export the correct values')
