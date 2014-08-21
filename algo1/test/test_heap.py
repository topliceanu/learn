import unittest

from src.heap import heap_sort, Median


class HeapTest(unittest.TestCase):

    def test_heap_sort(self):
        a = [5,2,7,8,4,3,1,9,6]
        expected = [1,2,3,4,5,6,7,8,9]
        actual = heap_sort(a)
        self.assertEqual(actual, expected, 'should have sorted the array')

    def test_median_maintenance(self):
        m = Median()

        median = m.add(1)
        self.assertEqual(median, 1, 'fist elem')

        median = m.add(5)
        self.assertEqual(median, 5, 'fist elem')

        median = m.add(3)
        self.assertEqual(median, 3, 'fist elem')

        median = m.add(100)
        self.assertEqual(median, 5, 'fist elem')
