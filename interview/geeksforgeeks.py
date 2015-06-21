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

    #def local_minima(arr):
    #    """ Returns the indices of local minima in arr.

    #    A local minima is a tower whose value is smaller than that of it's
    #    neighbours. Array edges cannot be minima!

    #    Returns:
    #        list
    #    """
    #    out = []
    #    for i in range(1, len(arr) - 1):
    #        if (arr[i] < arr[i-1] and arr[i] < arr[i+1]) or \
    #           (arr[i] <= arr[i-1] and arr[i] < arr[i+1]):
    #            out.append(i)
    #    return out

    #def local_maxima(arr):
    #    """ Returns the indices of local maxima in arr.

    #    A local minima is an tower whose value is smaller than that of it's
    #    neighbours. Array edges can be maxims

    #    Returns:
    #        list
    #    """
    #    out = []
    #    for i in range(len(arr)):
    #        if i == 0 or i == len(arr) - 1:
    #            if (i == 0 and arr[i] > arr[i+1]) or \
    #               (i == len(arr)-1 and arr[i] > arr[i-1]):
    #                out.append(i)
    #        else:
    #           if (arr[i] > arr[i-1] and arr[i] >= arr[i+1]) or \
    #              (arr[i] >= arr[i-1] and arr[i] > arr[i+1]):
    #                out.append(i)
    #    return out

    #fill = 0
    #clone = heights[:]

    #while True:
    #    # Find local minima and maxima.
    #    minima = local_minima(clone)
    #    maxima = local_maxima(clone)

    #    # If no minima then there are no gaps.
    #    if len(minima) == 0:
    #        break

    #    # Between each two consecutive local maxima there has to be a local
    #    # minima.
    #    for i in range(len(maxima)-1):
    #        start_gap = maxima[i]
    #        end_gap = maxima[i+1]
    #        fill_level = min(clone[start_gap], clone[end_gap])

    #        # Fill up all the gaps between the local maxima.
    #        for j in range(start_gap+1, end_gap):
    #            local_fill = fill_level - clone[j]
    #            fill += local_fill
    #            clone[j] += local_fill

    #return fill
