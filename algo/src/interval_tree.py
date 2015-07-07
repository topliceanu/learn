# -*- coding: utf-8 -*-


class Node(object):
    """ A node in an interval tree.

    Attrs:
        key: float, the start of the interval.
        end: float, the end of the interval.
        high: float, the highest end interval of all the intervals in the
            subtree whose root is this node.
        left: object, instance of src.interval_tree.Node
        right: object, instance of src.interval_tree.Node
        parent: object, instance of src.interval_tree.Node
    """
    def __init__(self, interval):
        self.key = interval[0]
        self.end = interval[1]
        self.high = interval[1]
        self.left = None
        self.right = None
        self.parent = None

class IntervalTree(object):
    """ Implements an interval tree. This data structure is optimal for
    determinine efficiently all the intervals which overlap with any given
    interval or point.

    This particular implementation is using the augmented tree aproach.

    See: https://en.wikipedia.org/wiki/Interval_tree#Augmented_tree

    Complexity: O(log n) in time, O(n) in space, construction is O(nlogn)

    Attrs:
        root: object, instace of src.interval_tree.Node
    """

    def __init__(self):
        self.root = None

    def insert(self, interval):
        """ Inserts the interval into the tree. """
        if self.root == None:
            self.root = Node(interval)
            return self.root

        (start, end) = interval
        node = self.root
        while True:
            if node.key <= start:
                path = 'right'
            else:
                path = 'left'

            # Maintain the high invariant, each node contains the leftmost
            # value in it's subtree.
            if node.high < end:
                node.high = end

            # Add a new node leaf.
            if getattr(node, path, None) is None:
                setattr(node, path, Node(interval))
                getattr(node, path).parent = node
                break
            else:
                node = getattr(node, path)

        return getattr(node, path)

    def delete(self, interval):
        pass

    def lookup_value(self, value):
        results = []

        if value > self.root.high:
            return results

        node = self.root
        while node != None:
            if node.key <= value <= node.end:
                results.append((node.key, node.end))

            if value <= node.key:
                node = node.left
            else:
                node = node.right

        return results

    def lookup_interval(self, interval):
        pass
