# -*- coding: utf-8 -*-

import unittest

from remove_nth_from_end import remove_nth_from_end, ListNode
from helpers import make_linked_list, from_linked_list

class TestRemoveNthFromEnd(unittest.TestCase):
    def test_remove_nth_from_end(self):
        tests = [
            ([1,2,3,4,5], 2, [1,2,3,5]),
            ([1,2,3,4,5], 10, [1,2,3,4,5]),
            ([1,2,3,4,5], -10, [1,2,3,4,5]),
            ([1,2,3,4,5], 1, [1,2,3,4]),
            ([1,2,3,4,5], 0, [1,2,3,4,5]),
        ]
        for test in tests:
            ls = make_linked_list(test[0])
            result = remove_nth_from_end(ls, test[1])
            actual = from_linked_list(result)
            expected = test[2]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))
