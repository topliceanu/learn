# -*- coding: utf-8 -*-

import math
import sys

from src.heap import Heap


class Cache(object):
    """ Base abstract class for all cache eviction strategies."""
    def __init__(self, max_size):
        if max_size <= 1:
            raise Exception('Cache size should be more than 1')
        self.max_size = max_size

    def write(self, key, value):
        """ Writes the data to cache.

        Args:
            key: str
            value: any
        """
        raise Exception('Cache#write method must be implemented')

    def read(self, key):
        """ Reads data from the cache.

        Args:
            key: str
        """
        raise Exception('Cache#read method must be implemented')


class LRUCache(object):
    """ Cleaner implementation of a LRU cache as a data structure.

    How to write this function:
    1. start with the public api: read() and write()
        - write implementations using mock private methods.
    2. the two most important private methods: remove() and prepend()
        - case: empty list, one element list, multiple elements: remove first, remove last, other
    3. add the rest of the methods: promote(), link(), evict(), is_overflow()
    4. make sure to maintaing the data invariants: count, data, first and last.

    Attrs:
        size: int, allowed number of object in the cache.
        count: int, the number of objects currently in the cache.
        first: object, reference for the head of the list
        last: object, reference for the last of the list
        data: dict, hash table to store references to nodes by key.
    """
    def __init__(self, size):
        self.size = size
        self.reset()

    def write(self, key, value):
        """ Writes a new key/value pair to the cache.

        If the key already exists, it will override the value.
        if the cache overflows, it will evict the least recently used item.

        Args:
            key: str
            value: any

        Return:
            Object, in case there is an eviction, the evicted item is returned.
            None, when no eviction occurs.
        """
        if key in self.data:
            item = self.data[key]
            item['value'] = value
            self.promote(item)
        else:
            item = self.make_item(key, value)
            self.prepend(item)

        if self.is_overflow():
            return self.evict()

    def read(self, key):
        """ Reads a data from the cache.

        Throws:
            Exception, when a cache miss occurs.

        Args:
            key: str

        Return:
            any, the value stored under the given key in the cache.
        """
        if key not in self.data:
            raise Exception('Cache miss for key {key}'.format(key=key))

        item = self.data[key]
        self.promote(item)
        return item['value']

    def promote(self, item):
        """ Given an inte object, it promotes the object to the head of the list.
        """
        self.remove_item(item)
        self.prepend(item)

    def remove(self, key):
        """ Removes an element by key from the cache. """
        item = self.data[key]
        self.remove_item(item)

    def remove_item(self, item):
        """ Removes an item object from the cache. """
        if self.count in [0, 1]:
            return self.reset()

        self.count -= 1
        del self.data[item['key']]

        if item == self.first:
            self.first = item['next']
            self.link(item, None)
            self.link(None, self.first)
        elif item == self.last:
            self.last = item['previous']
            self.link(None, item)
            self.link(self.last, None)
        else:
            self.link(item['previous'], item['next'])
            self.link(None, item)
            self.link(item, None)

    def prepend(self, item):
        """ Adds an item to the front of the list. """
        if self.count == 0:
            self.first = self.last = item
        elif self.count == 1:
            self.first = item
            self.link(self.first, self.last)
        else:
            self.link(item, self.first)
            self.first = item

        self.data[item['key']] = item
        self.count += 1

    def link(self, node1, node2):
        """ Links toghether two nodes in the list, making them consecutive. """
        if node1 != None and node2 != None:
            node1['next'] = node2
            node2['previous'] = node1
        elif node1 != None and node2 == None:
            node1['next'] = None
        elif node1 == None and node2 != None:
            node2['previous'] = None

    def evict(self):
        """ Removes the least recently used element, ie. tail of the list. """
        to_remove = self.last
        self.remove_item(to_remove)
        return to_remove

    def is_overflow(self):
        """ Returns True if the cache is overflowing. """
        return self.count > self.size

    def make_item(self, key, value):
        """ Override this to provide your own object format. """
        return {'key': key, 'value': value, 'previous': None, 'next': None}

    def reset(self):
        """ Brings the cache to an empty state. """
        self.count = 0
        self.first = None
        self.last = None
        self.data = {}


