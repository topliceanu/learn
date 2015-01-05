# -*- coding: utf-8 -*-

from math import floor, ceil


def sort_and_count_split_inversions (left, right):
    """
        Counts the number of inversions accross left and right.

        An inversion is any pair (i,j), i from left array and j from right
        array, such that i > j.

        Params:
            left: sorted list
            right: sorted list

        Return:
            [{list}, {int}] - sorted array and invertion counter
    """
    n = len(left)
    m = len(right)
    out = []
    i = 0
    j = 0
    count = 0

    while i < n and j < m:
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
            # Count an inversion when an element in the right array
            # is larger the the one in the left array.
            count += n - i
    if i is n:
        while j < m:
            out.append(right[j])
            j += 1
    if j is m:
        while i < n:
            out.append(left[i])
            i += 1
    return [out, count]


def sort_and_count_inversions (arr):
    """
        Divide an conquer routine that recursively splits
        the input array in two halves counting the inversions them summing
        them up.

        Params:
            arr: list of items to count inversions in.

        Return:
            A tuple with (sorted_arr, num_inversions)
    """
    n = len(arr)
    # Base case.
    if n is 1:
        return [arr, 0]
    else:
        # Split the input array in two in the middle.
        left = arr[0:int(floor(n/2))]
        right = arr[int(ceil(n/2)):]

        # Count inversions in each of the smaller arrays.
        [left_sorted, left_count] = sort_and_count_inversions(left)
        [right_sorted, right_count] = sort_and_count_inversions(right)

        # Count inversions only across the arrays.
        [arr_sorted, split_count] = sort_and_count_split_inversions(
                                            left_sorted, right_sorted)

        # Sum up all inversions.
        count = left_count + right_count + split_count

        return [arr_sorted, count]
