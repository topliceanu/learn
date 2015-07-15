# -*- coding: utf-8 -*-

import unittest

from cracking_the_coding_interview import *


class CrackingTheCodeInterview(unittest.TestCase):

    # Chapter 1: Arrays and Strings

    def test_problem_1_1(self):
        data = 'alexandru'
        self.assertFalse(problem_1_1(data), 'should detect duplicate chars')

        data = 'alex'
        self.assertTrue(problem_1_1(data), 'all chars are unique')

        data = 'alexandru'
        self.assertFalse(problem_1_1_bis(data), 'should detect duplicate chars')

        data = 'alex'
        self.assertTrue(problem_1_1_bis(data), 'all chars are unique')

    def test_problem_1_2(self):
        data = 'alex$'
        expected = 'xela$'
        actual = problem_1_2(data)
        self.assertEqual(actual, expected, 'should invert correctly')

    def test_problem_1_3(self):
        data = ""
        expected = ""
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "a"
        expected = "a"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "abc"
        expected = "abc"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "abcc"
        expected = "abc"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "aabc"
        expected = "abc"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "abca"
        expected = "abca"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "aaaa"
        expected = "a"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

    def test_problem_1_4(self):
        s1 = 'cat'
        s2 = 'act'
        self.assertTrue(problem_1_4(s1, s2), 'are anagrams')

        s1 = 'cats'
        s2 = 'act'
        self.assertFalse(problem_1_4(s1, s2), 'are not anagrams')

        s1 = 'aab'
        s2 = 'aba'
        self.assertTrue(problem_1_4(s1, s2), 'are anagrams')

        s1 = 'aab'
        s2 = 'abc'
        self.assertFalse(problem_1_4(s1, s2), 'are not anagrams')

    def test_problem_1_5(self):
        s = '   '
        expected = '%20%20%20'
        actual = problem_1_5(s)
        self.assertEqual(actual, expected, 'correct url encode spaces')

        s = ' a '
        expected = '%20a%20'
        actual = problem_1_5(s)
        self.assertEqual(actual, expected, 'correct url encode spaces')

        s = 'ab'
        expected = 'ab'
        actual = problem_1_5(s)
        self.assertEqual(actual, expected, 'correct url encode spaces')

    def test_problem_1_6(self):
        arr = [
            [ 1,  2,  3,  4,  5],
            [ 6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        actual = problem_1_6(arr)
        expected = [
            [21, 16, 11,  6, 1],
            [22, 17, 12,  7, 2],
            [23, 18, 13,  8, 3],
            [24, 19, 14,  9, 4],
            [25, 20, 15, 10, 5]
        ]
        self.assertItemsEqual(actual, expected, 'should rotate array')

    def test_problem_1_7(self):
        arr = [
            [ 0,  2,  3,  4,  5],
            [ 6,  7,  8,  0, 10],
            [ 0, 12,  0, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        expected = [
            [ 0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0],
            [ 0, 17,  0,  0, 20],
            [ 0, 22,  0,  0, 25],
        ]
        actual = problem_1_7(arr)
        self.assertItemsEqual(actual, expected, 'should turn correct items to zero')

    def test_problem_1_8(self):
        s1 = 'waterbottle'
        s2 = 'erbottlewat'
        self.assertTrue(problem_1_8(s1, s2), 'should detect rotated string')

        s1 = 'waterbottle'
        s2 = 'wabottleter'
        self.assertFalse(problem_1_8(s1, s2), 'should not detect any rotated string')

        s1 = 'abcd'
        s2 = 'bcdab'
        self.assertFalse(problem_1_8(s1, s2), 'should not detect any rotated string')

    # Chapter 2: Linked Lists.

    def test_problem_2_1(self):
        initial = SingleLinkedListNode.from_list([1,2,2,2,3,4,5])
        actual = problem_2_1(initial)
        expected = [1,2,3,4,5]
        self.assertEqual(actual.to_list(), expected, 'should remove duplicate 2s')

    def test_problem_2_2(self):
        l = SingleLinkedListNode.from_list([1,2,3,4,5])
        expected = 4
        actual = problem_2_2(l, 2).key
        self.assertEqual(actual, expected, 'should detect the correct value')

        l = SingleLinkedListNode.from_list([1])
        expected = 4
        actual = problem_2_2(l, 2)
        self.assertIsNone(actual, 'should detect index error')

        self.assertRaises(Exception, problem_2_2, None, -2,
            'should detect bad input params and raise exception')

        l = SingleLinkedListNode.from_list([1,2,3,4,5])
        expected = 5
        actual = problem_2_2(l, 1).key
        self.assertEqual(actual, expected, 'should detect the correct value')

        l = SingleLinkedListNode.from_list([1,2,3,4,5])
        expected = 1
        actual = problem_2_2(l, 5).key
        self.assertEqual(actual, expected, 'should detect the correct value')

    def test_problem_2_3(self):
        l = SingleLinkedListNode.from_list([1,2,3,4,5])
        node = l.next.next # Node with key 3.
        problem_2_3(node)

        actual = l.to_list()
        expected = [1,2,4,5]
        self.assertEqual(actual, expected, 'should have removed the key 3')

        l = SingleLinkedListNode.from_list([1,2,3,4,5])
        node = l.next.next.next.next # Node with key 5.
        self.assertRaises(Exception, problem_2_3, node,
            'should detect the last node in the list')

    def test_problem_2_4(self):
        l1 = SingleLinkedListNode.from_list([2,3,4])
        l2 = SingleLinkedListNode.from_list([1,2,3])
        expected = SingleLinkedListNode.from_list([3,5,7])
        actual = problem_2_4(l1, l2)
        self.assertEqual(actual.to_list(), expected.to_list(),
            'should compute sum of two regular numbers')

        l1 = SingleLinkedListNode.from_list([])
        l2 = SingleLinkedListNode.from_list([1,2,3])
        expected = SingleLinkedListNode.from_list([1,2,3])
        actual = problem_2_4(l1, l2)
        self.assertEqual(actual.to_list(), expected.to_list(),
            'should compute sum when the other element is empty')

        l1 = SingleLinkedListNode.from_list([1,2,3])
        l2 = SingleLinkedListNode.from_list([2])
        expected = SingleLinkedListNode.from_list([3,2,3])
        actual = problem_2_4(l1, l2)
        self.assertEqual(actual.to_list(), expected.to_list(),
            'should compute sum when one number has less digits')

        l1 = SingleLinkedListNode.from_list([9,9,9])
        l2 = SingleLinkedListNode.from_list([9,9,9])
        expected = SingleLinkedListNode.from_list([8,9,9,1])
        actual = problem_2_4(l1, l2)
        self.assertEqual(actual.to_list(), expected.to_list(),
            'should compute sum when digit overflow occurs')

    def test_problem_2_5(self):
        l = SingleLinkedListNode.from_list([1,2,3,4,5,6,7])
        start = l.next.next # Node with key 3.
        last = start.next.next.next.next # Node with key 7.
        last.next = start

        actual = problem_2_5(l)
        self.assertEqual(actual, start, 'should detect the start node')

    # Chapter 5: Bit Manipulation.

    def test_problem_5_1(self):
        n = int('10000000000', 2)
        m = int('10101', 2)
        i = 2
        j = 6
        actual = problem_5_1(n, m, i, j)
        expected = int('10001010100', 2)
        self.assertEqual(actual, expected, 'should produce the correct value')

        n = int('11111111111', 2)
        m = int('10101', 2)
        i = 2
        j = 6
        actual = problem_5_1(n, m, i, j)
        expected = int('11111010111', 2)
        self.assertEqual(actual, expected, 'should produce the correct value')

    def x_test_problem_5_2(self):
        n = 3.17
        actual = problem_5_2(n)
        expected = False
        self.assertEqual(actual, expected, 'should return the correct value')

    def test_problem_10_6(self):
        points = [(2,3), (4,5), (6,7), (8,9), (1,1), (2,2), (3,3)]
        expected = {(2,3), (4,5), (6,7), (8,9)}
        actual = problem_10_6(points)
        self.assertEqual(actual, expected, 'should find largest set of points')

    def test_problem_10_7(self):
        # NOTE: THIS IS INCORRECT!
        self.assertEqual(problem_10_7(0), 3*5*7, 'should have worked')
        self.assertEqual(problem_10_7(1), 3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7(2), 3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7(3), 3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(4), 3*3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7(5), 3*3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7(6), 3*3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(7), 3*5*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7(8), 3*3*3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7(9), 3*5*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(10), 3*3*3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7(11), 3*5*7*7*7, 'should have worked')
        self.assertEqual(problem_10_7(12), 3*3*3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(13), 3*3*5*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(14), 3*3*3*5*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(15), 3*3*5*5*5*7*7, 'should have worked')

    def test_problem_10_7_bis(self):
        self.assertEqual(problem_10_7_bis(0), 3*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(1), 3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(2), 3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(3), 3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(4), 3*3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(5), 3*3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(6), 3*3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(7), 3*5*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(8), 3*3*3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(9), 3*5*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(10), 3*3*3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(11), 3*5*7*7*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(12), 3*3*3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(13), 3*3*5*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(14), 3*3*3*3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(15), 3*3*5*5*7*7, 'should have worked')

    def test_problem_3_5_my_queue(self):
        q = MyQueue()
        q.enqueue(1)
        q.enqueue(2)

        self.assertEqual(len(q), 2, 'two elements in the queue')
        self.assertEqual(q.dequeue(), 1, 'should return the first value')
        self.assertEqual(q.dequeue(), 2, 'should return the second value')
        self.assertIsNone(q.dequeue(), 'queue is empty')
