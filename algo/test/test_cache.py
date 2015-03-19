# -*- conding: utf-8 -*-

import time
import unittest

from src.cache import LRUCache


class TestCache(unittest.TestCase):

    def test_lru_evicts_old_data(self):
        lru = LRUCache(2)
        lru.write('a', 10)

        lru.write('b', 20)
        time.sleep(0.1)

        #import pdb; pdb.set_trace()
        lru.write('c', 30)
        time.sleep(0.1)

        self.assertEqual(lru.read('b'), 20, 'should read the correct data')
        with self.assertRaises(Exception) as notFound:
            lru.read('a')
        self.assertIsNotNone(notFound, 'Cache miss')
