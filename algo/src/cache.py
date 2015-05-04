# -*- coding: utf-8 -*-

import time


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
        """
        if len(self.data) == self.max_size and key not in self.data:
            self.evict()

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
        """ Removes the last recently used key from the cache. """
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