class MRUCache(Cache):
    """ Most Recently Used cache implementation.

    This cache evicts the most recent item requested when the storage is full.
    This cache has a tendency to retain older data and as such it is usefull
    for random access patterns and repeated scans over large data sets.

    Args:
        data: dict, format {key: {key, value, next, previous}}
        deque: object, format {key, value, next, previous}
    """
    def __init__(self, max_size):
        Cache.__init__(self, max_size)
        self.data = {}
        self.deque = None

    def write(self, key, value):
        """ Writes the given (key, value) pair to the cache storage. """
        evicted = None
        if key not in self.data and len(self.data) == self.max_size:
            evicted = self.evict()

        if self.deque == None:
            node = {'previous': None, 'next': None, 'key': key, 'value': value}
            self.deque = node
            self.data[key] = node
        elif key in self.data:
            self.promote(key)
            self.deque['value'] = value
        else:
            node = {'previous': None, 'next': self.deque, 'key': key, 'value': value}
            self.deque['previous'] = node
            self.deque = node
            self.data[key] = node
        return evicted

    def read(self, key):
        """ Reads from the cache the value with the specified key.

        Raises:
            Exception, when a cache miss occurs.
        """
        if key not in self.data:
            raise Exception('Cache miss for key {key}'.format(key=key))

        self.promote(key)
        return self.deque['value']

    def promote(self, key):
        """ Brings the specified key into the head pointer of the deque. """
        node = self.data[key]
        if node['previous'] == None:
            return
        node['previous']['next'] = node['next']
        node['previous'] = None
        node['next'] = self.deque
        self.deque['previous'] = node
        self.deque = node

    def evict(self):
        """ Removes the head pointer when cache is full.

        Returns:
            dict, in case a value had to be evicted. Format {key, value}.
                key: str
                value: anything
            None, in case no eviction takes place
        """
        node = self.deque
        if node['next'] != None:
            node['next']['previous'] = None
        self.deque = node['next']

        del self.data[node['key']]
        return {'key': node['key'], 'value': node['value']}


class LFUHeap(Heap):
    """ Extends the base Heap class to allow the heap to hold references to
    the stored hash table int the queue and maintain the object with min
    frequency as the root.

    TODO This heap should also maintain a list of all the indexes of the nodes.

    Attrs:
        data: list, with format [{key, value, freq}]
            key: str, the key for the index.
            value: any, value to be stored in the cache.
            freq: int, increments whenever the value is read/written.
    """
    def compare(self, left, right):
        """ Compares two elements in the heap by their frequency property. """
        return cmp(left['freq'], right['freq'])

    def on_bubble(self, item, old_index, new_index):
        """ Maintains the index of each element in the array. """
        item['index'] = new_index


class LFUCache(Cache):
    """ Least Frequently Used cache implementation.

    To implement fast least frequently used key retrieval this class uses a heap.

    Args:
        data: dict, data structure containing the items.
        heap: object, instance of LFUHeap
    """
    def __init__(self, max_size):
        Cache.__init__(self, max_size)
        self.data = {}
        self.heap = LFUHeap()

    def write(self, key, value):
        """ Writes the data to the cache.

        When writing, the frequency of the key is also incremented.

        Complexity:

        Args:
            key, the key to write the data under.
            value, the value to store.
        """
        evicted = None
        if len(self.data) == self.max_size and key not in self.data:
            evicted = self.evict()

        if key not in self.data:
            node = {'key': key, 'value': value, 'freq': 0}
            self.data[key] = node
            self.heap.insert(node)
        else:
            self.data[key]['value'] = value
        self.increment_frequency(key)
        return evicted

    def read(self, key):
        """ Reads the value for the given key from the cache.

        The key gets its frequency incremented whenever it is read.

        Raises:
            Exception, when a cache miss occurs.
        """
        if key not in self.data:
            raise Exception('Cache miss for key={key}'.format(key=key))

        # TODO implement using a ballanced binary tree in order to make lookups faster!
        # Or you might use a heap with an key/value storage.
        self.increment_frequency(key)
        return self.data[key]

    def increment_frequency(self, key):
        """ Increments the frequency of the given key.

        Method also normalizes frequencies whenever the values reach the top
        limit for integers in python.

        Complexity: O(n) because of the index lookup.

        Args:
            key: the key for which to increase frequency.
        """
        node = self.data[key]
        index = self.heap.data.index(node)

        if node['freq'] == sys.maxint:
            for (__, item) in self.data.iteritems():
                item['freq'] = int(round(float(item['freq']) / 2))

        node['freq'] += 1
        self.heap.remove(index)
        self.heap.insert(node)

    def evict(self):
        """ Evicts the element with the least usage frequency.

        Complexity: O(log n) because of the heap.

        Returns:
            dict, in case a value had to be evicted. Format {key, value}.
                key: str
                value: anything
            None, in case no eviction takes place
        """
        node = self.heap.extract_min()
        del self.data[node['key']]
        return {'key': node['key'], 'value': node['value']}


