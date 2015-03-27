# -*- coding: utf-8 -*-

import random


class Node(object):
    """ An node in a skip list.

    Attrs:
        next: list, references to the next element each level of the skip list.
    """
    def __init__(self, value, levels):
        self.next = [None] * levels
        self.value = value

class SkipList(object):
    """ Implements a skip list data structure with the dictionary interface.

    Operations:
    - Insertion O(log n)
    - Removal O(log n)
    - Lookup O(log n)
    - Enumerate O(n)

    Attrs:
        head: list, of pointers to the first element in each level.
        levels: int, number of levels in the data structure.
    """

    def __init__(self, levels=10):
        self.levels = levels
        self.head = [Node(float('-inf'), levels) for i in xrange(levels)]

    def insert(self, value):
        """ Insert an element in the data structure.

        Randomly decide how many levels will the current value be present in: a
        node will be present in level k with a probability of 1/2^k

        Complexity: O(log n)

        Args:
            value: int, the value to insert to the database.
        """
        node = Node(value, self.levels)
        max_level = random.choice(range(self.levels))

        for level in xrange(max_level):
            head = self.head[level]
            while head != None and head.value > value:
                head = head.next[level]
            head.next[level] = node

    def lookup(self, value):
        """ Lookup a value in the skip list.

        Start by looking up from the top level to the bottom level. On each
        level, whenever we encounter a pointer to a larger value, we backtrack
        to the previous value and decrement the level.

        Complexity: O(log n)

        Args:
            value: int, the value to lookup in the data structure.

        Returns
            boolean, whether or not the value is present.
        """
        level = self.levels - 1
        pointer = self.head[level]
        while pointer != None:
            if pointer.value > value:
                return False
            elif pointer.value == value:
                return True
            elif pointer.value < value:
                level -= 1
                if level < 0:
                    pointer = None
                else:
                    pointer = pointer.next[level]
        return False

    def delete(self, value):
        """ Removes a node from the data structure.

        Recurse on every level, whenever the element is found, the node is
        removed from that level.

        Complexity: O(log n)

        Args:
            value: int, the value to remove from the node.

        Returns:
            boolean, whether or not the element was present in the first place.
        """
        found = False
        for level in xrange(self.levels-1, 0, -1):
            head = self.head[level]
            while head.next[level].value < value:
                head = head.next[level]
            if head.next[level].value == value:
                found = True
                head.next[level] = head.next[level].next[level]
        return found
