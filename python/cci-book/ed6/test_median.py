# -*- conding: utf-8 -*-

import unittest

from median import Median

class TestMedian(unittest.TestCase):
    def test_median(self):
        arr =     [1,2,2,3,4,4,5,5,5,5,5,5,5]
        medians = [1,1,2,2,2,2,3,3,4,4,4,4,5]
        m = Median()
        for i in range(len(arr)):
            m.insert(arr[i])
            self.assertEqual(m.median, medians[i],
                'wrong value for case {}'.format(i+1))

