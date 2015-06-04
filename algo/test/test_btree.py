# -*- coding: utf-8 -*-

import unittest

from src.btree import BTree


class BtreeTest(unittest.TestCase):

    def test_build_should_construct_a_new_btree(self):

        tree = BTree.build(3, [(2, 'a'), (-1, 'c'), (3, 'b'), (0, 'z')])
