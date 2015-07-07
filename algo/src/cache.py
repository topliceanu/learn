# -*- coding: utf-8 -*-

import math

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
    """ Cleaner implementation of a LRU cache as a data structure. """
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.first = None
        self.last = None
        self.data = {}

    def read(self, key):
        """ Read the last key from the data structure. """
        if key not in self.data:
            raise Exception('Cache miss for key {key}'.format(key=key))

        item = self.data[key] # {value, previous, next}
        self.promote(item)
        return item['value']

    def write(self, key, value):
        """ Write a key to the data structure.

        In case of overflow, this method will evict the last recently used item.
        """
        if key in self.data:
            item = self.data[key]
            item['value'] = value
            self.promote(item)
        else:
            item = self.prepend(key, value)
            self.data[key] = item

        if self.overflow():
            return self.evict()

    def remove(self, key):
        """ Removes a value from the cache by it's key.

        The implementation promotes the found object to the first value then
        removes it.
        """
        if key not in self.data:
            return

        to_remove = self.data[key]
        self.promote(to_remove)

        if self.count == 1:
            self.first = self.last = None
            self.data = {}
        else: # > 1
            self.first = self.first['next']
            self.link(None, self.first)
            del self.data[key]

        self.count -= 1

    def promote(self, item):
        """ Moves the given item to the from of the list.

        This method cannot be called on an empty data structure, so we have at
        least one element.
        """
        if self.count == 1:
            return
        if self.first == item:
            return

        if self.last == item:
            self.link(item['previous'], None)
            self.last = item['previous']
        else:
            self.link(item['previous'], item['next'])

        self.link(None, item)
        self.link(item, self.first)
        self.first = item

    def link(self, node1, node2):
        """ Links references of two nodes so they are consecutive in the list.

        Any of these two nodes can be None.
        """
        if node1 == None and node2 == None:
            return

        if node1 != None and node2 == None:
            node1['next'] = None
            return

        if node1 == None and node2 != None:
            node2['previous'] = None
            return

        node1['next'] = node2
        node2['previous'] = node1

    def prepend(self, key, value):
        """ Inserts a new value to the end of the list.

        Also maintains the count of the elements in the list.
        """
        item = {'key': key, 'value': value, 'previous': None, 'next': None}

        if self.count == 0:
            self.first = self.last = item
        else:
            self.link(item, self.first)
            self.first = item

        self.count += 1
        return item

    def overflow(self):
        """ Returns True if the number of items exceeds the allowed size. """
        return self.count > self.size

    def evict(self):
        """ Removes the last element in the list. """
        to_evict = self.last

        if self.count == 0:
            return

        if self.count == 1:
            self.first = self.last = None
            self.data = {}
        else:
            self.link(self.last['previous'], None)
            self.last = self.last['previous']
            del self.data[to_evict['key']]

        self.count -= 1

        return {"key": to_evict["key"], "value": to_evict["value"]}


class MRUCache(Cache):
    """ Most Recently Used cache implementation.

    This cache evicts the most recent item requested when the storage is full.

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


class LFUCache(Cache):
    """ Least Frequently Used cache implementation.

    To implement fast least frequently used key retrieval this class uses a heap.
    """
    # TODO What happens when the frequency numbers overflow. One solution is to
    # half all frequencies whenever an overflow happens.

    def __init__(self, max_size):
        Cache.__init__(self, max_size)
        self.data = {}
        self.heap = LFUHeap()

    def write(self, key, value):
        """ Writes the data to the cache.

        Note: when writing, the counter for the key is also incremented.
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

        The key gets its frequency increased whenever it is read.

        Raises:
            Exception, when a cache miss occurs.
        """
        if key not in self.data:
            raise Exception('Cache miss for key={key}'.format(key=key))

        self.increment_frequency(key)
        return self.data[key]

    def increment_frequency(self, key):
        """ Increments the frequency of the given key. """
        node = self.data[key]
        index = self.heap.data.index(node)
        node['freq'] += 1
        self.heap.remove(index)
        self.heap.insert(node)

    def evict(self):
        """ Evicts the element with the least usage frequency.

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


class ARCache(Cache):
    """ Adaptive Replacement cache implementation.

    See: http://en.wikipedia.org/wiki/Adaptive_replacement_cache

    Data is split in tow lists: t1 (a LRU cache) and t2 (a LFU cache).
    Originally t1 and t2 have equal size.
    Evicted keys from t1 move into b1 (a LRU cache) with the same size.
    Evicted keys from t2 move to b2 (a LFU cache) with the same size.
    b1 and b2 are called ghosts of t1 and, respectively, t2 and only contain
    keys, not the actual data.

    All new entries enter t1

    Schema:
        . . . [   b1  <-[     t1    <-!->      t2   ]->  b2   ] . .
              [ . . . . [ . . . . . . ! . .^. . . . ] . . . . ]
                        [   fixed cache size (c)    ]
    """
    # TODO finish the implementation.

    def __init__(self, max_size):
        Cache.__init__(self, max_size)

        self.t1 = LRUCache(max_size)
        self.t2 = LFUCache(max_size)
        self.b1 = LRUCache(max_size)
        self.b2 = LFUCache(max_size)

    def read(self, key):
        pass

    def write(self, key, value):
        evicted_from_t1 = self.t1.write(key, value)
        if evicted_from_t1 != None:
            self.b1.write(evicted_from_t1['key'], evicted_from_t1['value'])
