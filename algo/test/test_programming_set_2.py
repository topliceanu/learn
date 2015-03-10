#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

"""
Download the text file here. [./QuickSort.txt]

The file contains all of the integers between 1 and 10,000
(inclusive, with no repeats) in unsorted order.
The integer in the ith row of the file gives you
the ith entry of an input array.

Your task is to compute the total number of comparisons used
to sort the given input file by QuickSort. As you know, the number
of comparisons depends on which elements are chosen as pivots,
so we'll ask you to explore three different pivoting rules.
You should not count comparisons one-by-one. Rather, when there
is a recursive call on a subarray of length m, you should simply
add m−1 to your running total of comparisons. (This is because
the pivot element is compared to each of the other m−1 elements
in the subarray in this recursive call.)

WARNING: The Partition subroutine can be implemented in several
different ways, and different implementations can give you
differing numbers of comparisons. For this problem, you should
implement the Partition subroutine exactly as it is described in
the video lectures (otherwise you might get the wrong answer).

DIRECTIONS FOR THIS PROBLEM:

For the first part of the programming assignment, you should always
use the first element of the array as the pivot element.

HOW TO GIVE US YOUR ANSWER:

Type the numeric answer in the space provided.
So if your answer is 1198233847, then just type 1198233847 in the
space provided without any space / commas / other punctuation marks.
You have 5 attempts to get the correct answer.
(We do not require you to submit your code, so feel free to use
the programming language of your choice, just type the numeric
answer in the following space.)
"""

import os
import unittest


# Counts the number of comparisons globally.
comparison_count = 0

def pick_pivot_first_elem(l, r, arr):
    """ Picks a pivot element at random from the 25-75% input percentile.

    In this case only the first element is returned.

    Params:
    l - left most index to pick as pivot
    r - right most index to pick as pivot

    Return:
    int - a randon number in [l, r]
    """
    return l

def pick_pivot_last_elem(l, r, arr):
    return r

def pick_pivot_median_of_three(l, r, arr):
    if r - l == 1:
        return l

    m = (r - l) / 2
    vals = [arr[l], arr[r], arr[m]]
    max_val = max(vals)
    min_val = min(vals)
    if arr[l] not in [max_val, min_val]:
        return l
    if arr[m] not in [max_val, min_val]:
        return m
    if arr[r] not in [max_val, min_val]:
        return r

def partition(arr, l, r):
    """ Arranges all elements smaller than the pivot to the left and all
    elements larger than the pivot to the right.

    The pivot is in position l. Which means at the end it will put it in the
    correct position.

    Params:
    arr - list of elements in an array.
    l - left most index in the array and position of the pivot.
    r - right most index in the array.

    Return:
    """
    global comparison_count

    pos = l # pos denotes the position of the pivot.
    i = pos + 1
    for j in xrange(pos+1, r+1):
        comparison_count += 1
        if arr[j] < arr[pos]:
            (arr[i], arr[j]) = (arr[j], arr[i])
            i += 1
    # Finally move the pivot from the first position into it's correct order.
    (arr[i-1], arr[pos]) = (arr[pos], arr[i-1])
    return (i - 1)

def quick_sort(arr, l, r, pick_pivot, partition=partition):
    """ Sorts the input array using the 'quick sort' method.

    Params:
    arr - list of elements.
    l - int, left most index of the array
    r - int, right most index of the array
    pick_pivot - function, pick a pivot element from a list.
    partition - function, arranges elemnts around a pivot.

    Returns:
    A list of sorted elements.
    """
    global comparison_count
    comparison_count += 1
    if l > r:
        return
    if (l - r + 1) == 1:
        return
    if (l - r + 1) == 2:
        comparison_count += 1
        if arr[l] > arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
        return

    # Pick a pivot and place it in the first position of the array.
    p = pick_pivot(l, r, arr)
    (arr[l], arr[p]) = (arr[p], arr[l])

    # Partition the array in place and return the final position of the pivot.
    pos = partition(arr, l, r)

    # Recurse on the two positions.
    quick_sort(arr, l, pos-1, pick_pivot)
    quick_sort(arr, pos+1, r, pick_pivot)


class ProblemSet2Test(unittest.TestCase):

    def test_count_comparisons_with_pivot_as_first_elem(self):
        global comparison_count
        comparison_count = 0

        numbers = []
        with open('{base}/test/IntegerArray.txt'.format(base=os.getcwd()), 'r') as f:
            for line in f:
                numbers.append(int(line))

        quick_sort(numbers, 0, len(numbers) -1, pick_pivot=pick_pivot_first_elem)

        self.assertEqual(comparison_count, 2087776,
            'should count the correct number of compares')

    def test_count_comparisons_with_pivot_as_last_elem(self):
        global comparison_count
        comparison_count = 0

        numbers = []
        with open('{base}/test/IntegerArray.txt'.format(base=os.getcwd()), 'r') as f:
            for line in f:
                numbers.append(int(line))

        quick_sort(numbers, 0, len(numbers) -1, pick_pivot=pick_pivot_last_elem)

        self.assertEqual(comparison_count, 2180377,
            'should count the correct number of compares')

    def test_count_comparisons_median_of_three(self):
        global comparison_count
        comparison_count = 0

        numbers = []
        with open('{base}/test/IntegerArray.txt'.format(base=os.getcwd()), 'r') as f:
            for line in f:
                numbers.append(int(line))

        quick_sort(numbers, 0, len(numbers) -1, pick_pivot=pick_pivot_median_of_three)

        self.assertEqual(comparison_count, 2103992,
            'should count the correct number of compares')

    def xtest_pick_pivot_median_of_three(self):
        median_index = pick_pivot_median_of_three(0, 5, [1,2,3,4,5,6])
        self.assertEqual(median_index, 2);

        median_index = pick_pivot_median_of_three(0, 1, [1,2,3,4,5,6])
        self.assertEqual(median_index, 0);
