# -*- coding: utf-8 -*-

import unittest

from cracking_the_coding_interview import *


class BitManipulation(unittest.TestCase):

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
