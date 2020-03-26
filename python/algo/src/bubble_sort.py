# -*- coding: utf-8 -*-


def bubble_sort(arr):
    """ Sorts the input array using the bubble sort method.

    The idea is to raise each value to it's final position through successive
    swaps.

    Complexity: O(n^2) in time, O(n) in space (sorting is done in place)

    Args:
        arr: list of keys to sort

    Return:
        list
    """
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
