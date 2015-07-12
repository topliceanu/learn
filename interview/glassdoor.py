import sys
sys.path.insert(0, '/vagrant/algo')

from src.heap import Heap
from src.flood_fill import scanline_fill


# 1. Implement a spell-checker.


# 2. sort a k-sorted array: sort an array which is already partially sorted,
# ie. each element is at most k positions away from it's sorted position.

def k_sorted_array(arr, k):
    """ Method sorts a k-sorted array.

    A k-sorted array is an array where each element is at most k positions away
    of it's final sorted position.

    This solution piggybacks on the heapsort algorithm

    Complexity: O(nlogk) in time

    Args:
        arr: list, of values to sort.
        k: int, the max distance any element can be from it's final sorted position.

    Returns:
        list, sorted array
    """
    n = len(arr)
    if n < k:
        k = n

    heap = Heap.heapify(arr[:k])

    out = []
    for i in range(k, n):
        min_value = heap.extract_min_and_insert(arr[i])
        out.append(min_value)

    for i in range(k):
        min_value = heap.extract_min()
        out.append(min_value)

    return out

def connected_zeros_in_array(arr):
    """ Given a matrix of 1s and 0s, find if all the 0s are connected.

    See: http://www.glassdoor.com/Interview/Given-a-matrix-of-1s-and-0s-find-if-all-the-0s-are-connected-ie-can-you-flood-fill-the-area-QTN_967859.htm

    Returns:
        bool, True if all zeroes are connected
    """
    n = len(arr)

    # find a starting point
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                break
            else:
                continue
            break
    start_point = (i, j)

    # Flood-fill all reachable zeroes with values of one.
    scanline_fill(arr, start_point, 0, 1)

    # For each line, the sum of values should be n.
    for i in range(n):
        if sum(arr[i]) != n:
            return False
    return True

# Facebook Interviews

class Node(object):
    """ A node in a tree. """

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

def binary_tree_level_order_traversal(tree):
    """ Binary Tree level order traversal, a.k.a. breadth-first search. """
    def traverse(node, level, out):
        if node == None:
            return

        if level not in out:
            out[level] = set([])
        out[level].add(node.key)

        for child in node.children:
            traverse(child, level+1, out)

    output = {}
    traverse(tree, 1, output)
    return output
