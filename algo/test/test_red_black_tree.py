# -*- conding:utf-8 -*-

import unittest

from src.red_black_tree import RedBlackTree, KEY


class RedBlackTreeTest(unittest.TestCase):

    def test_build(self):
        """ Just makes sure the tree is built without errors. """
        b = RedBlackTree.build([3,1,2,5,4])

    def test_search(self):
        b = RedBlackTree.build([3,1,2,5,4])

        self.assertIsNotNone(b.search(3), 'should find 3 in the bst')
        self.assertIsNotNone(b.search(1), 'should find 1 in the bst')
        self.assertIsNotNone(b.search(2), 'should find 2 in the bst')
        self.assertIsNotNone(b.search(5), 'should find 5 in the bst')
        self.assertIsNotNone(b.search(4), 'should find 4 in the bst')
        self.assertIsNone(b.search(10), 'should not find 10 in the bst')

    def test_max(self):
        b = RedBlackTree.build([3,1,2,5,4])

        self.assertEqual(b.get_max()[KEY], 5, 'should find the max value')

    def test_min(self):
        b = RedBlackTree.build([3,1,2,5,4])

        self.assertEqual(b.get_min()[KEY], 1, 'should find the min value')

    def test_predecessor(self):
        b = RedBlackTree.build([3,1,2,5,4])

        actual = b.predecessor(6)
        self.assertIsNone(actual, 'did not find any node with key 6')

        actual = b.predecessor(1)
        self.assertIsNone(actual, '1 is min, so no predecessor')

        actual = b.predecessor(2)
        self.assertEqual(actual[KEY], 1, 'predecessor of 2 is 1')

        actual = b.predecessor(3)
        self.assertEqual(actual[KEY], 2, 'predecessor of 3 is 2')

        actual = b.predecessor(4)
        self.assertEqual(actual[KEY], 3, 'predecessor of 4 is 3')

        actual = b.predecessor(5)
        self.assertEqual(actual[KEY], 4, 'predecessor of 4 is 3')

    def test_successor(self):
        b = RedBlackTree.build([3,1,2,5,4])

        actual = b.successor(6)
        self.assertIsNone(actual, 'did not find any node with key 6')

        actual = b.successor(1)
        self.assertEqual(actual[KEY], 2, 'successor of 1 is 2')

        actual = b.successor(2)
        self.assertEqual(actual[KEY], 3, 'successor of 2 is 3')

        actual = b.successor(3)
        self.assertEqual(actual[KEY], 4, 'successor of 3 is 4')

        actual = b.successor(4)
        self.assertEqual(actual[KEY], 5, 'successor of 4 is 5')

        actual = b.successor(5)
        self.assertIsNone(actual, '5 is max of tree so no successor')

    def test_range_query(self):
        b = RedBlackTree.build([3,1,2,5,4])
        actual = b.range_query(2, 4)
        expected = [2,3,4]
        self.assertEqual(actual, expected, 'should return a range of data')

    def test_select(self):
        b = RedBlackTree.build([3,1,2,5,4])
        self.assertEqual(b.select(1)[KEY], 1, '1st elem is 1')
        self.assertEqual(b.select(2)[KEY], 2, '2nd elem is 2')
        self.assertEqual(b.select(3)[KEY], 3, '3rd elem is 3')
        self.assertEqual(b.select(4)[KEY], 4, '4th elem is 4')
        self.assertEqual(b.select(5)[KEY], 5, '5th elem is 5')

    def test_rank(self):
        b = RedBlackTree.build([3,1,2,5,4])
        self.assertEqual(b.rank(1), 0, '0 keys smaller than 1')
        self.assertEqual(b.rank(2), 1, '1 key smaller than 2')
        self.assertEqual(b.rank(3), 2, '2 keys smaller than 3')
        self.assertEqual(b.rank(4), 3, '3 keys smaller than 4')
        self.assertEqual(b.rank(5), 4, '4 keys smaller than 5')
        self.assertIsNone(b.rank(6), 'key 6 does not exist')
