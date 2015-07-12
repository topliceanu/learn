# -*- coding: utf-8 -*-

import unittest

from careercup import *


class TestCareerCup(unittest.TestCase):

    def test_find_pairs_in_list(self):
        arr = [1,2,3,4,5,6,7,8]
        k = 3
        l = 2
        actual = find_pairs_in_list(arr, k, l)
        self.assertTrue(actual, 'should have found at least one pair for k,l')

    def test_farm_rain_fall(self):
        plots = [
            [2, 5, 2],
            [2, 4, 7],
            [3, 6, 9]
        ]
        expected = [
            ['A', 'B', 'B'],
            ['A', 'A', 'B'],
            ['A', 'A', 'A']
        ]
        actual = farm_rainfall(plots)
        self.assertEqual(actual, expected, 'should produce the correct syncs')

        plots = [
            [10]
        ]
        expected = [
            ['A']
        ]
        actual = farm_rainfall(plots)
        self.assertEqual(actual, expected, 'should produce the correct syncs')

        plots = [
            [1, 0, 2, 5, 8],
            [2, 3, 4, 7, 9],
            [3, 5, 7, 8, 9],
            [1, 2, 5, 4, 2],
            [3, 3, 5, 2, 1]
        ]
        expected = [
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A'],
            ['B', 'B', 'A', 'C', 'C'],
            ['B', 'B', 'B', 'C', 'C'],
            ['B', 'B', 'C', 'C', 'C']
        ]
        actual = farm_rainfall(plots)
        self.assertEqual(actual, expected, 'should produce the correct syncs')

        plots = [
            [0, 2, 1, 3],
            [2, 1, 0, 4],
            [3, 3, 3, 3],
            [5, 5, 2, 1]
        ]
        expected = [
            ['A', 'A', 'B', 'B'],
            ['A', 'B', 'B', 'B'],
            ['A', 'B', 'B', 'C'],
            ['A', 'C', 'C', 'C']
        ]
        actual = farm_rainfall(plots)
        self.assertEqual(actual, expected, 'should produce the correct syncs')

    def test_sort_letters(self):
        # Five test cases:
        # 1. more letters in template than in word.
        word = 'cb'
        template = 'abc'
        expected = 'bc'
        actual = sort_letters(word, template)
        self.assertEqual(actual, expected, 'should sort the letters correctly')

        # 2. more letters in word than in template.
        word = 'abc'
        template = 'ba'
        expected = 'bac'
        actual = sort_letters(word, template)
        self.assertEqual(actual, expected, 'should sort the letters correctly')

        # 3. duplicate letters in the template.
        word = 'cba'
        template = 'aabc'
        expected = 'abc'
        actual = sort_letters(word, template)
        self.assertEqual(actual, expected, 'should sort the letters correctly')

        # 4. duplicate letters in the word.
        word = 'aabc'
        template = 'cba'
        expected = 'cbaa'
        actual = sort_letters(word, template)
        self.assertEqual(actual, expected, 'should sort the letters correctly')

        # 5. same letters in both template and example.
        word = 'abc'
        template = 'bac'
        expected = 'bac'
        actual = sort_letters(word, template)
        self.assertEqual(actual, expected, 'should sort the letters correctly')

    def test_binary_search_rotated(self):
        data = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
        found = binary_search_rotated(5, data, 0, len(data)-1)
        self.assertTrue(found, 'should find 5')

        data = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
        found = binary_search_rotated(10, data, 0, len(data)-1)
        self.assertTrue(found, 'should find 10')

        data = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
        found = binary_search_rotated(11, data, 0, len(data)-1)
        self.assertFalse(found, 'should not find 11')

        data = [4, 4, 5, 6, 7, 1, 2, 3, 4, 4, 4, 4]
        found = binary_search_rotated(5, data, 0, len(data)-1)
        self.assertTrue(found, 'should find 5')

    def test_merge_linked_list(self):
        l1 = {'value': 0, 'next': {'value': 1, 'next': {'value': 2, 'next': None}}}
        l2 = {'value': 5, 'next': {'value': 6, 'next': {'value': 7, 'next': None}}}
        l3 = {'value': 10, 'next': {'value': 11, 'next': {'value': 12, 'next': None}}}


        expected = {'value': 0, 'next': {'value': 1, 'next': {'value': 2, 'next':
                   {'value': 5, 'next': {'value': 6, 'next': {'value': 7, 'next':
                   {'value': 10, 'next': {'value': 11, 'next': {'value': 12, 'next': None}}}}}}}}}

        actual = merge_linked_lists([l1, l2, l3])
        self.assertEqual(actual, expected, 'should build the correct list')

    def test_paint_houses(self):
        n = 5
        m = 3
        cost = {0: {1: 10, 2: 11}, 1: {2: 7, 0: 8}, 2: {0: 9, 1: 10}}

        (actual_min_cost, actual_colors) = paint_houses(n, m, cost)

        expected_min_cost = 33
        expected_colors = [1,2,1,2,0]

        self.assertEqual(actual_min_cost, expected_min_cost, \
            'correctly computes the min cost')
        self.assertEqual(actual_colors, expected_colors,
            'should compute accurate colors')

    def test_shuffle(self):
        a = [1,2,3,4,5]
        b = a[:]
        self.assertNotEqual(a, shuffle(b), 'should correctly shuffle items')

    def teest_rewire_pointers(self):
        l = {'val': 'A', 'next': {'val': 'B', 'next': {'val': 'C', 'next': {'val': 'D', 'next': None}}}}
        actual = rewire_pointers(l)
        expected = {'val': 'B', 'next': {'val': 'A', 'next': {'val': 'D', 'next': {'val': 'C', 'next': None}}}}
        self.assertEqual(actual, expected, 'should compute it correctly')

        l = {'val': 'A', 'next': None}
        actual = rewire_pointers(l)
        expected = {'val': 'A', 'next': None}
        self.assertEqual(actual, expected, 'should compute it correctly')

        l = {'val': 'A', 'next': {'val': 'B', 'next': {'val': 'C', 'next': None}}}
        actual = rewire_pointers(l)
        expected = {'val': 'B', 'next': {'val': 'A', 'next': {'val': 'C', 'next': None}}}
        self.assertEqual(actual, expected, 'should compute it correctly')
