# -*- coding: utf-8 -*-

import unittest

from src.skiplist import SkipList


class SkipListTest(unittest.TestCase):

    def test_init(self):
        sl = SkipList(3)

    def x_test_insert_with_one_level(self):
        sl = SkipList(1)
        for i in [3, 2, 1]:
            sl.insert(i)
        actual = sl.list_sorted()
        expected = [1, 2, 3]
        self.assertEqual(actual, expected, 'should have sorted the values')

    def test_insert_with_two_levels(self):
        sl = SkipList(2)
        for i in [3, 2, 1]:
            sl.insert(i)
        actual = set(sl.list_sorted(1))
        expected = set([1, 2, 3])
        self.assertTrue(actual.issubset(expected),
            'should have sorted the values')

    def x_test_list_sorted(self):
        sl = SkipList(1)
        for i in [4, 2, 5, 1, 0, 3]:
            sl.insert(i)
        actual = sl.list_sorted()
        expected = [0, 1, 2, 3, 4, 5]
        self.assertEqual(actual, expected, 'should have sorted the values')

    def test_lookup(self):
        sl = SkipList(2)
        for i in [4, 2, 5, 1, 0, 3]:
            sl.insert(i)
        self.assertTrue(sl.lookup(2), 'should detect that 2 is present')
        self.assertFalse(sl.lookup(6), 'should deted that 6 is not present')

    def test_lookup_large_corpus(self):
        sl = SkipList(10)
        for i in xrange(100):
            sl.insert(i)
        self.assertTrue(sl.lookup(47), 'should find the number')
        self.assertFalse(sl.lookup(123), 'should not find a number larger than 100')

    def test_delete(self):
        sl = SkipList(2)
        for i in [4, 2, 5, 1, 0, 3]:
            sl.insert(i)
        self.assertTrue(sl.lookup(2), 'should detect that 2 is present')

        self.assertTrue(sl.remove(2), '2 is found an removed')
        self.assertFalse(sl.lookup(2), '2 is no longer present')

        expected = set([0, 1, 3, 4, 5])
        level0 = set(sl.list_sorted())
        level1 = set(sl.list_sorted(1))
        self.assertEqual(level0, expected,
            'should have removed 2 from bottom level')
        self.assertTrue(level1.issubset(expected),
            'should have removed 2 from top level')
