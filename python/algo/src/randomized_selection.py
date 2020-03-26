 -*- coding: utf-8 -*-

import random

import src.quick_sort as quick_sort


def randomized_selection(arr, n, i):
    """ Select the ith element from arr if arr would be sorted.

    Note! We are not sorting arr, we just want the ith element in the array.
    Note! This method modifies the original array.

    Complexity: O(n)

    Params:
        arr: the input array
        n: the length of the input array
        i: the position of the element that we are looking for

    Returns:
        The element on the given position.
    """
    if n in [0, 1]:
        return arr[0]

    pos = quick_sort.pick_pivot(0, n - 1)
    arr[0], arr[pos] = arr[pos], arr[0]

    pos = quick_sort.partition(arr, 0, len(arr) - 1)

    if pos == i:
        return arr[pos]
    elif pos > i:
        return randomized_selection(arr[0:pos], (pos - 1), i)
    else:
        return randomized_selection(arr[pos+1:], (n - pos - 1), (i - pos - 1))