class SLRUCache(Cache):
    """ Segmented LRU cache implementation.

    The cache data is split into two segments: probation and protected.
    Both the probation and protected segments are LRU caches.
    When writing, the data is stored in the probation section of the cache.
    When reading a key, it is moved in the most recently used section of the
    protected segment, even if the key was located in the probation segment.
    When overflow occurs on the probation segment, the least recently used key
    is removed completely from the cache. When overflow occurs on the protected
    segment, the least recently used key is moved to the probation segment.

    Attrs:
        max_size
        max_size_probation
        probation
        protected
    """

    def __init__(self, max_size, max_size_probation=None):
        Cache.__init__(self, max_size)
        if max_size_probation == None:
            max_size_probation = self.max_size * 4
        self.max_size_probation = max_size_probation

        self.probation = LRUCache(self.max_size_probation)
        self.protected = LRUCache(self.max_size)

    def write(self, key, value):
        """ Returns the evicted value. """
        return self.probation.write(key, value)

    def read(self, key):
        """ Read a key first from the protected then the probation segments.

        Raises:
            Exception, when a cache miss occurs.
        """
        try:
            protected_value = self.protected.read(key)
        except Exception, e:
            protected_value = None

        try:
            probation_value = self.probation.read(key)
        except Exception, e:
            probation_value = None

        if protected_value == None and probation_value == None:
            raise Exception('Cache miss for key {key}'.format(key=key))
        elif protected_value != None and probation_value == None:
            return protected_value
        else:
            # Move key from probation to protected.
            self.probation.remove(key)
            evicted = self.protected.write(key, probation_value)
            if evicted != None:
                self.probation.write(evicted['key'], evicted['value'])
            return probation_value


#class ARCache(Cache):
#    """ Adaptive Replacement cache implementation.
#
#    See: http://en.wikipedia.org/wiki/Adaptive_replacement_cache
#    See: https://www.ipvs.uni-stuttgart.de/export/sites/default/ipvs/abteilungen/as/lehre/lehrveranstaltungen/vorlesungen/WS1415/material/ARC.pdf
#
#    The idea is to optimize between a LRU and a LFU depending on the
#    distribution of input data. Ie. when clients require frequent access to the
#    same data, the LFU cache is favored because it is more efficient (in terms
#    of higher cache hit rates), otherwise LRU is prefered bacause it offers
#    optimal performance in average case.
#
#    Schema:
#        . . . [   b1  <-[     t1    <-!->      t2   ]->  b2   ] . .
#              [ . . . . [ . . . . . . ! . .^. . . . ] . . . . ]
#                        [   fixed cache size (c)    ]
#
#    Data is split in tow lists: t1 (a LRU cache) and t2 (a LFU cache).
#    Originally t1 and t2 have equal size.
#    Evicted keys from t1 move into b1 (a LRU cache) with the same size.
#    Evicted keys from t2 move to b2 (a LFU cache) with the same size.
#    b1 and b2 are called ghosts of t1 and, respectively, t2 and only contain
#    keys, not the actual data.
#    """
#    def __init__(self, max_size):
#        Cache.__init__(self, max_size)
#
#        l1_max_size = max_size / 2
#        l2_max_size = max_size - t1_max_size
#
#        self.t1 = LRUCache(l1_max_size)
#        self.t2 = LFUCache(l2_max_size)
#        self.b1 = LRUCache(l1_max_size)
#        self.b2 = LFUCache(l2_max_size)
#
#    def write(self, key, value):
#        """ Writes data to the disk. """
#        evicted_from_t1 = self.t1.write(key, value)
#        if evicted_from_t1 != None:
#            {key, value} = evicted_from_t1
#            evicted_from_b1 = self.b1.write(key, value)
#            if evicted_from_b1 != None:
#                {key, value} = evicted_from_b1
#                evicted_from_t2 = self.t2.write(key, value)
#                if evicted_from_t2 != None:
#                    return self.b2.write(key, value)
#
#    def read(self, key):
#        """ Read policy from the ARC. algorithm. """
#        from_t1 = self.read_from(self.t1)
#        from_b1 = self.read_from(self.b1)
#        from_t2 = self.read_from(self.t2)
#        from_b2 = self.read_from(self.b2)
#
#        if from_t1 != None or from_t2 != None:
#            value = from_t1 if from_t1 != None else from_t2
#            if from_t1 != None:
#                extracted = self.t1.remove(key)
#                self.t2.write(key, extracted)
#            return value
#
#        if from_b1 != None:
#            self.shift_cache_size('left')
#            raise Exception('Cache miss for key {key}'.format(key=key))
#
#        if from_b2 != None:
#            self.shift_cache_size('right')
#            raise Exception('Cache miss for key {key}'.format(key=key))
#
#
#
#
#    def shift_cache_size(self, direction):
#        """ Modifies the size of the two caches depending on the direction. """
#
#
#    def read_from(cache, key):
#        """ Helper method to silence the cache miss exception. """
#        try:
#            return cache.read(key)
#        except Exception, e:
#            return None
