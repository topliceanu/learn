# -*- conding: utf-8 -*-

import random


class BloomFilter(object):
    """ Models a bloom filter data structure.

    A bloom filter holds an array of bytes and a small set of hash functions.

    Attributes:
        num_bits: int, the size of the memory the datastructure uses.
        num_hash_fn: int, how many hash function to use to store data.
        bits: list, the container for the stored data.
        primes: list, a list of primes usefull in generating hash functions.
        hash_fns: list, of hash functions used to store data
    """

    def __init__(self, num_bits, num_hash_fn):
        """ Initialize a bloom filter by giving the size of the storage array.

        Params:
            num_bits: size of the internal array
            num_hash_fn: number of hash functions to generate to store data.
        """
        self.num_bits =  num_bits
        self.num_hash_fn = num_hash_fn

        self.bits = [0] * num_bits

        self.primes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        self.hash_fns = []
        for i in xrange(num_hash_fn):
            prime = random.choice(self.primes)
            self.primes.remove(prime)
            self.hash_fns.append(self.generate_hash_fn(prime))

    def generate_hash_fn(self, prime):
        """ Generates a hash functions based on a prime number. """
        num_bits = self.num_bits

        def hash_fn(value):
            hash_code = abs(hash(value))
            bucket_index = hash_code * prime % num_bits
            return bucket_index

        return hash_fn

    def insert(self, value):
        """ Inserts the value into the filter. """
        for hash_fn in self.hash_fns:
            index = hash_fn(value)
            self.bits[index] = 1

    def lookup(self, value):
        """ Cheks whether value is in the data structure.

        Note that this operation can return false positives.

        Params:
            value: any hashable value.

        Returns:
            A boolean representing whether the value is in the filter or not.
        """
        for hash_fn in self.hash_fns:
            index = hash_fn(value)
            if self.bits[index] != 1:
                return False
        return True
