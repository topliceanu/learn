import random


class BloomFilter(object):
    """ Models a bloom filter data structure.
    A bloom filter holds an array of bytes and a small set of hash functions.
    """

    def __init__(self, num_bits, num_hash_fn):
        """ Initialize a bloom filter by giving the size of the storage array
        ie. num_bits, and the number of hash functions to generate.
        """
        self.num_bits =  num_bits
        self.num_hash_fn = num_hash_fn

        self.bits = [0] * num_bits

        self.primes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        self.hash_fns = []
        for i in range(num_hash_fn):
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
        for hash_fn in self.hash_fns:
            index = hash_fn(value)
            self.bits[index] = 1

    def lookup(self, value):
        for hash_fn in self.hash_fns:
            index = hash_fn(value)
            if self.bits[index] != 1:
                return False
        return True
