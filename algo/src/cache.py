# -*- coding: utf-8 -*-

import time


class Cache(object):
    """ Base abstract class for all cache eviction strategies.

    This class' only concern is storing data and not overflowing.

    Attrs:
        data: dict, actual container of the data.
        max_size: int, the number of keys the cache can hold.
        size: int, how many key the cache currently holds.
    """
    def __init__(self, max_size):
        self.data = {}
        self.size = 0
        self.max_size = max_size

    def write(self, key, value):
        """ Writes the data to cache, maintaining the space constraints. """
        if self.size + 1 > self.max_size:
            raise Exception('Cache size overflow')

        self.data[key] = value
        self.size += 1

    def read(self, key):
        """ Reads data from the cache.

        Args:
            key: str

        Raises:
            Exception, when the key is not in the cache.
        """
        if key in self.data:
            return self.data[key]
        else:
            raise Exception('Cache miss for key {key}'.format(key=key))


class LRUCache(Cache):
    """ Implements the Last-Recently-Used cache eviction strategy.

    Attrs:
        ts: dict, a hash of timestamps of recent usage for each key in data.
    """

    def __init__(self, max_size):
        Cache.__init__(self, max_size)
        self.ts = {}

    def write(self, key, value):
        """ Writes a piece of data in the cache.

        First it finds and evincts the oldest key in the cache, then inserts
        the new one in it's place.

        TODO: instead of always going through the entire timestamp dicts to
        find the oldest timestamp, we can use a max-heap.

        Args:
            key: str
            value: anything
        """
        if self.size + 1 > self.max_size: # No more have room in the cache.
            oldest_ts = None
            for k, ts in self.ts.iteritems():
                if oldest_ts == None:
                    oldest_ts = ts
                    last_used_key = k
                if ts < oldest_ts:
                    oldest_ts = ts
                    last_used_key = k

            del self.data[last_used_key]
            del self.ts[last_used_key]
            self.size -= 1

        self.ts[key] = time.time()
        return Cache.write(self, key, value)
