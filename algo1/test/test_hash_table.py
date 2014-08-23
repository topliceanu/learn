# -*- coding: utf-8 -*-

import unittest

from src.hash_table import Hash, two_sum_problem_sort, two_sum_problem_hash


class TestHashTable(unittest.TestCase):

    # Hash Table implementation.

    def test_hash_insert(self):
        """ Forces a hash collision. """
        h = Hash(7)
        h.insert(14)
        h.insert(21)
        self.assertEqual(h.data[0], [14, 21], 'should have created a collision')

    def test_hash_lookup(self):
        h = Hash(5)
        h.insert(20)
        self.assertTrue(h.lookup(20), 'should find the value 20')

    def test_hash_delete(self):
        h = Hash(5)

        h.insert(20)
        self.assertTrue(h.lookup(20), 'should find the value 20')

        h.delete(20)
        self.assertFalse(h.lookup(20), '20 is no more in the hash')

    # Hash Table use cases.

    def test_two_sum_problem_sort(self):
        a = [4,3,2,6,5,8,9,1,0,7]
        total = 7
        expected = [(0,7), (1,6), (2,5), (3,4), (4,3), (5,2), (6,1), (7,0)]
        actual = two_sum_problem_sort(a, total)
        self.assertEqual(actual, expected, 'should return all matching pairs')

    def test_two_sum_problem_hash(self):
        a = [4,3,2,6,5,8,9,1,0,7]
        total = 7
        expected = [(4,3), (3,4), (2,5), (6,1), (5,2), (1,6), (0,7), (7,0)]
        actual = two_sum_problem_hash(a, total)
        self.assertEqual(actual, expected, 'should return all matching pairs')
