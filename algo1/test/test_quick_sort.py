import unittest

from src.quick_sort import quick_sort, partition, pick_pivot


class QuickSortTest(unittest.TestCase):

    def test_partition_splits_array_by_pivot(self):
        arr = [3, 8, 2, 5, 1, 4, 7, 6]
        expected = [1, 2, 3, 5, 8, 4, 7, 6]
        actual = partition(arr, 0, len(arr))
        self.assertEqual(actual, expected)

    def test_pick_pivot(self):
        pivot = pick_pivot(1, 10)
        self.assertIn(pivot, range(1, 11))
