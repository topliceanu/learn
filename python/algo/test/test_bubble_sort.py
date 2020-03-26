# -*- coding: utf-8 -*-

import unittest

from src.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [9,8,7,6,5,4,3,2,1]
        bubble_sort(arr)
        expected = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(arr, expected, 'should have sorted the list in place')
