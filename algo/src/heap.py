# -*- coding: utf-8 -*-

import heapq


def heap_sort(arr):
    """ Sorts list arr using a heap. """
    heapq.heapify(arr)
    out = []
    while True:
        try:
            min_value = heapq.heappop(arr)
            out.append(min_value)
        except IndexError as err:
            break
    return out

class Median(object):
    """ Class maintains a list of elements. Whenever a new element is added
    to the list the median value (n/2 order statistic) is recomputed.

    Note! In python's heapq implementation, max heaps are not supported, so
    we emulate them by using a min heap and inserting negated values in it!

    Arguments:
        h_low: list, a heap ordered list contaning the smallest n/2 numbers
        h_high: list, a heap ordered list containing the largest n/2 numbers
    """

    def __init__(self):
        self.h_low = []
        self.h_high = []

    def add(self, new_value):
        """ Add element to the internal list and return new median.

        Args:
            new_value: int

        Returns:
            An int representing the new median after inserting new_value.
        """
        if len(self.h_low) > 0:
            max_low = -self.h_low[0]
        else:
            max_low = float('inf')

        if len(self.h_high) > 0:
            min_high = self.h_high[0]
        else:
            min_high = float('-inf')

        if new_value < max_low:
            heapq.heappush(self.h_low, -new_value)
        else:
            heapq.heappush(self.h_high, new_value)

        # Reballance the two heaps to keep running time low in such a way that
        # when the number of imput elements is odd, h_low has exactly one
        # element more than h_high.
        if len(self.h_low) > len(self.h_high) + 1:
            extra = -heapq.heappop(self.h_low)
            heapq.heappush(self.h_high, extra)

        if len(self.h_high) > len(self.h_low):
            extra = heapq.heappop(self.h_high)
            heapq.heappush(self.h_low, -extra)

        # When the number of elements in the structure is odd, pick the min of
        # h_low, when it's even, also pick the min of h_low by convention.
        median = -self.h_low[0]
        return median

