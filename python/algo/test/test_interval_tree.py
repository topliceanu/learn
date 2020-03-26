# -*- coding: utf-8 -*-


import unittest

from src.interval_tree import IntervalTree


class TestIntervalTree(unittest.TestCase):

    def test_insert(self):
        tree = IntervalTree()
        tree.insert((20, 36))
        tree.insert((3, 41))
        tree.insert((0, 1))
        tree.insert((10, 15))
        tree.insert((29, 99))

        self.assertEqual(tree.root.key, 20, 'correct tree structure')
        self.assertEqual(tree.root.end, 36, 'correct tree structure')
        self.assertEqual(tree.root.high, 99, 'correct tree structure')
        self.assertEqual(tree.root.left.key, 3, 'correct tree structure')
        self.assertEqual(tree.root.left.end, 41, 'correct tree structure')
        self.assertEqual(tree.root.left.high, 41, 'correct tree structure')
        self.assertEqual(tree.root.left.left.key, 0, 'correct tree structure')
        self.assertEqual(tree.root.left.left.end, 1, 'correct tree structure')
        self.assertEqual(tree.root.left.left.high, 1, 'correct tree structure')
        self.assertEqual(tree.root.left.right.key, 10, 'correct tree structure')
        self.assertEqual(tree.root.left.right.end, 15, 'correct tree structure')
        self.assertEqual(tree.root.left.right.high, 15, 'correct tree structure')
        self.assertEqual(tree.root.right.key, 29, 'correct tree structure')
        self.assertEqual(tree.root.right.end, 99, 'correct tree structure')
        self.assertEqual(tree.root.right.high, 99, 'correct tree structure')

    def test_delete(self):
        pass

    def test_lookup_value(self):
        pass

    def test_lookup_interval(self):
        pass
