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
