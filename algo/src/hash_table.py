# -*- coding: utf-8 -*-

class ChainingHash(object):
    """ Hash table implementation which resolves collisions by using chaining.

    Attributes:
        num_buckets: int, how large should the internal array be to store data.
        data: list, a storage for hash data.
    """

    def __init__(self, num_buckets):
        """  Constructs hash table given the number of buckets.

        Args:
            num_buckets: should be a prime and it should not be close to a
                power of 2 or 10.
        """
        # Size of the internal storage list.
        self.num_buckets = num_buckets
        # Stores the hash buckets. It's a list of lists.
        self.data = [[] for i in xrange(self.num_buckets)]

    def insert(self, value):
        """ Add value to the hash table.

        Complexity: O(1)

        """
        index = self.hash_function(value)
        self.data[index].append(value)

    def lookup(self, value):
        """ Checks whether value is in the hash table or not.

        Complexity: O(1)

        Returns:
            bool, whether value is in the hash table or not.
        """
        index = self.hash_function(value)
        return value in self.data[index]

    def delete(self, value):
        """ Removes value from the hash.

        Complexity: O(1)

        Returns:
            bool, whether the value was present in the data structure.
        """
        index = self.hash_function(value)
        if value in self.data[index]:
            self.data[index].remove(value)
            return True
        return False

    def export(self):
        """ Exports a plain list with the enclosed elements.

        Complexity: On()
        """
        output = []
        for bucket in self.data:
            output.extend(bucket)
        return output

    def hash_function(self, value):
        """ Hashing function used to compute a key for the given value.
        This is done in two steps:
        `hash code`: key -> really big number
        `compression function`: really big number -> bucket number

        Args:
            value: any value hashable to be added to the hash table.

        Return:
            int, the position in the array where the items is located.
        """
        hash_code = abs(hash(value))
        bucket_index = hash_code % self.num_buckets
        return bucket_index


class OpenAddressingHash(object):
    """ Implements a hash table data structure using open addressing (with
    double hashing) for collision resolution.

    Two solutions for collision resolution using open addressing:
    - liniar probing: if the first position given by the hash function is not
    available, go to the next in line position and so on. Better for deletes.
    - double hashing: use two hash functions, when the position indicated by
    the first hash function is taken, use the second function to compute the
    next position. Better space efficiency.

    Args:
        num_buckets: int, number of buckets for the hash function.
        data: list, the input data.
        max_attempts: int, how many attempts to insert/lookup the data.
    """

    def __init__(self, num_buckets, max_attempts=10):
        self.num_buckets = num_buckets
        self.data = [None for i in xrange(self.num_buckets)]
        self.max_attempts = max_attempts

    def insert(self, value):
        """ Attempt to insert the data into the hash table.

        Uses the first hash function to compute the initial index. If that's
        taken, use the second function to compute offsets to search for empty
        slots.

        Raises:
            Exception, when the number of insert attempts exceeds a configured
            threshold.
        """
        first_index = self.primary_hash_function(value)
        if (self.data[first_index] == None):
            self.data[first_index] = value
            return

        attempt_count = 0
        second_index = first_index
        while (True):
            offset = self.secondary_hash_function(value)
            second_index = (second_index + offset) % self.num_buckets
            if (self.data[second_index] == None):
                self.data[second_index] = value
                return
            attempt_count += 1
            if attempt_count == self.max_attempts:
                raise Exception('Failed to insert the data in {count} attempts' \
                    .format(count=self.max_attempts))

    def lookup(self, value):
        """ Attempt to locate the data in the hash table.

        Returns:
            bool, whether or not the input value is present.
        """
        first_index = self.primary_hash_function(value)
        if (self.data[first_index] != None):
            return True

        attempt_count = 0
        second_index = first_index
        while (True):
            offset = self.secondary_hash_function(value)
            second_index = (second_index + offset) % self.num_buckets
            if (self.data[second_index] != None):
                return True
            attempt_count += 1
            if attempt_count == self.max_attempts:
                return False

    def delete(self, value):
        """ Removes the value from the data structure.

        Returns:
            bool, whether or not the data structure contained the given value.
        """
        first_index = self.primary_hash_function(value)
        if (self.data[first_index] != None):
            self.data[first_index] = None
            return True

        attempt_count = 0
        second_index = first_index
        while (True):
            offset = self.secondary_hash_function(value)
            second_index = (second_index + offset) % self.num_buckets
            if (self.data[second_index] != None):
                return True
            attempt_count += 1
            if attempt_count == self.max_attempts:
                return False

    def export(self):
        """ Exports the contents of the hash table into a list. """
        return [num for num in self.data if num != None]

    def primary_hash_function(self, value):
        """ First hash function for the initial lookup.

        Args:
            value: mixed, can be any hashable python value.

        Returns:
            int, an index in the array data structure.
        """
        hash_code = abs(hash(value))
        bucket_index = hash_code % self.num_buckets
        return bucket_index

    def secondary_hash_function(self, value):
        """ Second hash function used to offset the indexes produced by the
        first hash function.

        Args:
            value: mixed, can be any hashable python value.

        Returns:
            int, an index in the array data structure.
        """
        hash_code = abs(hash(value)+1319497)
        bucket_index = hash_code % self.num_buckets
        return bucket_index


def two_sum_problem_sort(data, total, distinct=False):
    """ Returns the pairs of number in input list which sum to the given total.

    Complexity O(nlogn)

    Args:
        data: list, all the numbers available to compute the sums.
        total: int, the sum to look for.
        distinct: boolean, whether to accept distinct values when computing sums.

    Returns:
        list, of pairs of numbers from data which sum up to total.
    """
    out = []
    data.sort()
    for i in data:
        if i > total:
            continue
        other = total - i
        if (other in data) and ((distinct == True and i != other) or (distinct == False)):
            out.append((i, other))
    return out

def two_sum_problem_hash(data, total, distinct=False):
    """ Returns the pairs of number in input list which sum to the given total.

    Complexity O(n)

    Args:
        data: list, all the numbers available to compute the sums.
        total: int, the sum to look for.
        distinct: boolean, whether to accept distinct values when computing sums.

    Returns:
        list, of pairs of numbers from data which sum up to total.
    """
    h = {} # Using python's native hash table which is much more performant.
    for i in data:
        h[i] = True

    out = []
    for i in data:
        other = total - i
        if (other in h) and ((distinct == True and i != other) or (distinct == False)):
            out.append((i, other))
    return out
