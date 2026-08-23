# -*- coding: utf-8 -*-

import unittest

from linked_lists import LinkedListNode, \
    from_list, to_list, value, goto, \
    remove_dups, kth_to_last, delete_middle

class TestLinkedLists(unittest.TestCase):
    def test_remove_dups(self):
        tests = [
            ([], []),
            ([1], [1]),
            ([1, 1, 1, 1], [1]),
            ([1, 1, 1, 1, 2], [1, 2]),
            ([1, 2, 2, 3], [1, 2, 3]),
            ([1, 1, 1, 2, 2], [1, 2]),
            ([1, 2, 3, 4], [1, 2, 3, 4]),
        ]
        for test in tests:
            head = from_list(test[0])
            actual = to_list(remove_dups(head))
            expected = test[1]
            self.assertEqual(actual, expected, 'Failed case={} with actual={}'
                    .format(test, actual))

    def test_kth_to_last(self):
        tests = [
            ([], 0, None),
            ([], 100, None),
            ([1], 0, 1),
            ([1, 2, 3], 0, 3),
            ([1, 2, 3], 1, 2),
            ([1, 2, 3], 2, 1),
            ([1, 2, 3], 3, None),
        ]
        tests = [
            ([1, 2, 3], 0, 3),
            ([1, 2, 3], 3, None),
        ]
        for test in tests:
            head, k, expected = from_list(test[0]), test[1], test[2]
            actual = value(kth_to_last(head, k))
            self.assertEqual(actual, expected, 'failed case={} with actual={}'
                    .format(test, actual))

    def test_delete_middle(self):
        tests = [
            (['a', 'b', 'c'], 'b', ['a', 'c']),
            (['a', 'b', 'c', 'd', 'e', 'f'], 'd', ['a', 'b', 'c', 'e', 'f']),
        ]
        for test in tests:
            head = from_list(test[0])
            middle = goto(head, test[1])
            expected = test[2]
            delete_middle(middle)
            actual = to_list(head)
            self.assertEqual(actual, expected, 'failed case={} with actual={}'
                    .format(test, actual))
