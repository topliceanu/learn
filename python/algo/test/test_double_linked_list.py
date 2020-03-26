# -*- coding: utf-8 -*-


import unittest

from src.double_linked_list import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):


    def test_insert_head_single(self):
        l = DoubleLinkedList()
        l.insert_head(1)

        self.assertEqual(len(l), 1, 'should have one element inserted')
        self.assertEqual(l.head.value, 1, 'first value is the inserted one')
        self.assertEqual(l.last.value, 1, 'last value is the inserted one')
        self.assertIsNone(l.head.pred, 'node is alone in the list')
        self.assertIsNone(l.head.succ, 'node is alone in the list')

    def test_insert_last(self):
        pass

    def test_peek_head(self):
        pass

    def test_peek_last(self):
        pass

    def test_remove_head(self):
        pass

    def test_remove_last(self):
        pass
