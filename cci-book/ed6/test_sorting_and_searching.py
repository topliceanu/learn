# -*- coding: utf-8 -*-

import unittest

from sorting_and_searching import bubble_sort, selection_sort, \
    merge_sort, quick_sort, heap_sort, sorted_merge, group_anagrams, \
    search_rotated, sorted_search_no_size, sparse_search, sort_big_file

class TestSortingAndSearch(unittest.TestCase):
    def test_sorted_merge(self):
        tests = [
            ([1,3,5], [2,4,6], [1,2,3,4,5,6])
        ]
        for test in tests:
            actual = sorted_merge(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))

    def test_group_anagrams(self):
        tests = [
            (["pot", "lea", "top", "ela"], ["lea", "ela", "pot", "top"]),
        ]
        for test in tests:
            actual = group_anagrams(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))

    def test_search_rotated(self):
        tests = [
            ([1, 2, 3, 4, 5], 5, 4),
            ([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5, 8),
            ([8, 9, 1, 2, 3, 4, 5, 6, 7], 5, 6),
            ([3, 4, 5, 6, 7, 8, 9, 1, 2], 5, 2),
        ]
        for test in tests:
            actual = search_rotated(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))

    def test_sorted_search_no_size(self):
        def elementAt(arr, idx):
            if idx >= len(arr):
                return -1
            else:
                return arr[idx]
        def makeElementAt(arr):
            return lambda idx: elementAt(arr, idx)
        tests = [
            ([1, 2, 3, 4, 5], 5, 4),
            ([1, 1, 2, 3, 3, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25], 7, 8),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 7),
        ]
        for test in tests:
            actual = sorted_search_no_size(test[1], makeElementAt(test[0]))
            expected = test[2]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))

    def test_sparse_search(self):
        tests = [
            (["at", "", "", "" , "ball", "", "", "car", "" , "" , "dad", ""], "ball", 4),
            (["", "", "" , "", "", "car", "" , "" , "dad", ""], "ball", None),
        ]
        for test in tests:
            actual = sparse_search(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))

    def test_sort_big_file(self):
        tests = [
            (["at", "ale", "bizz", "ball", "car", "dud", "dad"],
             ["ale", "at", "ball", "bizz", "car", "dad", "dud"]),
        ]
        for test in tests:
            actual = sort_big_file(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))

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