class Heap(object):
    """ Implementation of a min-heap data structure.

    Attributes:
        data: list, contains elements maintaining the heap invariant.
    """

    def __init__(self, data=None):
        """ Initialize an empty heap. """
        if data is None:
            data = []
        self.data = data

    def __len__(self):
        """ Returns the size of the internal array of data. """
        return len(self.data)

    def insert(self, element):
        """ Adds an element to the heap.

        Initially insert the element as the next leaf, the bubble it up if
        necessary: if the parent is larger do a swap then recurse.

        NOTE when inserting a new node there can only be AT MOST one edge that
        is out of order, ie. does not have the heap property.

        Running time: O(log n)

        Args:
            element: any value to add to the heap.
        """
        self.data.append(element)
        self.bubble_up(len(self.data) - 1)

    def extract_min(self):
        """ Removes the head of the array, swaps in the tail (last leaf in
        the tree) then bubbles it down to restore the heap property.

        Complexity: O(log n)

        Returns:
            The min value of the list of values inserted into the heap.
        """
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        root = self.data.pop(-1)
        self.bubble_down(0)
        return root

    def peek_min(self):
        """ Return the min value of the heap without removing it.

        Complexity O(1)

        Returns:
            The min value of the values in the heap.
        """
        return self.data[0]

    def extract_min_and_insert(self, new_value):
        """ Returns the min value of the heap, removes it and add new_value.

        The reason to combine an extract_min and an insert is for performance.
        Both operations take O(log n) separately, combined they ammount also to
        O(log n)

        Args:
            new_value: int, a new value to add to the heap after removing min.

        Returns:
            The min of all the values in the heap.
        """
        min_value = self.data.pop(-1)
        self.data.insert(0, new_value)
        self.bubble_down(0)
        return min_value

    def remove(self, index):
        """ Removes the element found at index in the heap array.

        The last leaf in the heap is swapped in the position index,
        then the element is removed.
        If if violates the heap property towards its parent then bubble up,
        otherwise bubble down.
        If the index is not found in the heap, nothing happens.

        Args:
            index: the key to remove from the heap.

        Returns:
            The element which was removed from the heap at index.
        """
        if index >= len(self.data):
            return
        if index == len(self.data) - 1:
            return self.data.pop(-1)

        self.data[index], self.data[-1] = self.data[-1], self.data[index]
        removed = self.data.pop(-1)
        parent = Heap.parent(index)
        if parent is None:
            # Just removed the root so simply bubble_down the new root.
            self.bubble_down(index)
        elif self.data[parent] > self.data[index]:
            self.bubble_up(index)
        else:
            self.bubble_down(index)
        return removed

    def bubble_up(self, index):
        """ Bubbles a value at position index to maintain the heap property:
        any parent node should be smaller than it's children.

        This will do at most log2 n (ie. the number of layers in the tree)
        swaps to restore the heap property.

        Running time: O(log2 n) the max number of swaps == depth of the tree.
        A.K.A. percolate up.

        Args:
            index: int, the key in the heap to bubble up.
        """
        while True:
            parent = Heap.parent(index)
            if parent is None:
                break # We are at the root.
            if self.compare(self.data[parent], self.data[index]) < 0:
                break # The heap invariant is preserved.
            else:
                (self.data[parent], self.data[index]) = \
                    (self.data[index], self.data[parent])
                index = parent
        return index

    def bubble_down(self, parent):
        """ Bubbles down the element at position <parent> (if it has any children).

        This is done by continuously swapping the parent node with the minimum
        of the two children nodes.

        Running time: O(log2 n) the max number of swaps == depth of the tree.
        A.K.A. percolate down

        Args:
            parent: int, the index in the heap to bubble down.
        """
        while True:
            left = parent * 2 + 1
            right = parent * 2 + 2
            min_index = self.get_min(parent, left, right)
            if min_index == parent:
                break # The heap invariant is preserved.

            (self.data[parent], self.data[min_index]) = \
                (self.data[min_index], self.data[parent])
            parent = min_index
        return parent

    def get_min(self, parent, left, right):
        """ Returns the index corresponging to the minimum values in a list.

        Assumes at least the parent index exists in the contained data, but
        the left and right children may not exist, so this method takes care
        of that.

        Args:
            parent: int
            left: int
            right: int

        Returns:
            An int representing the index with the min value.
        """
        min_index = parent
        for index in [left, right]:
            if index < len(self.data) and \
               self.compare(self.data[min_index], self.data[index]) > 0:
                    min_index = index
        return min_index

    def compare(self, left, right):
        """ Defines a comparison function between two elements from the heap.

        By default uses the standard cmp function, but subclasses can extend
        this functionality.

        Args:
            left: mixed
            right: mixed

        Return:
            -1: if left < right
            0: if left == right
            1: if left > right
        """
        return cmp(left, right)

    @classmethod
    def heapify(cls, data):
        """ Initializes a heap from a list of numbers.

        Traverse the array from end to front and bubble keys down as needed.
        Running time: O(n)

        NOTE! This is a class method to allow for inheritance in subclasses.
        See: http://stackoverflow.com/a/9755805 for an explanation on why the
        running time is O(n) and not O(nlogn). Basically, it's much better to
        run bubble-down starting from the root, the to do bubble-up starting
        from the leaves.


        Args:
            data: list, array of elements to organize into a heap.
        """
        h = cls(data)
        for i in xrange(len(h.data)-1, -1, -1):
            h.bubble_down(i)
        return h

    @staticmethod
    def parent(index):
        """ Computes the parent index of the given index.

        Args:
            index: int, a position in the list storing the heap.

        Returns:
            An int with the index of the parent element
            None if the given index is 0 (ie. the root of the heap)
        """
        if index == 0:
            return None
        if index % 2 == 0:
            return index/2 - 1
        else:
            return int(index/2)

    @staticmethod
    def is_heap(data):
        """ Checks if a list of numbers has the min heap property, ie. parent
        key is smaller than child keys

        Complexity: O(n)

        Args:
            data: list, array of elements to check if a heap.

        Returns:
            bool
        """
        for i in xrange(1, len(data)):
            parent = Heap.parent(i)
            if parent is None:
                continue
            elif data[i] < data[parent]:
                return False
        return True
