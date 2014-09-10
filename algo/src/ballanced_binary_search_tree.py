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

    All operations have a complexity of O(log n)

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

        Complexity: O(log n)

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

        Complexity: O(log n)

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

        Complexity: O(log n)

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

        Complexity: O(log n)

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

        Complexity: O(log n)

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

        Complexity: O(log n)

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

    def range_query(self, start_key, end_key):
        """ Return all keys between start_key and end_key in a sorted order.

        Complexity: O(k*log n) where k is the number of keys between
        start_key and end_key.

        Args:
            start_key: int, value in the tree to start traversing.
            end_key: int, value in the tree to traverse to.

        Returns:
            A list of all contained data from start_key to end_key.
        """
        if self.search(start_key) is None:
            return []

        output = [start_key]
        while True:
            node = self.successor(start_key)
            if node is None or node[KEY] > end_key:
                break
            output.append(node[KEY])
        return output

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

        Complexity: O(log n)

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

    def select(self, index, node = None):
        """ Finds the i'th order statistic in the containing data structure.

        Complexity: O(log n)

        Args:
            index: int, the order of the element to find. Order starts with 0.
            root: list, format [parent, key, left, right, size] the
                root of the search.

        Returns:
            The key of element on the index position in the sorted list.
        """
        if node is None:
            node = self.root

        if node[LEFT] is None:
            left = 0
        else:
            left = node[LEFT][SIZE]

        if index == left + 1:
            return node
        if index < left + 1:
            return self.select(index, node[LEFT])
        else:
            return self.select(index - left - 1, node[RIGHT])

    def rank(self, key, node=None):
        """ Given a key, computes how many elements are stritcly smaller than
        that key in the tree.

        Complexity: O(log n)

        Args:
            key: int, the value to look for.

        Returns:
            An int representing the number of keys strictly smaller.
            None if the key is not found the data structure.
        """
        if self.search(key) is None:
            return None
        if node is None:
            node = self.root
        return self.recursive_rank(key, node)

    def recursive_rank(self, key, node):
        """ Recursive pair of .rank() method.

        The idea is to traverse the tree starting from the root.
        """
        if node is None:
            return 0

        if node[LEFT] is None:
            left_size = 0
        else:
            left_size = node[LEFT][SIZE]

        if node[KEY] == key:
            return left_size
        elif key < node[KEY]:
            return self.recursive_rank(key, node[LEFT])
        else:
            return 1 + left_size + self.recursive_rank(key, node[RIGHT])

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

    def rotate(self, node, direction=LEFT):
        """ Interchange between node and one of it's children.

        If direction is LEFT, then interchange between node and it' right child,
        otherwise if direction is RIGHT, interchange between node and it's
        left child.
        This operation is done in O(1) and preserves the search tree property.

        TODO finish up the implementation and tests.

        Args:
            node: list, format [parent, key, left, right, size]
            direction: number, either LEFT or RIGHT.
        """
        if node[PARENT][LEFT] == node:
            parent_direction = LEFT
        else:
            parent_direction = RIGHT

        child = node[direction]

        if direction == LEFT:
            other_direction = RIGHT
        else:
            other_direction = LEFT
        other_child = node[other_direction]

        node[PARENT][parent_direction] = child
        child[PARENT] = node[PARENT]

        child[other_direction] = node
        node[PARENT] = child

        node[direction] = child[other_direction]
        child[other_direction][PARENT] = node

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
    TODO implement this to maintain invariants.
    """

    def __init__(self):
        BST.__init__(self)

    def insert(self, key):
        """ Insert a key in the RB tree preserving the invariants. """
