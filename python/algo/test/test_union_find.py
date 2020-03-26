# -*- coding: utf8 -*-

import unittest

from src.union_find import UnionFind


class TestUnionFind(unittest.TestCase):

    def test_correctly_maintains_the_data_structure(self):
        uf = UnionFind()

        uf.make_set(1)
        uf.make_set(2)
        uf.make_set(3)
        self.assertEqual(uf.find(1), 1, 'each item in its own set')
        self.assertEqual(uf.find(2), 2, 'each item in its own set')
        self.assertEqual(uf.find(3), 3, 'each item in its own set')

        self.assertEqual(uf.find(4), 4, 'find should also insert if not found')

        uf.union(1,2)
        uf.union(3,4)
        self.assertEqual(uf.find(1), uf.find(2), '1 and 2 in the same set now')
        self.assertEqual(uf.find(3), uf.find(4), '3 and 4 in the same set now')

        uf.union(1, 4)
        self.assertEqual(uf.find(2), uf.find(3), '2 and 3 are now in the '+
                                    'same set because 1 and 4 were joined')

    def test_make_set_existing_key(self):
        uf = UnionFind()

        leader = uf.make_set(1)
        leader = uf.make_set(1)
        self.assertEqual(leader, 1, 'the leader is the same element')

        uf.make_set(2)
        uf.union(1, 2)
        leader = uf.make_set(2)
        self.assertEqual(leader, 1, 'the leader of 2 is still 1')
