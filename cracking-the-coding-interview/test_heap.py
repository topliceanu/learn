# -*- encoding:utf-8 -*-

import unittest

from heap import heapify, insert, extract_index

class TestHeap(unittest.TestCase):
    def test_heapify(self):
        arr = [5,3,1,2,4]
        heapify(arr)
        self.assertEqual(arr[0], 1, 'head of min-heap should be smallest value')

    def test_insert(self):
        arr = [5,3,1,2,4]
        heapify(arr)
        insert(arr, 0)
        self.assertEqual(arr[0], 0, 'new head of min-heap should be 0')

    def test_extract_index(self):
        arr = [5,3,1,2,4]
        heapify(arr)
        actual = extract_index(arr, 0)
        self.assertEqual(actual, 1, 'should pop the correct min')
        self.assertTrue(arr[0] != 1, 'new heap should miss the old min')
