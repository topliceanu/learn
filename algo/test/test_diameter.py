# -*- coding: utf8 -*-

import unittest

from src.ballanced_binary_search_tree import BST
from src.diameter import diameter


class TestDiameter(unittest.TestCase):

    def test_diameter(self):
        """ Given the following binary search tree:
                (3)
               /  \
             (2)  (4)
            /        \
          (1)        (5)
        """
        tree = BST.build([3,2,1,4,5])
        actual = diameter(tree.root)
        expected = 5
        self.assertEqual(actual, expected, 'should return the path with '+
                                           'the max number of vertices')

    def test_unballanced_graph_diameter(self):
        """ Given the following binary search tree:
                (1)
                  \
                  (2)
                     \
                     (3)
                       \
                       (4)
                          \
                          (5)
        """
        tree = BST.build([1,2,3,4,5])
        actual = diameter(tree.root)
        expected = 5
        self.assertEqual(actual, expected, 'should return the path with '+
                                           'the max number of vertices')
