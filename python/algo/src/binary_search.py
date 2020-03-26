# -*- coding: utf-8 -*-


def binary_search(key, arr, left, right):
    """ Locate the key value in the given array. """
    if left > right:
        return False

    middle = (left + right) / 2

    if arr[middle] == key:
        return True


    if key <= arr[middle]:
        return binary_search(key, arr, left, middle-1)
    else:
        return binary_search(key, arr, middle+1, right)
