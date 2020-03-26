# -*- coding: utf-8 -*-

from math import floor, ceil


def merge (left, right):
    """ Joins two sorted lists into a third list and returns that list.

    Args:
        left: a sorted list of elements.
        right: a sorted list of elements.

    Returns:
        A list produced by merging the two received lists.
    """
    i = 0
    j = 0
    n = len(left)
    m = len(right)
    out = []

    while i < n and j < m:
        if left[i] < right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1

    if i is n:
        for l in xrange(j, m):
            out.append(right[l])
    elif j is m:
        for l in xrange(i, n):
            out.append(left[l])

    return out

def merge_sort (arr):
    """ Sort the input array.

    This implementations does modify the input array.
    Merge sort is better suited for sorting liked lists than arrays because
    of the low auxiliary storage required.
    Merge sort is better when sorting data from disk because it requires less
    reads (ie. it can batch read data from disk).

    Complexity: O(nlogn)

    Args:
        arr: list, of items.

    Return:
        The sorted version of the input array.
    """
    n = len(arr)
    if n is 1: # Base case.
        return arr
    else:
        left = merge_sort(arr[0:int(floor(n/2))])
        right = merge_sort(arr[int(ceil(n/2)):])
        res = merge(left, right)
        return res
