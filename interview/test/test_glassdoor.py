# -*- coding: utf-8 -*-

import unittest

from glassdoor import *


class TestGlassdoor(unittest.TestCase):

    def test_k_sorted_array(self):
        k = 3
        arr = [3,2,1,6,5,4,9,8,7]

        expected = [1,2,3,4,5,6,7,8,9]
        actual = k_sorted_array(arr, k)
        self.assertEqual(actual, expected, 'should correctly sort the array')

    def test_connected_zeros_in_array(self):
        arr = [
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0],
            [1,1,0,0,0,1,1],
            [0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
        ]
        actual = connected_zeros_in_array(arr)
        self.assertFalse(actual, 'should detect that not all zeroes are reachable')

        arr = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [1,1,1,0,1,1,1],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
        ]
        actual = connected_zeros_in_array(arr)
        self.assertTrue(actual, 'should detect that all zeroes are reachable')

    def test_binary_tree_level_traversal(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        a.add_child(b)
        a.add_child(c)
        b.add_child(d)
        b.add_child(e)
        c.add_child(f)

        expected = {1: {'a'}, 2: {'b', 'c'}, 3: {'d', 'e', 'f'}}
        actual = binary_tree_level_order_traversal(a)
        self.assertEqual(actual, expected, 'should traverse the tree correctly')
