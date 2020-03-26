# -*- coding: utf-8 -*-


def selection_sort(arr):
    """ Sort the input array by means of selection sort.

    The idea is to consistently find the smallest element in the array and swap
    it in it's place.

    Complexity: O(n^2) in time, O(n) in space (sorting is done in place)

    Args:
        arr: list of keys to sort

    Returns:
        list
    """
    for i in range(len(arr)):
        min_val = float('inf')
        min_pos = None
        for j in range(i, len(arr)):
            if min_val > arr[j]:
                min_val = arr[j]
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
