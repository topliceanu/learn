# -*- coding: utf-8 -*-

import unittest

from src.selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self):
        arr = [9,8,7,6,5,4,3,2,1]
        selection_sort(arr)
        expected = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(arr, expected, 'should have sorted it correctly')
