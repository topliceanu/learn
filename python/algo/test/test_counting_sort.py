# -*- coding: utf-8 -*-

import unittest

from src.counting_sort import counting_sort


class CountingSortTest(unittest.TestCase):

    def test_counting_sort(self):
        data = [4,1,2,1,2,5,2,3,9,6,6,3,4,5,6,7,3,4,8,3,6,7,8,9,4,5,9]
        actual = counting_sort(data)
        expected = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9, 9]
        self.assertEqual(actual, expected, 'should return the expected data');
