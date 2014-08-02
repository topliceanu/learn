# -*- coding: utf-8 -*-

import unittest

from src.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def setUp(self):
        pass

    def test_merge_sort(self):
        a = [5, 3, 2, 8, 9, 1]
        b = merge_sort(a)
        expected = [1, 2, 3, 5, 8, 9]
        self.assertEqual(b, expected, 'should have sorted the input array')

    def tearDown(self):
        pass


if __name__ is '__main__':
    unittest.main()
