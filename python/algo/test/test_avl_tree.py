# -*- coding: utf-8 -*-

import unittest

from src.avl_tree import AVLTree, KEY, LEFT, RIGHT


class TestAVLTree(unittest.TestCase):
    """ Testing the four cases in wikipedia: http://en.wikipedia.org/wiki/File:AVL_Tree_Rebalancing.svg """

    def test_insert_and_reballance_left_right_case(self):
        tree = AVLTree.build([5, 3])
        tree.insert(4)

        self.assertEqual(tree.root[KEY], 4, 'inserted node is now root')
        self.assertEqual(tree.root[LEFT][KEY], 3)
        self.assertEqual(tree.root[RIGHT][KEY], 5)

    def test_insert_and_reballance_left_left_case(self):
        tree = AVLTree.build([5, 4])
        tree.insert(3)

        self.assertEqual(tree.root[KEY], 4, 'parent is now the new root')
        self.assertEqual(tree.root[LEFT][KEY], 3, 'inserted node is now left')
        self.assertEqual(tree.root[RIGHT][KEY], 5, 'old root has rotated to right')

    def test_insert_and_reballance_right_left_case(self):
        tree = AVLTree.build([3, 5])
        tree.insert(4)

        self.assertEqual(tree.root[KEY], 4, 'inserted node is now root')
        self.assertEqual(tree.root[LEFT][KEY], 3, 'old root has rotated to left')
        self.assertEqual(tree.root[RIGHT][KEY], 5, 'old parent is now right')

    def test_insert_and_reballance_right_right_case(self):
        tree = AVLTree.build([3, 4])
        tree.insert(5)

        self.assertEqual(tree.root[KEY], 4, 'parent is now the new root')
        self.assertEqual(tree.root[LEFT][KEY], 3, 'old root has rotated to left')
        self.assertEqual(tree.root[RIGHT][KEY], 5, 'old parent is now right')

    def test_insert_and_reballance_larger_set(self):
        tree = AVLTree.build([9,5,10,0,6,11,-1,1,2])

        """ The resulting tree should be:
                    9
                   /  \
                  1    10
                /  \     \
               0    5     11
              /    /  \
             -1   2    6
        """
        self.assertEqual(tree.root[KEY], 9)
        self.assertEqual(tree.root[LEFT][KEY], 1)
        self.assertEqual(tree.root[LEFT][LEFT][KEY], 0)
        self.assertEqual(tree.root[LEFT][LEFT][LEFT][KEY], -1)
        self.assertEqual(tree.root[LEFT][LEFT][RIGHT], None)
        self.assertEqual(tree.root[LEFT][RIGHT][KEY], 5)
        self.assertEqual(tree.root[LEFT][RIGHT][LEFT][KEY], 2)
        self.assertEqual(tree.root[LEFT][RIGHT][RIGHT][KEY], 6)
        self.assertEqual(tree.root[RIGHT][KEY], 10)
        self.assertEqual(tree.root[RIGHT][LEFT], None)
        self.assertEqual(tree.root[RIGHT][RIGHT][KEY], 11)

    def test_delete_and_reballance_branch(self):
        """ Given the following tree:
                    9
                   /  \
                  1    10
                /  \     \
               0    5     11
              /    /  \
             -1   2    6

        After deleting 10 (node with only one child), we should end up with:
                    1
                   /  \
                  0    9
                /     /  \
              -1     5   11
                    / \
                   2   6
        """
        tree = AVLTree.build([9,5,10,0,6,11,-1,1,2])
        tree.delete_and_reballance(10)

        self.assertEqual(tree.root[KEY], 1)
        self.assertEqual(tree.root[LEFT][KEY], 0)
        self.assertEqual(tree.root[LEFT][LEFT][KEY], -1)
        self.assertEqual(tree.root[LEFT][RIGHT], None)
        self.assertEqual(tree.root[RIGHT][KEY], 9)
        self.assertEqual(tree.root[RIGHT][LEFT][KEY], 5)
        self.assertEqual(tree.root[RIGHT][LEFT][LEFT][KEY], 2)
        self.assertEqual(tree.root[RIGHT][LEFT][RIGHT][KEY], 6)
        self.assertEqual(tree.root[RIGHT][RIGHT][KEY], 11)

    def test_delete_and_reballance_leaf(self):
        """ Given the following tree:
                    9
                   /  \
                  1    10
                /  \     \
               0    5     11
              /    /  \
             -1   2    6
        After deleting 11 (a leaf), we should end up with:
                    1
                   /  \
                  0    9
                /     /  \
              -1     5   10
                    / \
                   2   6
        """
        tree = AVLTree.build([9,5,10,0,6,11,-1,1,2])
        tree.delete_and_reballance(11)

        self.assertEqual(tree.root[KEY], 1)
        self.assertEqual(tree.root[LEFT][KEY], 0)
        self.assertEqual(tree.root[LEFT][LEFT][KEY], -1)
        self.assertEqual(tree.root[LEFT][RIGHT], None)
        self.assertEqual(tree.root[RIGHT][KEY], 9)
        self.assertEqual(tree.root[RIGHT][LEFT][KEY], 5)
        self.assertEqual(tree.root[RIGHT][LEFT][LEFT][KEY], 2)
        self.assertEqual(tree.root[RIGHT][LEFT][RIGHT][KEY], 6)
        self.assertEqual(tree.root[RIGHT][RIGHT][KEY], 10)

    def test_delete_and_reballance_intermediate_node(self):
        """ Given the following tree:
                    9
                   /  \
                  1    10
                /  \     \
               0    5     11
              /    /  \
             -1   2    6

        After deleting node with key 1 (an intermediate node) the result should be:
                    9
                   /  \
                  0    10
                /  \     \
              -1    5     11
                   / \
                  2   6
        """
        tree = AVLTree.build([9,5,10,0,6,11,-1,1,2])
        tree.delete_and_reballance(1)

        self.assertEqual(tree.root[KEY], 9)
        self.assertEqual(tree.root[LEFT][KEY], 0)
        self.assertEqual(tree.root[LEFT][LEFT][KEY], -1)
        self.assertEqual(tree.root[LEFT][RIGHT][KEY], 5)
        self.assertEqual(tree.root[LEFT][RIGHT][LEFT][KEY], 2)
        self.assertEqual(tree.root[LEFT][RIGHT][RIGHT][KEY], 6)
        self.assertEqual(tree.root[RIGHT][KEY], 10)
        self.assertEqual(tree.root[RIGHT][RIGHT][KEY], 11)

    def test_delete_root_then_reballance(self):
        """ Given the following tree:
                    9
                   /  \
                  1    10
                /  \     \
               0    5     11
              /    /  \
             -1   2    6

        After deleting node 9 (the root) the result should be:
                    6
                   /  \
                  1    10
                /  \     \
               0    5     11
              /    /
             -1   2
        """
        tree = AVLTree.build([9,5,10,0,6,11,-1,1,2])
        tree.delete_and_reballance(9)

        self.assertEqual(tree.root[KEY], 6)
        self.assertEqual(tree.root[LEFT][KEY], 1)
        self.assertEqual(tree.root[LEFT][LEFT][KEY], 0)
        self.assertEqual(tree.root[LEFT][LEFT][LEFT][KEY], -1)
        self.assertEqual(tree.root[LEFT][RIGHT][KEY], 5)
        self.assertEqual(tree.root[LEFT][RIGHT][LEFT][KEY], 2)
        self.assertEqual(tree.root[RIGHT][KEY], 10)
        self.assertEqual(tree.root[RIGHT][RIGHT][KEY], 11)
