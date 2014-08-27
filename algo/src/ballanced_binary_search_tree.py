# -*- coding: utf-8 -*-


PARENT = 0
KEY = 1
LEFT = 2
RIGHT = 3

class BBST(object):
    """ Implements the operations needed for a Ballanced Binary Search Tree.

    Search Tree Property: for any node k, all keys in the left subtree are
    smaller than k and all keys in the right three are larger than k

    Two alternative implementations to consider:
    http://code.activestate.com/recipes/577540-python-binary-search-tree/
    http://www.laurentluce.com/posts/binary-search-tree-library-in-python/

    Attributes:
        root: list, represents the root node, format: [parent, key, left, right]
        length: int, number of nodes in the structure.
    """

    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, key):
        """ Insert a node into the data structure.

        For equal keys the convention is to keep them in the left subtree.

        Args:
            key: int, the value to insert in the tree.
        """
        if self.root is None:
            self.root = [None, key, None, None]
            self.length += 1
            return

        node = self.root
        while True:
            if key > node[KEY]:
                path = RIGHT
            else:
                path = LEFT
            if node[path] is None:
                node[path] = [node, key, None, None]
                self.length += 1
                break
            else:
                node = node[path]

    def search(self, key):
        """ Looks up a key in the data structure.

        Args:
            key: immutable value to look for.

        Returns:
            A bool indicating whether key exists or not in the structure.
        """
        if self.root is None:
            return False

        node = self.root
        while True:
            if key == node[KEY]:
                return True
            elif key > node[KEY]:
                node = node[RIGHT]
            else:
                node = node[LEFT]
            if node is None:
                return False

    def select(self, index):
        """ Finds the index'th order statistic in the containing data structure.

        Args:
            index: int, the order of the element to find.

        Returns:
            An int on the position index.
        """

    def max(self):
        return self.select(self._len)

    def min(self):
        return self.select(0)

    def predecessor(self, key):
        pass

    def successor(self, key):
        pass

    def rank(self, key):
        pass

    def output(self):
        """ In-order traversal of a binary search tree.

        Returns:
            A list with all elements in the data structure in sorted order.
        """

