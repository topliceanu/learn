# -*- coding: utf-8 -*-

def heapify(arr):
    """ Formats an array into a min-heap structure, in place."""
    for i in range(len(arr)):
        bubble_down(arr, i)

def bubble_up(arr, index):
    """ Promotes a value from an index until the min-heap invariant is maintained. """
    parent_index = parent_of(index)
    if parent_index < 0:
        return
    if arr[parent_index] <= arr[index]:
        return
    arr[parent_index], arr[index] = arr[index], arr[parent_index]
    bubble_up(arr, parent_index)

def bubble_down(arr, index):
    """ Bubbles down the value at the given index until the min-heap invariant is maintained. """
    (left_index, right_index) = children_of(index)
    parent, left, right = arr[index], float('inf'), float('inf')
    if left_index < len(arr):
        left = arr[left_index]
    if right_index < len(arr):
        right = arr[right_index]
    min_index = index_of_min(arr, index, left_index, right_index)
    if min_index == index:
        return
    arr[min_index], arr[index] = arr[index], arr[min_index]
    bubble_down(arr, min_index)

def insert(arr, val):
    """ Add a new value to the min-heap index and maintains the invariant. """
    arr.append(val)
    bubble_up(arr, len(arr) - 1)

def extract_index(arr, index):
    """ Removes a value from the min-heap at a given index.
    This generalises the extract_min call which is just extract_index(arr, 0).
    """
    arr[index], arr[len(arr) - 1] = arr[len(arr) - 1], arr[index]
    val = arr.pop()
    bubble_down(arr, index)
    return val

# helpers

def children_of(index):
    return (2 * index + 1, 2 * index + 2)

def parent_of(index):
    return int((index - 1) / 2)

def index_of_min(arr, parent, left, right):
    min_index = parent # we know this is in arr
    for i in [left, right]:
        if i >= len(arr):
            continue
        if arr[min_index] > arr[i]:
            min_index = i
    return min_index
