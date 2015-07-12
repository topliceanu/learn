# -*- coding: utf-8 -*-
import heapq
import math
import string
import sys
import random

sys.path.insert(0, '/vagrant/algo')
from src.union_find import UnionFind


# Source of the problems:
# http://www.careercup.com/page?pid=palantir-technology-interview-questions

class Container(object):
    """ Container class needed for the find_pairs_in_list() method.
    """

    def __init__(self):
        self.data = {}

    def inc(self, key):
        if key not in self.data:
            self.data[key] = 1
        else:
            self.data[key] += 1

    def dec(self, key):
        if key not in self.data:
            return
        self.data[key] -= 1
        if self.data[key] <= 0:
            del self.data[key]

    def count(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return -1

def find_pairs_in_list(arr, k, l):
    """ Given an array of values, design and code an algorithm that returns
    whether there are two duplicates within k indices of each other?
    and within plus or minus l (value) of each other?
    Do all, even the latter, in O(n) running time and O(k) space.

    Reference: www.careercup.com/question?id=18517665

    Args:
        arr: list of ints, values to find pairs in.
        k: int, the distance between two pairs.
        l: int, the difference between two close items.

    Return:
        bool, whether such a pair exists.
    """
    i = 0
    j = 0
    n = len(arr)
    container = Container()
    container.inc(arr[i])

    while j < n and i <= j:

        values = set()
        for m in range(l+1):
            values.add(arr[i] + m)
            values.add(arr[i] - m)

        for value in values:
            if (container.count(value) > 0 and value != arr[i]) or \
               (container.count(arr[i]) > 1):
                return True

        if j < n:
            j += 1
            container.inc(arr[j])
        if j - i > k or j == n-1:
            container.dec(arr[i])
            i += 1

    return False


def get_smaller_neighbour(plots, i, j):
    """ Finds a neighbouring plot with elevation strictly smaller than (i, j)."""
    n = len(plots)
    neighbours = []
    if i > 0:
        neighbours.append((i-1, j))
    if i < n-1:
        neighbours.append((i+1, j))
    if j > 0:
        neighbours.append((i, j-1))
    if j < n-1:
        neighbours.append((i, j+1))

    min_elevation = plots[i][j]
    min_elevation_plot = None
    for m in neighbours:
        if plots[m[0]][m[1]] <= min_elevation:
            min_elevation = plots[m[0]][m[1]]
            min_elevation_plot = m

    return min_elevation_plot

def farm_rainfall(plots):
    """ A group of farmers has some elevation data, and we’re going to help
    them understand how rainfall flows over their farmland.
    We’ll represent the land as a two-dimensional array of altitudes and use
    the following model, based on the idea that water flows downhill:

    If a cell’s four neighboring cells all have higher altitudes, we call this
    cell a sink; water collects in sinks. Otherwise, water will flow to the
    neighboring cell with the lowest altitude. If a cell is not a sink, you may
    assume it has a unique lowest neighbor and that this neighbor will be lower
    than the cell.

    Cells that drain into the same sink – directly or indirectly – are said to
    be part of the same basin.

    Your challenge is to partition the map into basins. In particular, given a
    map of elevations, your code should partition the map into basins and output
    the sizes of the basins, in descending order.

    Assume the elevation maps are square. Input will begin with a line with one
    integer, S, the height (and width) of the map. The next S lines will each
    contain a row of the map, each with S integers – the elevations of the S
    cells in the row. Some farmers have small land plots such as the examples
    below, while some have larger plots. However, in no case will a farmer have
    a plot of land larger than S = 5000.

    Your code should output a space-separated list of the basin sizes, in
    descending order. (Trailing spaces are ignored.)

    While correctness and performance are the most important parts of this
    problem, a human will be reading your solution, so please make an effort
    to submit clean, readable code. In particular, do not write code as if you
    were solving a problem for a competition.

    Complexity: O(n^2) , where n - size of the input array.

    Args:
        plots: list, of lists of elevations

    Returns:
        list, of lists with each position being the name of a pond.
    """
    union_find = UnionFind()
    n = len(plots)

    # Compute sink lots for each lot in the field.
    for i in range(n):
        for j in range(n):
            smaller = get_smaller_neighbour(plots, i, j)
            if smaller != None:
                union_find.union((smaller[0], smaller[1]), (i, j))


    # Compose the output array.
    k = 0
    names = {}
    out = [[None]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            lead = union_find.find((i,j))
            if lead not in names:
                names[lead] = string.ascii_uppercase[k]
                k += 1
            name = names[lead]
            out[i][j] = name

    return out

# TODO
#def farm_rainfall2(plots):
#    """ Second implementation fo the same problem but using recursion. """
#
#    def recurse(plots, left, right, top, bottom):
#        if left == right and top == bottom:
#            union_find.make_set((left, top))
#            return
#
#        top_left = recurse(plots, left, (right+left)/2, top, (top+bottom)/2)
#        top_right = recurse(plots, (right+left)/2, top, (top+bottom)/2)
#        bottom_left = recurse(plots, left, (right+left)/2, (top+bottom)/2, bottom)
#        bottom_right = recurse(plots, (right+left)/2, (top+bottom)/2, bottom)

def sort_letters(word, template):
    """ Sort the letters in one word by the order they occur in another in
    linear time.

    Complexity: O(n)

    Params:
        word: string, word whose letters should be reordered.
        template: string, the order of the letters should be performed.
    """
    # Build a dict with all letters from the word to be reordered.
    letters = dict()
    for c in word:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1

    # Pass through all letters in template and if they are present in word add
    # them to the output.
    output = []
    for letter in template:
        if letter in letters:
            output.append(letter)
            letters[letter] -= 1
            if letters[letter] == 0:
                del letters[letter]

    # Append the rest of the letters left in the word, if any.
    if len(letters) != 0:
        for letter in word:
            if letter in letters:
                output.append(letter)
                letters[letter] -= 1
                if letters[letter] == 0:
                    del letters[letter]

    return ''.join(output)

# Source of problems:
# http://www.careercup.com/page?pid=facebook-interview-questions

def binary_search_rotated(key, arr, left, right):
    """ Search in a sorted rotated array. """
    if left > right:
        return False

    middle = (left + right) / 2

    if arr[left] == key or arr[middle] == key or arr[right] == key:
        return True

    if arr[middle] <= arr[right]:
        # Right side is sorted.
        if arr[middle] < key < arr[right]:
            return binary_search_rotated(key, arr, middle+1, right-1)
        else:
            return binary_search_rotated(key, arr, left+1, middle-1)
    elif arr[left] <= arr[middle]:
        # Left side is sorted.
        if arr[left] < key < arr[middle]:
            return binary_search_rotated(key, arr, left+1, middle-1)
        else:
            return binary_search_rotated(key, arr, middle+1, right-1)

def merge_linked_lists(lists):
    """ Merge K sorted singly linked list

    Args:
        lists: list of object, linked list with node of format: {value, next}
    """
    # Build references of lists.
    refs = {}
    for i in range(len(lists)):
        refs[i] = lists[i]

    # Build the initial heap.
    h = []
    for (list_name, list_ref) in refs.iteritems():
        heapq.heappush(h, (list_ref['value'], list_name))

    start = None
    end = None

    while len(refs) != 0:
        (_, list_name) = heapq.heappop(h)

        # Maintain the references in refs.
        node = refs[list_name]
        refs[list_name] = node['next']
        node['next'] = None

        # Wire the pointers to the result list.
        if start == None:
            start = end = node
        else:
            end['next'] = node
            end = node

        # Add back a new value to the heap from the same list.
        if refs[list_name] == None:
            del refs[list_name]
        else:
            heapq.heappush(h, (refs[list_name]['value'], list_name))

    return start

def paint_houses(n, m, cost):
    """ Paint a list of N houses and M colors, each combination has cost,
    minimize the total cost without color in row.

    Args
        n - number of houses
        m - number of colors
        cost - cost matrix of each combination. Format {color1: {color2: cost}}

    Returns:
        (min_cost, colors), min_cost - the total min cost of the coloring.
                            colors - the order of the coloring.
    """
    def get_cost(i, j):
        if i in cost:
            if j in cost[i]:
                return cost[i][j]
        return 0

    # Recursion:
    # A[i][j] = min value obtained with i houses given the last color is j
    # A[i][j] = min(A[i-1][k] + cost(k, j)), k != j, i=0..n, j=0..m
    #            k

    # Initialize.
    A = [[0] * m for _ in range(n)]
    B = [[None] * m for _ in range(n)]

    # Compute min cost.
    for i in range(1, n):
        for j in range(0, m):
            min_k = float('inf')
            min_partial_cost = float('inf')
            for k in range(0, m):
                if k == j:
                    continue
                partial_cost = A[i-1][k] + get_cost(k, j)
                if partial_cost < min_partial_cost:
                    min_partial_cost = partial_cost
                    min_k = k
            A[i][j] = min_partial_cost
            B[i][j] = min_k

    (min_k, min_cost) = min(enumerate([A[n-1][k] for k in range(0, m)]), key=lambda t: t[1])

    # Compute the color ordering that yields min cost.
    colors = []
    i = n-1 # Count houses.
    while i >= 0:
        colors.append(min_k)
        min_k = B[i][min_k]
        i -= 1
    colors.reverse()

    return (min_cost, colors)

def shuffle(arr):
    """ Given array A of size N, using function Random(returns random number
    between 0 and 1) implement function that will return array of size N with
    randomly shuffled elements of the array A. You should give only algo.

    Algorithm: Fisher-Yeates

    Args:
        arr: list of ints. Note! it shuffles the list in-place.
    """
    for i in range(len(arr)):
        j = int(math.floor(random.random() * len(arr)))
        arr[i], arr[j] = arr[j], arr[i]

def rewire_pointers(linked_list):
    """ Given a singly linked list, swap the list items in pairs (reconnect the
    pointers, not simply swap the values).
    """
    before = None
    node = linked_list
    after = node['next']
    if after != None:
        start = after

    while after != None:
        if before != None:
            before['next'] = after
        node['next'] = after['next']
        after['next'] = node

        previous = node
        node = node['next']
        if node['next']:
            after = node['next']['next']
        else:
            after = None

    return start
