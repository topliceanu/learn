# -*- coding: utf-8 -*-

import unittest

from src.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        found = binary_search(5, arr, 0, len(arr)-1)
        self.assertTrue(found, '5 is in array')

        found = binary_search(5.5, arr, 0, len(arr)-1)
        self.assertFalse(found, '5.5 is not in array')

        found = binary_search(17, arr, 0, len(arr)-1)
        self.assertFalse(found, '17 is not in array')

        found = binary_search(15, arr, 0, len(arr)-1)
        self.assertTrue(found, '15 is in array')

        arr = [1,2,3,4,4,4,4,4,4,4,4,4,4,5,6,7]

        found = binary_search(2, arr, 0, len(arr)-1)
        self.assertTrue(found, '2 is in array')

        found = binary_search(6, arr, 0, len(arr)-1)
        self.assertTrue(found, '6 is in array')
