# -*- coding: utf-8 -*-


import unittest

from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        q = Queue()

        q.enqueue(1)
        self.assertEqual(q.head['value'], q.tail['value'], 'tail and head are the same')

        q.enqueue(2)
        self.assertEqual(q.head['value'], 2, 'head is now the new value')
        self.assertIsNone(q.head['prev'], 'head is not linked to the next node')
        self.assertEqual(q.tail['value'], 1, 'first value is now tail')
        self.assertEqual(q.tail['prev']['value'], 2, 'tail is linked to head')

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)

        value = q.dequeue()
        self.assertEqual(value, 1, 'should return the first inserted item')
        self.assertEqual(q.head['value'], q.tail['value'],
            'tail and head are the same after an dequeue')

        value = q.dequeue()
        self.assertEqual(value, 2, 'should return the second inserted item')
        self.assertIsNone(q.head, 'head is None')
        self.assertIsNone(q.tail, 'tail is None')
