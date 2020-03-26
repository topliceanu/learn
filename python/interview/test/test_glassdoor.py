# -*- coding: utf-8 -*-

import unittest

from glassdoor import *


class TestGlassdoor(unittest.TestCase):

    def test_k_sorted_array(self):
        k = 3
        arr = [3,2,1,6,5,4,9,8,7]

        expected = [1,2,3,4,5,6,7,8,9]
        actual = k_sorted_array(arr, k)
        self.assertEqual(actual, expected, 'should correctly sort the array')

    def test_connected_zeros_in_array(self):
        arr = [
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0],
            [1,1,0,0,0,1,1],
            [0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
        ]
        actual = connected_zeros_in_array(arr)
        self.assertFalse(actual, 'should detect that not all zeroes are reachable')

        arr = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [1,1,1,0,1,1,1],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
        ]
        actual = connected_zeros_in_array(arr)
        self.assertTrue(actual, 'should detect that all zeroes are reachable')

    def test_binary_tree_level_traversal(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        a.add_child(b)
        a.add_child(c)
        b.add_child(d)
        b.add_child(e)
        c.add_child(f)

        expected = {1: {'a'}, 2: {'b', 'c'}, 3: {'d', 'e', 'f'}}
        actual = binary_tree_level_order_traversal(a)
        self.assertEqual(actual, expected, 'should traverse the tree correctly')

    def test_match(self):
        text = 'alexandru'
        pattern = 'al.*a.dru*'
        matched = match(text, pattern)
        self.assertTrue(matched, 'should discover pattern')

    def test_same_fringe(self):
        t1 = {'key': 1, 'children': [{'key': 2, 'children': []},
                                     {'key': 3, 'children': []}]}
        t2 = {'key': 4, 'children': [{'key': 2, 'children': []},
                                     {'key': 3, 'children': []}]}
        is_same = same_fringe(t1, t2)
        self.assertTrue(is_same, 'should detect the same fringe for both trees')

    def test_is_anagram(self):
        actual = is_anagram('cat', 'act')
        self.assertTrue(actual, 'are anagrams')

        actual = is_anagram('caat', 'acta')
        self.assertTrue(actual, 'are anagrams')

        actual = is_anagram('cats', 'fact')
        self.assertFalse(actual, 'are not anagrams')

    def test_find_anagrams_slow(self):
        needle = 'cat'
        haystack = 'actor'
        actual = find_anagrams_slow(needle, haystack)
        self.assertTrue(actual, 'found an anagram')

        needle = 'sat'
        haystack = 'actor'
        actual = find_anagrams_slow(needle, haystack)
        self.assertFalse(actual, 'couls find any anagrams')

    def test_delta(self):
        s1 = 'abc'
        s2 = 'bcd'
        actual = delta(s1, s2)
        expected = {'extra': ['d'], 'missing': ['a']}
        self.assertEqual(actual, expected, 'should detect the correct data')

        s1 = 'alexa'
        s2 = 'lexan'
        actual = delta(s1, s2)
        expected = {'extra': ['n'], 'missing': ['a']}
        self.assertEqual(actual, expected, 'should detect the correct data')

        s1 = 'aaa'
        s2 = 'aab'
        actual = delta(s1, s2)
        expected = {'extra': ['b'], 'missing': ['a']}
        self.assertEqual(actual, expected, 'should detect the correct data')

    def test_find_anagrams_fast(self):
        needle = 'cat'
        haystack = 'actor'
        actual = find_anagrams_fast(needle, haystack)
        self.assertTrue(actual, 'found an anagram')

        needle = 'sat'
        haystack = 'actor'
        actual = find_anagrams_fast(needle, haystack)
        self.assertFalse(actual, 'couls find any anagrams')
