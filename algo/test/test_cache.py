# -*- conding: utf-8 -*-

import time
import unittest

from src.cache import LRUCache


class TestCache(unittest.TestCase):

    def test_write_evicts_the_oldest_elem_when_cache_is_full(self):
        lru = LRUCache(2)
        lru.write('a', 10)
        lru.write('b', 20)
        lru.write('c', 30)

        self.assertEqual(len(lru.data), 2, 'should have only one element')
        self.assertEqual(lru.first['key'], 'c', 'c is the most recent')
        self.assertEqual(lru.last['key'], 'b', 'b is the latest addition')

    def test_write_adds_only_element_to_cache(self):
        lru = LRUCache(2)
        lru.write('a', 10)
        self.assertEqual(lru.first['key'], 'a', 'a is the first')
        self.assertEqual(lru.last['key'], 'a', 'a is the last')

    def test_write_moves_key_to_the_first_position(self):
        lru = LRUCache(2)
        lru.write('a', 10)
        lru.write('b', 20)
        lru.write('a', 30)

        self.assertEqual(lru.first['key'], 'a', 'a is the first')
        self.assertEqual(lru.last['key'], 'b', 'b is the last')
        self.assertEqual(lru.first['next']['key'], 'b', 'b is successor to a')
        self.assertEqual(lru.data['a']['value'], 30, 'should have updated val')

    def test_write_inserts_new_key_in_front_of_cache(self):
        lru = LRUCache(3)
        lru.write('a', 10)
        lru.write('b', 20)
        lru.write('c', 30)

        self.assertEqual(lru.first['key'], 'c', 'c is the first')
        self.assertIsNone(lru.first['previous'], 'a has no predecessor')
        self.assertEqual(lru.first['next']['key'], 'b', 'a successor is b')
        self.assertEqual(lru.data['b']['previous']['key'], 'c', 'c before b')
        self.assertEqual(lru.data['b']['next']['key'], 'a', 'a after b')
        self.assertEqual(lru.last['key'], 'a', 'a is the last')
        self.assertEqual(lru.last['previous']['key'], 'b', 'b before last')
        self.assertIsNone(lru.data['a']['next'], 'a is the last')

    def test_read_throws_when_cache_miss(self):
        lru = LRUCache(2)
        with self.assertRaises(Exception) as notFound:
            lru.read('a')
        self.assertIsNotNone(notFound, 'Cache miss exception raised')

    def test_read_returns_correct_value(self):
        lru = LRUCache(2)
        lru.write('a', 10)
        lru.write('b', 20)
        expected = 20
        actual = lru.read('b')
        self.assertEqual(actual, expected, 'should return the correct value')

    def test_read_must_rewire_the_first_pointer(self):
        lru = LRUCache(2)
        lru.write('a', 10)
        lru.write('b', 20)

        lru.read('a')
        self.assertEqual(lru.first['key'], 'a', 'a should now be the first')
        self.assertIsNone(lru.first['previous'],
            'first should not have anything before')
        self.assertEqual(lru.first['next']['key'], 'b',
            'b is not least recently used')
        self.assertEqual(lru.last['key'], 'b', 'a should now be the first')
        self.assertIsNone(lru.last['next'],
            'last should not have anything after it')
        self.assertEqual(lru.last['previous']['key'], 'a',
            'a is before last')

    def test_evict_when_cache_has_no_elements(self):
        lru = LRUCache(2)
        lru.evict()

    def test_evict_when_cache_has_one_element(self):
        lru = LRUCache(2)
        lru.write('a', 10)
        lru.evict()
        self.assertNotIn('a', lru.data, 'cache should be empty')
        self.assertIsNone(lru.first, 'double linked list is empty')
        self.assertIsNone(lru.last, 'double linked list is empty')

    def test_evict_when_cache_has_at_least_two_elements(self):
        lru = LRUCache(2)
        lru.write('a', 10)
        lru.write('b', 20)
        lru.evict()

        self.assertNotIn('a', lru.data, 'cache should not contain key a')
        self.assertIn('b', lru.data, 'cache should contain key b')
        self.assertEqual(lru.first['key'], 'b', 'cache should only contain b')
        self.assertEqual(lru.last['key'], 'b', 'cache should only contain b')
        self.assertIsNone(lru.last['previous'], 'no more data in cache')
        self.assertIsNone(lru.last['next'], 'no more data in cache')

    def test_lru_evicts_old_data(self):
        lru = LRUCache(2)
        lru.write('a', 10)
        lru.write('b', 20)
        lru.write('c', 30)

        self.assertEqual(lru.read('b'), 20, 'should read the correct data')
        with self.assertRaises(Exception) as notFound:
            lru.read('a')
        self.assertIsNotNone(notFound, 'Cache miss')
