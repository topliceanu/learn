# -*- coding: utf-8 -*-

from math import floor, ceil

def merge (left, right):
    """ Joins two sorted lists.

        Positional arguments:
        left -- a sorted list of elements
        right -- a sorted list of elements

        Return:
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
        for l in range(j, m):
            out.append(right[l])
    elif j is m:
        for l in range(i, n):
            out.append(left[l])

    return out


def merge_sort (arr):
    """ Sorts out an array.
        Does modify the input array.

        Params:
        arr - a list of items.

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
