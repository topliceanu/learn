# -*- coding: utf-8 -*-

import random


class Node(object):
    """ An node in a skip list.

    Attrs:
        next: list, references to the next element each level of the skip list.
        value: int, the key to store.
    """
    def __init__(self, value, levels):
        self.next = [None] * levels
        self.value = value

class SkipList(object):
    """ Implements a skip list data structure with the dictionary interface.

    See: http://igoro.com/archive/skip-lists-are-fascinating/ for a reference
    implementation.
    See: http://www.cs.umd.edu/~meesh/420/Notes/MountNotes/lecture11-skiplist.pdf

    Attrs:
        head: object, pointer to the first node in the structure, without value.
        end: object, pointer to the last node in the structure, without value.
        levels: int, number of levels in the data structure. Usually the number
            of levels depends on the number of keys n to store: log(n)
    """
    def __init__(self, levels=10):
        self.levels = levels
        self.head = Node(float('-inf'), levels)
        self.end = Node(float('inf'), levels)
        for level in xrange(levels):
            self.head.next[level] = self.end

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

        for level in xrange(max_level+1):
            head = self.head
            while head.next[level].value < value and head.next[level] != self.end:
                head = head.next[level]
            node.next[level] = head.next[level]
            head.next[level] = node

    def list_sorted(self, level=0):
        """ Returns a list of all the containing data in sorted order for the
        given level.

        Complexity: O(n)

        Params:
            level: int, the level on which to print the succession of values.

        Returns:
            list, sorted items in the specified levels.
        """
        current = self.head.next[level]
        out = []

        while current != self.end:
            out.append(current.value)
            current = current.next[level]

        return out

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
        pointer = self.head
        while pointer != self.end:
            if pointer.next[level].value > value:
                level -= 1
                if level < 0:
                    return False
            elif pointer.next[level].value == value:
                return True
            elif pointer.next[level].value < value:
                pointer = pointer.next[level]
        return False

    def remove(self, value):
        """ Removes a node from the data structure.

        Recurse on every level, whenever the element is found, the node is
        removed from that level.

        Complexity: O(log n)

        Args:
            value: int, the value to remove from the node.

        Returns:
            boolean, whether or not the element was present in the first place.
        """
        level = self.levels - 1
        pointer = self.head
        while pointer != self.end:
            if pointer.next[level].value > value:
                level -= 1
                if level < 0:
                    return False
            elif pointer.next[level].value == value:
                # The element was found.
                for level in xrange(self.levels):
                    if pointer.next[level] != None:
                        pointer.next[level] = pointer.next[level].next[level]
                return True
            elif pointer.next[level].value < value:
                pointer = pointer.next[level]
        return False
