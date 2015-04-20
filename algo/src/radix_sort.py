# -*- coding: utf-8 -*-


def radix_sort(arr, radix=10):
    """ Sorts an array of integers inplace using radix sort method.

    A type of bucket sort method which sorts keys by their binary representation.
    Algorithms: sequencially select the least significant digit (for radix=10)
    and collect all keys with equal digit in the same bucket. Then move to the
    next digit. The algorithm runs for the number of digits the largest key has.

    Args:
        arr: list of integers. Note! these must be integers withing a well
            defined interval.

    Returns:
        list, the sorted array
    """
    mask = 1
    max_length = False

    while not max_length:
        max_length = True
        buckets = [[] for __ in range(radix)]

        # Place keys in buckets corresponding to the digit mask.
        for key in arr:
            tmp = key/mask
            buckets[tmp % radix].append(key)
            if max_length is True and tmp > 0:
                max_length = False

        # Replace the input array with the contents of the buckets.
        a = 0
        for b in range(radix):
            bucket = buckets[b]
            for i in bucket:
                arr[a] = i
                a += 1

        mask *= radix

    return arr
