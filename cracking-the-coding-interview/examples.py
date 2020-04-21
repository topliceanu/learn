# -*- coding: utf-8 -*-

def all_permutations(a, b):
    """ Ch 7, page 70. Example: Given a smaller strings and a bigger string b,
    design an algorithm to find all permutations of the shorter string within
    the longer one. Print the location of each permutation.

    TODO not tested yet
    """
    def is_permutation(str1, str2):
        char_count = {}
        for char in str1:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        for char in str2:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        return True

    m = len(a)
    n = len(b)
    indices = []
    i = 0
    j = i + m - 1
    while j < n:
        if is_permutation(b[i:j], a):
            indices.append(i)
        i += 1
        j += 1
    return indices

def common_elements(arr1, arr2):
    """ Question: Given two sorted arrays, find the number of elements in common.
    The arrays are the same length and each has all distinct elements.
    Example:
        A: 13 27 35 40 49 55 59
        B: 17 35 39 40 55 58 60
    Common elements are: 35, 40, 55
    """
    i, j = 0, 0
    output = []
    while i < len(arr1) and j < len(arr2):
        if arr[i] < arr[j]:
            i += 1
        elif arr[i] > arr[j]:
            j += 1
        else:
            output.append(arr[i])
            i += 1
            j += 1
    return output
