# -*- coding: utf-8 -*-


import sys

sys.path.insert(0, '../algo')
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

# 5 Facebook internship problems:
# http://www.geeksforgeeks.org/facebook-interview-set-2-campus-interview-internship/

def max_fruit_gathered_by_birds(fruits, m):
    """" There are n trees in a circle. Each tree has a fruit value associated
    with it. A bird can sit on a tree for 0.5 sec and then he has to move to a
    neighbouring tree. It takes the bird 0.5 seconds to move from one tree to
    another. The bird gets the fruit value when she sits on a tree. We are
    given n and m (the number of seconds the bird has), and the fruit values
    of the trees. We have to maximise the total fruit value that the bird can
    gather. The bird can start from any tree.

    Observations:
    - it takes 1 second to travel to a tree and eat the fruit. So I can only
    visit at most <time> trees.
    - it's enough to visit trees in one direction, because we compute gain
    starting from each tree.
    - becomes a problem of finding the sliding window of fixed size with max
    value in an array of integers.

    Args:
        fruits: list, of ints, representing the fruit quantity for each tree.
        m: int, the number of seconds allowed to pick up all fruit.

    Complexity: O(n), n - number of trees
    """
    n = len(fruits)
    if m >= n:
        return fruits

    if len(fruits) == 0 or m == 0:
        return 0

    fruits.extend(fruits[:2])

    s = sum(fruits[:m])
    max_s = s
    max_int = [0,m-1]
    for r in range(m, len(fruits)):
        l = r - m + 1
        s += fruits[r]
        s -= fruits[l-1]
        if s > max_s:
            max_s = s
            max_int = [l, r]

    return fruits[max_int[0] : max_int[1]+1]

def base_convert_range(n, base):
    """ You are given the encoding for a base 58 number. You have to convert
    all the numbers from 1 to n to a base 58 number using the encoding given.

    Args:
        n: int, range of numbers to convert.
        base: int, the base for convertion.

    Returns:
        list, of converted numbers
    """
    def inc(arr, base):
        """ Increments a number represented in the given base.

        Args:
            arr: list, of ints, represents the number in reverse order.
            base: int, the numeric base representation of arr

        Returns:
            list, of ints
        """
        arr[0] += 1
        if arr[0] >= base:
            tmp = inc(arr[1:])
            tmp.insert(0, arr[0] % base)
            arr = tmp
        return arr


    first = [1]
    out = [first]
    for i in range(1, n):
        out.append(inc(out[i-1]))

    return out

def is_interval_overlap(intervals):
    """ You are given the start time and finish time of n intervals. You have
    to write a a function that returns boolean value indicating if there was
    any overlapping interval in the set of existing intervals.

    Complexity: O(nlogn)
    """
    sorted_intervals = sorted(intervals, key=lambda i: i[0]) # sort by position.

    points = []
    for i in sorted_intervals:
        l = {'pos': i[0], 'start': True}
        r = {'pos': i[1], 'start': False}
        points.extend([l, r])

    sorted_points = sorted(points, key=lambda i: i['pos']) # sort by position.

    count_openings = 0
    for p in sorted_points:
        if p['start'] == True:
            count_openings += 1
        else:
            count_openings -= 1
        if count_openings > 1:
            return True

    return False

# Needed for the following problem.
class IntervalTree(object):
    """ Interval tree where there are no overlapping intervals and each
    interval has a value associated.
    """
    def __init__(self):
        self.root = None # format: {start, end, left, right, parent}

    def insert(self, interval, value):
        """ Insert the corresponding interval and value in the tree.

        TODO this requires a self-ballance routine!
        """
        [start, end] = interval

        if self.root == None:
            self.root = {'start': start, 'end': end, 'left': None,
                         'right': None, 'parent': None, 'value': value}
            return

        node = self.root
        while True:
            if node['start'] >= end:
                direction = 'left'
            elif node['end'] <= start:
                direction = 'right'

            if node[direction] == None:
                node[direction] = {'start': start, 'end': end, 'left': None,
                                   'right': None, 'parent': node, 'value': value}
                return
            node = node[direction]

    def lookup(self, point):
        """ Lookup the value corresponding to the given point in the interval tree.
        Note! The point can not "not exists" in any interval!
        """
        node = self.root

        while node != None:
            start = node['start']
            end = node['end']
            if start <= point <= end:
                return node['value']
            elif point < start:
                node = node['left']
            elif point > end:
                node = node['right']

def dot_product(vector1, vector2):
    """ Represent the dot intersection between two vectors.
    You have 2 sparse vectors (large number of 0’s). First tell me a way to
    represent and store them, and then find the dot product.

    Vector Compression (Run Length Encoding):
    [0,0,0,0,0,0,1,1,0,0] -> [0,6,1,2,0,2]
    [0,1,0,1,0,1,0,1,0,1] -> [0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1]

    To multiply use an interval tree, whereby each interval has a value
    assigned, either 1 or 0.

    Complexity: O(nlogk) , n - number of bits each vector
                           k - max number of intervals of continuous bits with the same value.
    """
    def length(vector):
        return sum([vector[i] for i in range(1,len(vector),2)])

    def build_interval_tree(vector):
        """ Builds up the interval tree. """
        int_tree = IntervalTree()
        start = 0
        for i in range(0, len(vector), 2):
            value = vector[i]
            end = start + vector[i+1] -1
            int_tree.insert([start, end], value)
            start = end + 1
        return int_tree

    n = length(vector2)
    m = length(vector1)

    if m != n:
        raise Exception('Vectors must have the same length for dot product to work')

    int_tree_1 = build_interval_tree(vector1)
    int_tree_2 = build_interval_tree(vector2)

    dot_product = 0
    for i in range(n):
        dot_product += int_tree_1.lookup(i) * int_tree_2.lookup(i)
    return dot_product
