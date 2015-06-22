# -*- coding: utf-8 -*-


import sys

sys.path.insert(0, '/vagrant/algo')
from src.trie import Trie


# 1. Implement Reverse DNS Lookup Cache
# http://www.geeksforgeeks.org/implement-reverse-dns-look-cache/

class ReverseDNS(object):

    def __init__(self):
        self.storage = Trie()

    def insert(self, ip, url):
        self.storage.insert(ip, url)

    def lookup(self, ip):
        return self.storage.lookup(ip)


# For the next two problems, see http://www.geeksforgeeks.org/flipkart-interview-experience-set-28-for-sde2/
# 2. Towers holding water

def towers_holding_water(heights):
    """ You are given an array whose each element represents the height of the
    tower. The width of every tower is 1. It starts raining. How much water
    is collected between the towers?
    Eg: [1,5,3,7,2] - then answer is 2 units between towers 5 and 7

    Complexity: O(n)
    """

    # left[i] is the largest value left of heights[i]
    left = [float('-inf')]
    max_so_far = heights[0]
    for i in range(1, len(heights)):
        left.append(max_so_far)
        if max_so_far < heights[i]:
            max_so_far = heights[i]

    # right[i] is the largest value right of heights[i]
    right = [float('-inf')]
    max_so_far = heights[len(heights)-1]
    for i in range(len(heights)-1, 0, -1):
        if max_so_far < heights[i]:
            max_so_far = heights[i]
        right.insert(0, max_so_far)

    fill = 0
    for i in range(len(heights)):
        if left[i] > heights[i] and \
           heights[i] < right[i] and \
           left[i] != float('-inf') and \
           right[i] != float('-inf'):
            fill += min(left[i], right[i]) - heights[i]

    return fill

# 3. Largest Group of Intersecting Intervals.

def largest_group_of_intersecting_intervals(intervals):
    """ We have a huge log file for meeting times in an office. Each entry has
    only start and end time. Given this we have to find the time which has the
    most number of meetings.

    Complexity: O(nlogn) - dominated by the initial sorting.

    Args:
        intervals: list of tuples representing intervals, format [(start, end)]

    Returns:
        tuple, representing the intersection of intervals, format (start, end)
    """
    data = []
    names = {}
    for (index, i) in enumerate(intervals):
        ds = {'start': i[0], 'end': i[1], 'name': index}
        data.append((i[0], ds))
        data.append((i[1], ds))
        names[index] = ds

    sorted_data = sorted(data, key=lambda i: i[0]) # sort by start and end.

    max_count_intervals = float('-inf')
    max_intervals = None

    current_intervals = []
    count_intervals = 0

    for i in range(len(sorted_data)):
        item = sorted_data[i]
        is_opening = item[0] == item[1]['start']
        is_closing = item[0] == item[1]['end']

        if is_opening:
            count_intervals += 1
            current_intervals.append(item[1]['name'])
        if is_closing:
            count_intervals -= 1
            current_intervals.remove(item[1]['name'])

        if max_count_intervals < count_intervals:
            max_count_intervals = count_intervals
            max_intervals = current_intervals[:]

    # Process largest group of overlaping intervals to determine intersection.
    start = max([names[name]['start'] for name in max_intervals])
    end = min([names[name]['end'] for name in max_intervals])
    return (start, end)


# 4. Find the nearest smaller numbers on left side in an array
# http://www.geeksforgeeks.org/find-the-nearest-smaller-numbers-on-left-side-in-an-array/

def nearest_smallest_left_element(arr):
    """ Find the nearest smaller numbers on left side in an array

    Given an array of integers, find the nearest smaller number for every
    element such that the smaller element is on left side.

    Example:
        Input:  arr[] = {1, 6, 4, 10, 2, 5}
        Output:         {_, 1, 1,  4, 1, 2}
        First element ('1') has no element on left side. For 6,
        there is only one smaller element on left side '1'.
        For 10, there are three smaller elements on left side (1,
        6 and 4), nearest among the three elements is 4.

    Example:
        Input: arr[] = {1, 3, 0, 2, 5}
        Output:        {_, 1, _, 0, 2}

    Complexity: O(n)
    """
    stack = []
    out = []

    for item in arr:
        if len(stack) == 0:
            out.append(None)
            stack.append(item)
            continue

        while len(stack) > 0 and stack[-1] >= item:
            stack.pop()
        if len(stack) == 0:
            out.append(None)
        else:
            out.append(stack[-1])
        stack.append(item)

    return out
