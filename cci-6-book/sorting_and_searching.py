# -*- coding: utf-8 -*-

import heapq

def sorted_merge(a, b):
    """ 10.1 Sorted Merge: You are given two sorted arrays, A and B, where A
    has a large enough buffer at the end to hold B. Write a method to merge B
    into A in sorted order.
    """
    if len(a) == 0 and len(b) == 0:
        return []
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    ha, ta = a[0], a[1:]
    hb, tb = b[0], b[1:]
    if ha < hb:
        return [ha] + sorted_merge(ta, b)
    else:
        return [hb] + sorted_merge(a, tb)

def group_anagrams(words):
    """ 10.2 Group Anagrams: Write a method to sort an array of strings so that
    all the anagrams are next to each other.
    """
    words_with_sorted = [(w, str(sorted(list(w)))) for w in words]
    words_sorted_by_anagram = sorted(words_with_sorted, key=lambda p: p[1])
    return [p[0] for p in words_sorted_by_anagram]

def search_rotated(arr, el):
    """ 10.3 Search in Rotated Array: Given a sorted array of n integers that
    has been rotated an unknown number of times, write code to find an element
    in the array. You may assume that the array was originally sorted in
    increasing order.
    EXAMPLE
    Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
    Output: 8 (the index of 5 in the array)
    """
    def search(arr, el, left, right):
        if left > right:
            return None
        if left == right:
            if arr[left] == el:
                return left
            else:
                return None
        middle  = (left + right) / 2
        if arr[left] <= arr[middle]: # inflection is to the right
            if el <= arr[middle]:
                return search(arr, el, left, middle)
            else:
                return search(arr, el, middle+1, right)
        else: # inflection is the left side
            if el >= arr[middle]:
                return search(arr, el, middle, right)
            else:
                return search(arrl, el, left, middle-1)

    return search(arr, el, 0, len(arr) - 1)

def sorted_search_no_size(x, elementAt):
    """ 10.4 Sorted Search, No Size: You are given an array-like data structure
    Listy which lacks a size method. It does, however, have an elementAt(i)
    method that returns the element at index i in 0(1) time. If i is beyond the
    bounds of the data structure, it returns -1. (For this reason, the data
    structure only supports positive integers.) Given a Listy which contains
    sorted, positive integers, find the index at which an element x occurs.
    If x occurs multiple times, you may return any index.
    """
    def rec_search(el, elementAt, left_idx, right_idx):
        left_val = elementAt(left_idx)
        right_val = elementAt(right_idx)
        if left_idx == right_idx:
            if el == left_val:
                return left_idx
            else:
                return None
        if right_val == -1:
            return rec_search(el, elementAt, left_idx, (left_idx + right_idx) / 2)
        if el < right_val:
            return rec_search(el, elementAt, left_idx, (left_idx + right_idx) / 2)
        if right_val < el:
            return rec_search(el, elementAt, right_idx, right_idx * 2)
        if right_val == el:
            return right_idx

    return rec_search(x, elementAt, 0, 100)

def sparse_search(arr, s):
    """ 10.5 Sparse Search: Given a sorted array of strings that is interspersed
    with empty strings, write a method to find the location of a given string.
    EXAMPLE:
    Input: find "ball" in {"at", "", "", "" , "ball", "", "", "car", "" , "" , "dad", ""}
    Output: 4
    """
    def spread(arr, middle, left, right):
        k = 1
        while middle - k >= left and middle + k <= right:
            if arr[middle - k] != "":
                return middle - k
            if arr[middle + k] != "":
                return middle + k
            k += 1
        return middle
    def rec_sparse_search(arr, s, left, right):
        if left > right:
            return None
        middle = (left + right) / 2
        if arr[middle] == "":
            new_middle = spread(arr, middle, left, right)
            if new_middle == middle:
                return None
            middle = new_middle
        if arr[middle] == s:
            return middle
        if arr[middle] < s:
            return rec_sparse_search(arr, s, left, middle - 1)
        return rec_sparse_search(arr, s, middle + 1, right)

    return rec_sparse_search(arr, s, 0, len(arr) - 1)

def sort_big_file(lines):
    """ 10.6 Sort Big File: Imagine you have a 20 GB file with one string per
    line. Explain how you would sort the file.

    Solution: bucket sort, we make a pass through each line and copy it at the
    an of new file  that starts with the first two letters of the line.
    At the end we will have 24*2 file, of more-or-less 0.5GB, which can be sorted in memory.
    Finally, merge the files in alphabetic order on disk.
    """
    buckets = {}
    for line in lines:
        prefix = line[:2]
        if prefix not in buckets:
            buckets[prefix] = []
        buckets[prefix].append(line)

    for key, bucket in buckets.items():
        buckets[key] = sorted(bucket)

    sorted_by_keys = sorted(buckets.items(), key=lambda p: p[0])

    output = []
    for _, bucket in sorted_by_keys:
        output = output + bucket
    return output

## PRACTICE BASE ALGORITHMS

def bubble_sort(arr):
    """ Time complexity O(n^2) Space complexity O(1) """
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[i], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def join_sorted(left, right):
    out = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    if i == len(left):
        out.extend(right[j:])
    if j == len(right):
        out.extend(left[i:])
    return out

def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    middle = int(len(arr) / 2)
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return join_sorted(left, right)

def pick_pivot(left, right):
    return int((right + left) / 2) # better yet, pick a random number.

def partition(arr, left, right):
    """
      *--------*----------*-----------*
    left      mid      frontier      right

    left is the pivot, it has been moved to the beginning of the array.
    frontier marks all the elements we've alreay looked at.
    mid is the new index of the pivot, everything to the left is smaller than
        pivot, everything to the right is larger.
    """
    mid = left + 1
    frontier = left + 1
    while frontier < right:
        if arr[frontier] < arr[left]:
            arr[frontier], arr[mid] = arr[mid], arr[frontier]
            mid += 1
        frontier += 1
    arr[left], arr[mid] = arr[mid], arr[left]
    return mid

def quick_sort_rec(arr, left, right):
    if right <= left + 1:
        return
    pivot = pick_pivot(left, right)
    arr[left], arr[pivot] = arr[pivot], arr[left]
    new_pivot = partition(arr, left, right)
    quick_sort_rec(arr, new_pivot+1, right)

def quick_sort(arr):
    quick_sort_rec(arr, 0, len(arr) - 1)
    return arr

def heap_sort(arr):
    heapq.heapify(arr)
    out = []
    while len(arr) != 0:
        out.append(heapq.heappop(arr))
    return out
