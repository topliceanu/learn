# -*- conding: utf-8 -*-

import time
import unittest

from src.cache import LRUCache, MRUCache, LFUCache, SLRUCache, ARCache


class TestLRUCache(unittest.TestCase):

    def test_write_evicts_the_oldest_elem_when_cache_is_full(self):
        lru = LRUCache(2)
        lru.write('a', 10)
        lru.write('b', 20)
        evicted = lru.write('c', 30)

        self.assertEqual(len(lru.data), 2, 'should have only two elements')
        self.assertEqual(lru.first['key'], 'c', 'c is the most recent')
        self.assertEqual(lru.last['key'], 'b', 'b is the latest addition')

        self.assertEqual(evicted['key'], 'a', 'should have evicted key a')
        self.assertEqual(evicted['value'], 10, 'should have evicted value for a')

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
        self.assertEqual(len(lru.data), 0, 'noop')

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
        evicted = lru.write('c', 30)

        self.assertEqual(lru.read('b'), 20, 'should read the correct data')
        with self.assertRaises(Exception) as notFound:
            lru.read('a')
        self.assertIsNotNone(notFound, 'Cache miss')

        self.assertEqual(evicted['key'], 'a', 'should have evicted key a')
        self.assertEqual(evicted['value'], 10, 'should have evicted value for a')

    def test_lru_remove_correctly_deletes_first_key_from_cache(self):
        lru = LRUCache(3)
        lru.write('a', 10)
        lru.write('b', 20)
        lru.write('c', 20)
        lru.remove('c')

        self.assertIn('a', lru.data, 'a is in the cache')
        self.assertIn('b', lru.data, 'b is in the cache')
        self.assertNotIn('c', lru.data, 'c was removed')

        self.assertEqual(lru.first['key'], 'b', 'b is first pointer')
        self.assertIsNone(lru.first['previous'], 'b is head pointer')
        self.assertEqual(lru.first['next']['key'], 'a', 'a comes after b')

        self.assertEqual(lru.last['key'], 'a', 'a is last pointer')
        self.assertIsNone(lru.last['next'], 'a is the end pointer')
        self.assertEqual(lru.last['previous']['key'], 'b', 'b comes before a')

class TestMRUCache(unittest.TestCase):

    def test_mru_writes_key_to_empty_cache(self):
        mru = MRUCache(2)
        mru.write('a', 1)

        self.assertEqual(mru.deque['key'], 'a', 'head pointer is correct')
        self.assertIn('a', mru.data, 'key a should be stored')

    def test_mru_writes_key_to_a_cache_with_one_value(self):
        mru = MRUCache(2)
        mru.write('a', 1)
        mru.write('b', 2)

        self.assertEqual(mru.deque['key'], 'b', 'b is the new head pointer')
        self.assertEqual(mru.deque['next']['key'], 'a', 'a is after b')
        self.assertEqual(mru.deque['next']['previous']['key'], 'b', 'before a is b')
        self.assertIn('a', mru.data, 'key a should be stored')
        self.assertIn('b', mru.data, 'key b should be stored')

    def test_mru_writes_key_to_a_cache_with_more_than_2_keys(self):
        mru = MRUCache(3)
        mru.write('a', 1)
        mru.write('b', 2)
        mru.write('c', 3)

        self.assertEqual(mru.deque['key'], 'c', 'c is the head pointer')
        self.assertIsNone(mru.deque['previous'], 'c is head so no previous')
        self.assertEqual(mru.deque['next']['key'], 'b', 'b is after c')
        self.assertEqual(mru.deque['next']['previous']['key'], 'c', 'before b is c')
        self.assertEqual(mru.deque['next']['next']['key'], 'a', 'a is after b')
        self.assertEqual(mru.deque['next']['next']['previous']['key'], 'b', 'before a is b')
        self.assertIsNone(mru.deque['next']['next']['next'], 'b is the last one')

        self.assertIn('a', mru.data, 'key a should be stored')
        self.assertIn('b', mru.data, 'key b should be stored')
        self.assertIn('c', mru.data, 'key c should be stored')

    def test_mru_evicts_most_recently_used_key(self):
        mru = MRUCache(2)
        mru.write('a', 1)
        mru.write('b', 2)
        evicted = mru.write('c', 3)

        self.assertEqual(mru.deque['key'], 'c', 'c is the new head')
        self.assertIsNone(mru.deque['previous'], 'c is the front of the head')
        self.assertEqual(mru.deque['next']['key'], 'a', 'a follows c')
        self.assertIsNone(mru.deque['next']['next'], 'a ends the queue')

        self.assertIn('a', mru.data, 'key a should be stored')
        self.assertNotIn('b', mru.data, 'key b should be stored')
        self.assertIn('c', mru.data, 'key c should be stored')

        self.assertEqual(evicted['key'], 'b', 'should have evicted key b')
        self.assertEqual(evicted['value'], 2, 'should have evicted value for b')

    def test_mru_read_promotes_the_read_key_in_front_of_deque(self):
        mru = MRUCache(2)
        mru.write('a', 1)
        mru.write('b', 2)
        mru.read('a')

        self.assertEqual(mru.deque['key'], 'a', 'a is the new head as it was promoted')
        self.assertIsNone(mru.deque['previous'], 'a is the head so no previous')
        self.assertEqual(mru.deque['next']['key'], 'b', 'b is after a, it got demoted')
        self.assertIsNone(mru.deque['next']['next'], 'b ends the queue')

        self.assertIn('a', mru.data, 'key a should be stored')
        self.assertIn('b', mru.data, 'key b should be stored')


