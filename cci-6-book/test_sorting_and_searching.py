# -*- coding: utf-8 -*-

import unittest

from sorting_and_searching import bubble_sort, selection_sort, \
    merge_sort, quick_sort, heap_sort

class TestSortingAndSearch(unittest.TestCase):
    def test_sort(self):
        fns = {
            "bubble": (lambda arr: bubble_sort(arr)),
            "selection": (lambda arr: selection_sort(arr)),
            "merge": (lambda arr: merge_sort(arr)),
            "heap": (lambda arr: heap_sort(arr)),
            #"quick": (lambda arr: quick_sort(arr)), # TODO FIXME
        }
        tests = [
            ([], []), # edge case: empty
            ([1], [1]), # edge case: one element
            ([1, 2, 3], [1, 2, 3]), # edge case: already sorted
            ([3, 2, 1], [1, 2, 3]), # edge case: sorted in the other order
            ([1, 5, 3, 2, 4], [1, 2, 3, 4, 5]), # sort an array
            ([2, 1, 4, 3], [1, 2, 3, 4]), # sort odd length array
            ([2, 2, 2, 1, 1, 1], [1, 1, 1, 2, 2, 2]), # sort array with duplicates
        ]
        for test in tests:
            for (fn_name, fn) in fns.items():
                actual = fn(test[0])
                expected = test[1]
                self.assertEqual(actual, expected,
                        'failed test={} for fn={} with actual={}'
                        .format(test, fn_name, actual))
