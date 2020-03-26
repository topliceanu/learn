# -*- coding: utf-8 -*-

import unittest

from src.hash_table import ChainingHash, OpenAddressingHash, \
                           two_sum_problem_sort, two_sum_problem_hash


class TestHashTable(unittest.TestCase):

    # Hash Table implementation with chaining conflict resolution.

    def test_hash_insert(self):
        """ Forces a hash collision. """
        h = ChainingHash(7)
        h.insert(14)
        h.insert(21)
        self.assertEqual(h.data[0], [14, 21], 'should have created a collision')

    def test_hash_lookup(self):
        h = ChainingHash(5)
        h.insert(20)
        self.assertTrue(h.lookup(20), 'should find the value 20')

    def test_hash_delete(self):
        h = ChainingHash(5)

        h.insert(20)
        self.assertTrue(h.lookup(20), 'should find the value 20')

        h.delete(20)
        self.assertFalse(h.lookup(20), '20 is no more in the hash')

    def test_export(self):
        h = ChainingHash(5)
        for number in range(1,20):
            h.insert(number)
        self.assertEqual(set(range(1,20)), set(h.export()),
            'should return all the input data')

    # Hash Table implementation with open addressing (double hashing)
    # conflict resolution.

    def test_hash_insert(self):
        """ Forces a hash collision. """
        h = OpenAddressingHash(7)
        h.insert(14)
        h.insert(21)
        self.assertEqual(h.data[0], 14, 'should have avaoided collision')
        self.assertEqual(h.data[4], 21, 'should have created a collision')

    def test_hash_lookup(self):
        h = OpenAddressingHash(5)
        h.insert(20)
        self.assertTrue(h.lookup(20), 'should find the value 20')

    def test_hash_delete(self):
        h = OpenAddressingHash(5)

        h.insert(20)
        self.assertTrue(h.lookup(20), 'should find the value 20')

        h.delete(20)
        self.assertFalse(h.lookup(20), '20 is no more in the hash')

    def test_export(self):
        h = OpenAddressingHash(100)
        for number in range(1,20):
            h.insert(number)
        self.assertEqual(set(range(1,20)), set(h.export()),
            'should return all the input data')

    # Hash Table use cases.

    def test_two_sum_problem_sort(self):
        a = [4,3,2,6,5,8,9,1,0,7]
        total = 7
        expected = [(0,7), (1,6), (2,5), (3,4), (4,3), (5,2), (6,1), (7,0)]
        actual = two_sum_problem_sort(a, total)
        self.assertEqual(actual, expected, 'should return all matching pairs')

    def test_two_sum_problem_sort_with_distinct_results(self):
        a = [0,1,2,3,3,4,5,6]
        total = 6
        expected = [(0,6), (1,5), (2,4), (4,2), (5,1), (6,0)]
        actual = two_sum_problem_sort(a, total, distinct=True)
        self.assertEqual(actual, expected,
            'should return all matching pairs with distinct results')

    def test_two_sum_problem_hash(self):
        a = [4,3,2,6,5,8,9,1,0,7]
        total = 7
        expected = [(4,3), (3,4), (2,5), (6,1), (5,2), (1,6), (0,7), (7,0)]
        actual = two_sum_problem_hash(a, total)
        self.assertEqual(actual, expected, 'should return all matching pairs')

    def test_two_sum_problem_hash_with_distinct_results(self):
        a = [0,1,2,3,3,4,5,6]
        total = 6
        expected = [(0,6), (1,5), (2,4), (4,2), (5,1), (6,0)]
        actual = two_sum_problem_hash(a, total, distinct=True)
        self.assertEqual(actual, expected,
            'should return all matching pairs with distinct results')
