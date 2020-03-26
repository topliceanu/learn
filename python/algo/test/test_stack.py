# -*- coding: utf-8 -*-

import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):

    def test_push(self):
        s = Stack()

        s.push(1)
        self.assertEqual(s.top['value'], 1, 'should have inserted 1')
        self.assertIsNone(s.top['prev'], 'should have nothing before')

        s.push(2)
        self.assertEqual(s.top['value'], 2, 'should have 2 as top')
        self.assertEqual(s.top['prev']['value'], 1, 'should have 1 before')
        self.assertIsNone(s.top['prev']['prev'], '1 is the last value')

    def test_pop(self):
        s = Stack()

        value = s.pop()
        self.assertIsNone(value, 'should return None from empty stack')

        s.push(1)
        value = s.pop()
        self.assertEqual(value, 1, 'should return the stack value')
        self.assertEqual(s.pop(), None, 'should remain an empty stack')

    def test_len(self):
        s = Stack()
        self.assertEqual(len(s), 0, 'no elements yet')

        s.push(1)
        self.assertEqual(len(s), 1, 'one element')

        s.push(2)
        self.assertEqual(len(s), 2, 'two elements')

        s.pop()
        self.assertEqual(len(s), 1, 'one element left')

        s.pop()
        self.assertEqual(len(s), 0, 'no elements left')

        s.pop()
        self.assertEqual(len(s), 0, 'still no elements left')