class TestLFUCache(unittest.TestCase):

    def test_lfu_write_should_insert_a_new_key(self):
        lfu = LFUCache(2)
        lfu.write('a', 1)

        self.assertIn('a', lfu.data, 'should contain the key a')
        self.assertEqual(lfu.heap.data[0]['_key'], 'a', 'a should be in the heap')
        self.assertEqual(lfu.data['a']['key'], 1, 'after insert the frequency is 1')

    def test_lfu_write_should_update_an_existing(self):
        lfu = LFUCache(2)
        lfu.write('a', 1)
        lfu.write('a', 2)

        self.assertIn('a', lfu.data, 'should contain the key a')
        self.assertEqual(lfu.heap.data[0]['_key'], 'a', 'a should be in the heap')
        self.assertEqual(lfu.data['a']['key'], 2, 'after each write the frequency is bumped by 1')
        self.assertEqual(lfu.data['a']['value'], 2, 'updates are persisted')

    def test_lfu_write_should_evict_a_key_to_make_room(self):
        lfu = LFUCache(2)
        lfu.write('a', 1)
        lfu.read('a')
        lfu.write('b', 2)
        evicted = lfu.write('c', 3)

        self.assertIn('a', lfu.data, 'should contain the key a')
        self.assertNotIn('b', lfu.data, 'should not contain the key b')
        self.assertIn('c', lfu.data, 'should contain the key c')

        self.assertEqual(lfu.data['a']['key'], 2, 'after insert and a read is 2')
        self.assertEqual(lfu.data['c']['key'], 1, 'after insert it is 1')
        self.assertEqual(lfu.heap.data[0]['_key'], 'c', 'c is the least frequently used key')

        self.assertEqual(evicted['key'], 'b', 'should have evicted key b')
        self.assertEqual(evicted['value'], 2, 'should have evicted value for b')

    def test_lfu_read_increments_key_frequency(self):
        lfu = LFUCache(3)
        lfu.write('a', 1)
        lfu.write('b', 2)
        lfu.write('c', 3)

        lfu.read('a')
        lfu.read('a')
        lfu.read('b')

        self.assertEqual(lfu.data['a']['key'], 3, 'after insert and 2 reads')
        self.assertEqual(lfu.data['b']['key'], 2, 'after insert and 1 read')
        self.assertEqual(lfu.data['c']['key'], 1, 'after insert')


class TestSLRUCache(unittest.TestCase):

    def test_slru_read_causes_a_cache_miss_when_key_is_not_present(self):
        slru = SLRUCache(2)
        slru.write('a', 1)

        with self.assertRaises(Exception) as notFound:
            slru.read('b')
        self.assertIsNotNone(notFound, 'Cache miss exception raised')

    def test_slru_read_from_probation_moves_key_to_protected(self):
        slru = SLRUCache(2)
        slru.write('a', 1)
        slru.read('a')

        self.assertEqual(len(slru.probation.data), 0, 'probation is empty')
        self.assertEqual(len(slru.protected.data), 1, 'probation now has one element')

        self.assertIn('a', slru.protected.data, 'a should be in protected')

    def test_slru_read_from_protected(self):
        slru = SLRUCache(2)
        slru.write('a', 1)
        slru.read('a')
        value = slru.read('a')
        self.assertEqual(value, 1, 'should return value from protected cache')

    def test_slru_read_from_probation_might_cause_an_evict_in_protected(self):
        slru = SLRUCache(2, 2)
        slru.write('a', 1)
        slru.read('a')
        slru.write('b', 2)
        slru.read('b')
        slru.write('c', 3)
        slru.write('d', 3)
        slru.read('c')

        self.assertIn('d', slru.probation.data, 'd in probation')
        self.assertIn('a', slru.probation.data, 'a in probation')
        self.assertIn('c', slru.protected.data, 'c in probation')
        self.assertIn('b', slru.protected.data, 'b in probation')

        self.assertEqual(slru.probation.first['key'], 'a', 'a is first in probation')
        self.assertEqual(slru.probation.last['key'], 'd', 'd is last in probation')
        self.assertEqual(slru.protected.first['key'], 'c', 'c is first in protected')
        self.assertEqual(slru.protected.last['key'], 'b', 'b is last in protected')


class TestARCache(unittest.TestCase):

    def test_write_to_empty_cache(self):
        c = ARCache(10)
        c.write('x', 1)

        self.assertEqual(len(c.t1), 1, 'should have one data item in')
        self.assertEqual(len(c.b1), 0, 'should be empty')
        self.assertEqual(len(c.t2), 0, 'should be empty')
        self.assertEqual(len(c.b2), 0, 'should be empty')

    def x_test_write_to_cache_same_value(self):
        c = ARCache(10)
        c.write('x', 1)
        c.write('x', 1)

        self.assertEqual(len(c.t1), 0, 'should be empty')
        self.assertEqual(len(c.b1), 0, 'should be empty')
        self.assertEqual(len(c.t2), 1, 'should have a data item in')
        self.assertEqual(len(c.b2), 0, 'should be empty')
