# -*- coding: utf-8 -*-


PARENT = 0
KEY = 1
LEFT = 2
RIGHT = 3
SIZE = 4

class BST(object):
    """ Implements the operations needed for a Ballanced Binary Search Tree.
Search Tree Property: for any node k, all keys in the left subtree are
    smaller than k and all keys in the right three are larger than k

    Two alternative implementations to consider:
    http://code.activestate.com/recipes/577540-python-binary-search-tree/
    http://www.laurentluce.com/posts/binary-search-tree-library-in-python/

    Attributes:
        root: list, represents the root node, format: [parent, key, left, right]
    """

    def __init__(self):
        self.root = None

    def insert(self, key):
        """ Insert a node into the data structure.

        For equal keys the convention is to keep them in the left subtree.
        Also increments the size of all nodes which are ancestors to the
        inserted node. The default size of a node is 1 because it can reach
        itself.

        Args:
            key: int, the value to insert in the tree.
        """
        if self.root is None:
            self.root = [None, key, None, None, 1]
            return

        node = self.root
        while True:
            if key > node[KEY]:
                path = RIGHT
            else:
                path = LEFT

            node[SIZE] += 1

            if node[path] is None:
                node[path] = [node, key, None, None, 1]
                break
            else:
                node = node[path]

    def search(self, key):
        """ Looks up a key in the data structure.

        Args:
            key: immutable value to look for.

        Returns:
            The node found in format [parent, key, left, right] or None.
        """
        node = self.root
        while True:
            if key == node[KEY]:
                return node
            elif key > node[KEY]:
                node = node[RIGHT]
            else:
                node = node[LEFT]
            if node is None:
                return None

    def get_max(self, root=None):
        """ Returns the node with the maximum value of the tree.

        Args:
            root: node, if specified it will be used as root for the
                search routine. Otherwise the tree's root will be used.

        Returns:
            A node [parent, key, left, right] with max key in the tree.
        """
        if root is None:
            root = self.root

        node = root
        while True:
            if node[RIGHT] is None:
                return node
            else:
                node = node[RIGHT]

    def get_min(self, root=None):
        """ Returns the node with the minimum value of the tree.

        Args:
            root: node, if specified it will be used as root for the
                search routine. Otherwise the tree's root will be used.

        Returns:
            A node [parent, key, left, right] with min key in the tree.
        """
        if root is None:
            root = self.root

        node = root
        while True:
            if node[LEFT] is None:
                return node
            else:
                node = node[LEFT]

    def predecessor(self, key):
        """ Finds the node with the largest key smaller the the given one.

        First find the node with key, then, if it's left subtree exists,
        find the maximum in it, otherwise move up through it's ancestors to
        find the one with smaller key.

        Args:
            key: int, value in the tree to find predecessor of.

        Returns:
            The immediate predecessor of key format [parent, key, left, right]
        """
        node = self.search(key)
        if node is None:
            return None

        if node[LEFT] is not None:
            return self.get_max(node[LEFT])
        else:
            node = node[PARENT]
            while True:
                if node[KEY] < key:
                    return node
                node = node[PARENT]
                if node is None:
                    return None

    def successor(self, key):
        """ Finds the node with the smallest key larger the the given one.

        Args:
            key: int, value in the tree to find predecessor of.

        Returns:
            The immediate successor of key format [parent, key, left, right]
        """
        node = self.search(key)
        if node is None:
            return None

        if node[RIGHT] is not None:
            return self.get_min(node[RIGHT])
        else:
            node = node[PARENT]
            while True:
                if node[KEY] > key:
                    return node
                node = node[PARENT]
                if node is None:
                    return None

    def delete(self, key):
        """ Removes the key from the tree.

        Three cases:
        1. if node has no children, it's easy, just remove it from the tree.
        2. if node has only one child, swap the child with the removed node.
        3. if the node has both children, compute it's predecessor, swap the
        predecessor in place of the deleted node, then call delete again on the
        new swapped node.

        This method also decrements the size of all ancestors of the deleted
        node.

        Args:
            key: int, a number to remove from the tree.
                 list, represents a node with the format [parent, key, left, right]

        Returns:
            The node just deleted is returned. Note! that is contains pointers.
        """
        if type(key) == int:
            node = self.search(key)
        else:
            node = key
        if node is None:
            return None
        parent = node[PARENT]

        if parent is None:
            direction = None
        elif parent[LEFT] == node:
            direction = LEFT
        else:
            direction = RIGHT

        # First case.
        if node[LEFT] is None and node[RIGHT] is None:
            parent[direction] = None
            self.decrement_sizes(parent)
            return node

        # Second case.
        if node[LEFT] is None or node[RIGHT] is None:
            if node[LEFT] is None:
                parent[direction] = node[RIGHT]
                node[RIGHT][PARENT] = parent
            else:
                parent[direction] = node[LEFT]
                node[LEFT][PARENT] = parent
            self.decrement_sizes(parent)
            return node

        # Third case.
        predecessor = self.predecessor(node[KEY])
        node[KEY], predecessor[KEY] = predecessor[KEY], node[KEY]
        self.delete(predecessor)

    def select(self, index):
        """ Finds the index'th order statistic in the containing data structure.

        Args:
            index: int, the order of the element to find.

        Returns:
            An int on the position index.
        """

    def rank(self, key):
        """ Given a key, computes how many elements are stritcly smaller than
        that key in the tree.
        """

    def list_sorted(self):
        """ In-order traversal of a binary search tree.

        Returns:
            A list with all elements in the data structure in sorted order.
        """
        output = []

        def traversal(node):
            if node[LEFT] is not None:
                traversal(node[LEFT])
            output.append(node)
            if node[RIGHT] is not None:
                traversal(node[RIGHT])

        traversal(self.root)
        return output

    def decrement_sizes(self, node):
        """ Decrements the sizes of node and all it's acestors.

        Args:
            node: list, of format [parent, key, left, right, size]
        """
        while node:
            node[SIZE] -= 1
            node = node[PARENT]

    @staticmethod
    def node_to_string(node):
        """ Prints the given node in a human readable way.

        Args:
            node: list, format [parent, key, left, right, size]
        """
        def print_key(node):
            if node is None:
                return 'None'
            else:
                return node[KEY]

        parent = print_key(node[PARENT])
        left = print_key(node[LEFT])
        right = print_key(node[RIGHT])
        return "[{parent}, {key}, {left}, {right}, {size}]".format( \
                                    parent=parent, key=node[KEY], left=left,
                                    right=right, size=node[SIZE])

    @classmethod
    def tree_to_string(cls, root):
        """ Prints the tree structure in a readable way. """
        # TODO fix this!
        node = root
        while node:
            print "({parent})->({left});".format(parent=cls.node_to_string(node),
                                        left=cls.node_to_string(node[LEFT]))
            print "({parent})->({right});".format(parent=cls.node_to_string(node),
                                        right=cls.node_to_string(node[RIGHT]))
            cls.tree_to_string(node[LEFT])
            cls.tree_to_string(node[RIGHT])

    @staticmethod
    def build(keys):
        """ Static method which builds a binary search tree.

        Args:
            keys: list, of integers to add to the tree.

        Returns:
            An instance of BST class.
        """
        b = BST()
        for key in keys:
            b.insert(key)
        return b


class RedBlackTree(BST):
    """ Implements ballanced red-black trees as a subclass of binary search tree.
    """

    def __init__(self):
        BST.__init__(self)
