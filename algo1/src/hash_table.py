# -*- coding: utf-8 -*-

class Hash(object):
    """ Solves collisions by using chaining (instead of open addressing). """
    def __init__(self, num_buckets):
        """  Constructs hash table given the number of buckets.
        `num_buckets` should be a prime and it should not be close to a
        power of 2 or 10.
        """
        # Size of the internal storage list.
        self.num_buckets = num_buckets
        # Stores the hash buckets. It's a list of lists.
        self.data = [[] for i in range(self.num_buckets)]

    def insert(self, value):
        """ Add a key, value pair to the hash table. """
        index = self.hash_function(value)
        self.data[index].append(value)

    def lookup(self, value):
        """ Checks whether the value is in the hash table or not. """
        index = self.hash_function(value)
        return value in self.data[index]

    def delete(self, value):
        """ Removes a value from the hash. """
        index = self.hash_function(value)
        if value in self.data[index]:
            self.data[index].remove(value)

    def hash_function(self, value):
        """ Hashing function used to compute a key for the given value.
        This is done in two steps:
        `hash code`: key -> really big number
        `compression function`: really big number -> bucket number
        """
        hash_code = abs(hash(value))
        bucket_index = hash_code % self.num_buckets
        return bucket_index

def ignore_duplicates(data):
    pass

def two_sum_problem_sort(data, total):
    """ Returns the pairs of number in input list which sum to the given total.
    Complexity O(nlogn)
    """
    out = []
    data.sort()
    for i in data:
        if i > total:
            continue
        other = total - i
        if other in data:
            out.append((i, other))
    return out

def two_sum_problem_hash(data, total):
    """ Returns the pairs of number in input list which sum to the given total.
    Complexity O(n)
    """
    h = {}
    for i in data:
        h[i] = True

    out = []
    for i in data:
        other = total - i
        if other in h:
            out.append((i, other))
    return out
