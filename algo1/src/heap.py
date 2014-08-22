import heapq


def heap_sort(arr):
    """ Sorts an array using a heap. """
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
    """

    def __init__(self):
        self.h_low = []
        self.h_high = []

    def add(self, new_value):
        """ Add element to the internal list and return new median. """
        if len(self.h_low) > 0:
            max_low = self.h_low[-1]
        else:
            max_low = float('inf')

        if len(self.h_high) > 0:
            min_high = self.h_high[0]
        else:
            min_high = float('-inf')

        if new_value < max_low:
            heapq.heappush(self.h_low, new_value)
        else:
            heapq.heappush(self.h_high, new_value)

        if len(self.h_low) > len(self.h_high) + 1:
            extra = heapq.heappop(self.h_low)
            heapq.heappush(self.h_high, extra)

        if len(self.h_high) > len(self.h_low) + 1:
            extra = heapq.heappop(self.h_high)
            heapq.heappush(self.h_low, extra)

        if (len(self.h_low) > len(self.h_high)):
            return self.h_low[-1]
        else:
            return self.h_high[0]

class Heap(object):
    """ Implementation of a min-heap. """

    def __init__(self, data):
        """ Initialize an empty heap. """
        if data is None:
            data = []
        self.data = data

    def insert(self, element):
        """ Adds an element to the heap.
        Initially insert the element as the next leaf, the bubble it up if
        necessary: if the parent is larger do a swap then recurse.

        NOTE when inserting a new node there can only be AT MOST one edge that
        is out of order, ie. does not have the heap property.

        Running time: O(log n)
        """
        self.data.append(element)
        self.bubble_up(len(self.data) - 1)

    def extract_min(self):
        """ Removes the head of the array, swaps in the tail (last leaf in
        the tree) then bubbles it down to restore the heap property.
        """
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        root = self.data.pop(-1)
        self.bubble_down(0)
        return root

    def remove(self, element):
        """ Removes the first occurance of an element from a heap.
        The last leaf in the heap is swapped in the position of the element.
        If if violates the heap property towards its parent then bubble up,
        otherwise bubble down.
        """
        try:
            index = self.data.index(element)
            self.data[index] = self.data.pop(-1)
            if self.data[int(index/2)] > self.data[index]:
                self.bubble_up(index)
            else:
                self.bubble_down(index)
        except ValueError as ve:
            pass
        return

    @staticmethod
    def heapafy(data):
        """ Initializes a heap from a list of numbers. """
        pass

    @staticmethod
    def parent(index):
        """ Computes the parent index of the given index. """
        if index % 2 == 0:
            return index/2 - 1
        else:
            return int(index/2)

    @staticmethod
    def is_heap(data):
        """ Checks if a list of numbers has the min heap property, ie. parent
        key is smaller than child keys
        Complexity: O(n)
        """
        for i in range(1, len(data)):
            if data[i] < data[Heap.parent(i)]:
                return False
        return True

    def bubble_up(self, index):
        """ Bubbles a value at position index to maintain the heap property:
        any parent node should be smaller than it's children.
        This will do at most log2 n (ie. the number of layers in the tree)
        swaps to restore the heap property.
        """
        while True:
            parent = int(index/2)
            if self.data[parent] < self.data[index]:
                break
            else:
                (self.data[parent], self.data[index]) = \
                    (self.data[index], self.data[parent])
                index = parent

    def bubble_down(self, parent):
        """ Bubbles down the element at position index (if it has any children).
        This is done by continuously swapping with the minimum of the two
        children keys.

        Running time: O(log2 n) the max number of swaps.
        """
        while True:
            left = parent * 2
            right = parent * 2 + 1
            min_index = self.get_min(parent, left, right)
            if min_index == parent:
                break

            (self.data[parent], self.data[min_index]) = \
                (self.data[min_index], self.data[parent])
            parent = min_index

    def get_min(self, parent, left, right):
        a = []
        try:
            a.append((self.data[parent], parent))
            a.append((self.data[left], left))
            a.append((self.data[right], right))
        except:
            pass

        __, min_index = min(a, key=lambda t: t[0])
        return min_index

