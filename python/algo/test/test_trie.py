# -*- coding: utf-8 -*-

import unittest

from src.trie import Trie, END, TrieNode


class TestTrieNode(unittest.TestCase):

    def test_insert(self):
        """ Build the following trie:
                    ()
                   a|
                   ()
                  b|
                  ()
                c/  \d
               (1)  (2)
        """
        root = TrieNode()
        root.insert('abc', 1)
        root.insert('abd', 2)

        self.assertIsNone(root.value, 'root has no value')
        self.assertItemsEqual(root.children.keys(), ['a'], 'only one child')
        self.assertIsNone(root.children['a'].value, 'first node has no value')
        self.assertItemsEqual(root.children['a'].children.keys(), ['b'], 'only one child')
        self.assertIsNone(root.children['a'].children['b'].value, 'second node has no value')
        self.assertItemsEqual(root.children['a'].children['b'].children.keys(), ['c', 'd'], 'two children')
        self.assertEqual(root.children['a'].children['b'].children['c'].value, 1, 'correct value is stored')
        self.assertEqual(root.children['a'].children['b'].children['d'].value, 2, 'correct value is stored')

    def test_lookup(self):
        root = TrieNode()
        root.insert('abc', 1)
        root.insert('abd', 2)

        self.assertEqual(root.lookup('abc'), 1, 'should return the correct value')
        self.assertIsNone(root.lookup('abe'), 'should not find the corresponding value')

    def test_lookup_prefix(self):
        root = TrieNode()
        root.insert('abc', 1)
        root.insert('abd', 2)
        root.insert('acd', 3)
        root.insert('bcd', 4)
        root.insert('bc', 5)

        actual = root.lookup_prefix('ab')
        expected = [('abc', 1), ('abd', 2)]
        self.assertItemsEqual(actual, expected,
            'should return all key, value pairs with keys beginning with prefix')

        actual = root.lookup_prefix('a')
        expected = [('abc', 1), ('abd', 2), ('acd', 3)]
        self.assertItemsEqual(actual, expected,
            'should return all key, value pairs with keys beginning with prefix')

        actual = root.lookup_prefix('')
        expected = [('abc', 1), ('abd', 2), ('acd', 3), ('bcd', 4), ('bc', 5)]
        self.assertItemsEqual(actual, expected, 'found all pairs in the trie')

        actual = root.lookup_prefix('c')
        expected = []
        self.assertItemsEqual(actual, expected, 'found no keys matching prefix')

    def test_delete(self):
        root = TrieNode()
        root.insert('abc', 1)
        root.insert('abd', 2)
        root.insert('acd', 3)
        root.insert('bc', 4)
        root.insert('bcd', 5)

        root.delete('acd')
        self.assertIsNotNone(root.lookup('abc'), 'should still access abc')
        self.assertIsNotNone(root.lookup('abd'), 'should still access abc')

        root.delete('ab') # Key holds no value.
        self.assertIsNotNone(root.lookup('abc'), 'nothing is deleted')
        self.assertIsNotNone(root.lookup('abd'), 'nothing is deleted')

        root.delete('bc') # Key hods a value but has children.
        self.assertIsNone(root.lookup('bc'), 'value has been removed')
        self.assertIsNotNone(root.lookup('bcd'),
            'key with bc prefix are still accessible')

    def test_traverse(self):
        root = TrieNode()
        root.insert('acd', 3)
        root.insert('bc', 4)
        root.insert('abd', 2)
        root.insert('bcd', 5)
        root.insert('abc', 1)

        actual = root.traverse()
        expected = [('abc', 1), ('abd', 2), ('acd', 3), ('bc', 4), ('bcd', 5)]
        self.assertEqual(actual, expected,
            'should product the pairs sorted by key')


class TestTrie(unittest.TestCase):

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
