# -*- coding: utf-8 -*-

import unittest

from src.skiplist import SkipList


class SkipListTest(unittest.TestCase):

    def test_insert(self):
        import pdb; pdb.set_trace()
        sl = SkipList(3)
        for i in range(10):
            sl.insert(i)

    def test_lookup(self):
        pass

    def test_delete(self):
        pass
