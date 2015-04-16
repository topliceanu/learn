# -*- coding: utf-8 -*-

import unittest

from src.splay_tree import SplayTree, PARENT, LEFT, RIGHT, KEY


class SplayTreeTest(unittest.TestCase):

    def test_insert_splays_node_to_the_root(self):
        st = SplayTree()
        for i in range(30):
            st.insert(i)
        self.assertEqual(st.root[KEY], 29, 'root is now the last element')

    def test_delete_splays_parents_to_the_root(self):
        st = SplayTree()
        for i in range(30):
            st.insert(i)
        removed_node = st.delete_and_splay(2)
        self.assertEqual(removed_node[KEY], 2, 'returns the removed node')
        self.assertEqual(st.root[KEY], 3, 'root is now the parent of 2')

    def test_search_and_splay_works(self):
        st = SplayTree()
        for i in range(30):
            st.insert(i)
        found = st.search_and_splay(12)
        self.assertEqual(found[KEY], 12, 'found the correct node')
        self.assertEqual(st.root[KEY], 12, 'root is now the parent of 12')

    def test_join_two_trees(self):
        pass
