# -*- coding: utf-8 -*-

import unittest

from add_to_numbers import Solution, ListNode

s = Solution()
global s

class TestAddTwoNumbers(unittest.TestCase):

    def test_solution(self):
        a = ListNode(val=2,
                next=ListNode(val=4,
                    next=ListNode(val=3, next=None)))
        b = ListNode(val=7,
                next=ListNode(val=0,
                    next=ListNode(val=8, next=None)))
        c = ListNode(val=9,
                next=ListNode(val=9,
                    next=ListNode(val=9, next=None)))
        zero = ListNode(val=0, next=None)
        a_plus_b = ListNode(val=9,
                next=ListNode(val=4,
                    next=ListNode(val=1,
                        next=ListNode(val=1, next=None))))
        b_plus_c = ListNode(val=6,
                next=ListNode(val=0,
                    next=ListNode(val=8,
                        next=ListNode(val=1, next=None))))
        c_plus_c = ListNode(val=8,
                next=ListNode(val=9,
                    next=ListNode(val=9,
                        next=ListNode(val=1, next=None))))
        tests = [
            (a, b, a_plus_b),
            (b, c, b_plus_c),
            (c, c, c_plus_c),
            (a, zero, a),
        ]
        for test in tests:
            actual = s.addTwoNumbers(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual.to_list(), expected.to_list(), \
                    'failed {} + {} expected {}, got {}'.format( \
                        test[0].to_list(), test[1].to_list(), \
                        expected.to_list(), actual.to_list()))
