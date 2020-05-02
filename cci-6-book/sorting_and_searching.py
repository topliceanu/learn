# -*- coding: utf-8 -*-

import heapq

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
