# -*- coding: utf-8 -*-

import unittest

from src.radix_sort import radix_sort


class RadixSortTest(unittest.TestCase):

    def test_radix_sort(self):
        subject = [18,5,100,3,1,19,6,0,7,4,2]
        expected = [0,1,2,3,4,5,6,7,18,19,100]
        actual = radix_sort(subject)
        self.assertEqual(actual, expected, 'should sort the input array')
