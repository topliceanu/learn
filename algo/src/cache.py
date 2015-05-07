# -*- coding: utf-8 -*-

import time

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


class LRUCache(Cache):
    """ Implements the Last-Recently-Used cache eviction strategy.

    The implementation uses a doubly linked list to keep the last recently used
    keys last. Whenever a new key is read/written the corresponding node is
    moved to the from of the list. This implementation also uses a hash table
    whereby for each key there corresponds the nodes in the list.

    Attrs:
        data: dict, format {key: {key, value, previous, next}}
        first: dict, first element in a doubly linked list representing priority.
            Format {key, value, previous, next}
        last: dict, last element in a doubly linked list representing priority.
            Format {key, value, previous, next}
    """
    def __init__(self, max_size):
        Cache.__init__(self, max_size)
        self.data = {}
        self.first = None
        self.last = None

    def write(self, key, value):
        """ Writes a piece of data in the cache.

        Args:
            key: str
            value: anything

        Returns:
            tuple, in case a value had to be evicted. Format (key, value).
                key: str
                value: anything
            None, in case no eviction takes place
        """
        evicted = None
        if len(self.data) == self.max_size and key not in self.data:
            evicted = self.evict()

        if self.first == None: # First element in the cache.
            node = {'key': key, 'value': value, 'next': None, 'previous': None}
            self.data[key] = node
            self.first = node
            self.last = node
        elif key not in self.data: # Key not already present.
            node = {'key': key, 'value': value, 'next': self.first, 'previous': None}
            self.first['previous'] = node
            self.first = node
            self.data[key] = node
        else: # Key already present in the cache.
            node = self.data[key]
            if node['previous'] != None: # First node in the list already.
                node['previous']['next'] = node['next']
                if node['next'] == None: # When we have only two elements.
                    self.last = self.first
                node['previous'] = None
                node['next'] = self.first
                self.first['previous'] = node
                self.first = node
            node['value'] = value
        return evicted

    def read(self, key):
        """ Reads a piece of data from the cache.

        Args:
            key: str

        Raises:
            Exception, when a cache miss occurs.
        """
        if key not in self.data:
            raise Exception('Cache miss for key {key}'.format(key=key))
        node = self.data[key]

        if node['previous'] != None: # It's not already the first element.
            node['previous']['next'] = node['next']
            if node['next'] == None: # Node was the last one.
                self.last = self.first
            node['previous'] = None
            node['next'] = self.first
            self.first['previous'] = node
            self.first = node

        value = node['value']
        return value

    def evict(self):
        """ Removes the last recently used key from the cache.

        Returns:
            dict, in case a value had to be evicted. Format {key, value}.
                key: str
                value: anything
            None, in case no eviction takes place
        """
        node = self.last
        if node == None: # The cache has no elements.
            return

        if node['previous'] != None: # The cache has more than one element.
            node['previous']['next'] = None
            self.last = node['previous']
        else: # The cache has only one element.
            self.first = None
            self.last = None

        del self.data[node['key']]
        return {'key': node['key'], 'value': node['value']}

    def remove(self, key):
        """ Removes an item from the cache by key. """
        if key not in self.data:
            return

        node = self.data[key]
        del self.data[key]

        if node == self.first:
            self.first = node['next']
            if node['next'] != None:
                node['next']['previous'] = None
        elif node == self.last:
            self.last = node['previous']
            if node['previous'] != None:
                node['previous']['next'] = None
        else:
            node['previous']['next'] = node['next']


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

    TODO This heap should also maintains a list of all the indexes of the nodes.

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
    is removed completely the cache. When overflow occurs on the protected
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
