# -*- coding: utf-8 -*-

from src.merge_sort import merge


PARENT = 0
KEY = 1
LEFT = 2
RIGHT = 3
SIZE = 4

class BST(object):
    """ Implements the operations needed for a Unballanced Binary Search Tree.

    Search Tree Property: for any node k, all keys in the left subtree are
    smaller than k and all keys in the right three are larger than k

    Two alternative implementations to consider:
    http://code.activestate.com/recipes/577540-python-binary-search-tree/
    http://www.laurentluce.com/posts/binary-search-tree-library-in-python/

    All operations have a complexity of O(log n)
    Each node is encapsulated as a list (not a dict) for performance reasons.

    Attributes:
        root: list, represents the root node, format:
            [parent, key, left, right, size]
    """

    def __init__(self):
        self.root = None

    def __len__(self):
        """ Returns the number of nodes in the binary search tree. """
        if self.root == None:
            return 0
        return self.root[SIZE]

    def insert(self, key):
        """ Insert a node into the data structure.

        For equal keys the convention is to keep them in the left subtree.
        Also increments the size of all nodes which are ancestors to the
        inserted node. The default size of a node is 1 because it can only
        reach itself.

        Complexity: O(log n)

        Args:
            key: int, the value to insert in the tree.

        Returns:
            A list representing the newly inserted node.
        """
        if self.root is None:
            self.root = [None, key, None, None, 1]
            return self.root

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
        return node[path]

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
            A node [parent, key, left, right, size] with max key in the tree.
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
            A node [parent, key, left, right, size] with min key in the tree.
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
        """ Finds the node with the largest key smaller than the given one.

        First find the node with key, then, if it's left subtree exists,
        find the maximum in it, otherwise move up through it's ancestors to
        find the one with smaller key.

        Complexity: O(log n)

        Args:
            key: int, value in the tree to find predecessor of.

        Returns:
            The immediate predecessor of given key. Format;
                [parent, key, left, right, size]
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

        If the node has a right subtree, return the node with min key.
        Otherwise, moves ups the parrent hierarchy until it reaches a node
        with a key larger that the queried key.

        Complexity: O(log n)

        Args:
            key: int, value in the tree to find predecessor of.

        Returns:
            The immediate successor of given key. Format:
                [parent, key, left, right, size]
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

        Note: a better solution in complexity might be to just traverse the
        graph in sorted order then return the requested interval.

        Args:
            start_key: int, value in the tree to start traversing.
            end_key: int, value in the tree to traverse to.

        Returns:
            A list of all contained data from start_key to end_key.
        """
        key = start_key
        if self.search(key) is None:
            return []
        output = [key]

        while True:
            node = self.successor(key)
            if node is None or node[KEY] > end_key:
                break
            key = node[KEY]
            output.append(key)
        return output

    def delete(self, key):
        """ Removes the key from the tree.

        Three cases:
        1. if node has no children, it's easy, just remove it from the tree.
        2. if node has only one child, swap the child with the removed node.
        3. if the node has both children, compute it's predecessor, swap the
        predecessor in place of the deleted node, then call delete again on the
        new swapped node (ie. recurse).

        This method also decrements the size of all ancestors of the deleted
        node. The size of a node is the number of nodes in it's subtree.

        Complexity: O(log n)

        Args:
            key: int, a number to remove from the tree.
                 list, represents a node with the format:
                    [parent, key, left, right, size]

        Returns:
            The node just deleted is returned. Note! that is still contains
            old pointers.
        """
        if type(key) != list:
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

        # First case: node is leaf.
        if node[LEFT] is None and node[RIGHT] is None:
            parent[direction] = None
            self.decrement_sizes(parent)
            return node

        # Second case: node has only one child.
        if node[LEFT] is None or node[RIGHT] is None:
            if node[LEFT] is None:
                parent[direction] = node[RIGHT]
                node[RIGHT][PARENT] = parent
            else:
                parent[direction] = node[LEFT]
                node[LEFT][PARENT] = parent
            self.decrement_sizes(parent)
            return node

        # Third case: node has both children.
        predecessor = self.predecessor(node[KEY])
        node[KEY], predecessor[KEY] = predecessor[KEY], node[KEY]
        return self.delete(predecessor)

    def select(self, index, node = None):
        """ Finds the i'th order statistic in the containing data structure.

        Uses an extra invariant stored for each node: the size, ie. the number
        of nodes in the subgraph whose parent it is. A node's size is equivalent
        to the key's position in sorted keys list. This method looks up the key
        with the size equal to index.

        Complexity: O(log n)

        Args:
            index: int, the order of the element to find. Order starts with 0.
            node: list, format [parent, key, left, right, size] the root
                node of the search.

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

    def rank(self, key):
        """ Given a key, computes how many elements are stritcly smaller than
        that key in the tree.

        This is possible because we are keeping score on the number of nodes
        in the subtree for each node, ie. SIZE.

        Complexity: O(log n)

        Args:
            key: int, the value to look for.

        Returns:
            An int representing the number of keys strictly smaller.
            None if the key is not found the data structure.
        """
        if self.search(key) is None:
            return None
        # start looking for key from the root node.
        return self.recursive_rank(key, self.root)

    def recursive_rank(self, key, node):
        """ Recursive pair of .rank() method.

        This method combines recursive lookup for a node with given key from
        left to right and then aggregate the number of nodes smaller than key.

        Args:
            key: int, the key we are looking for.
            node: list, the node we are currently investigating. Format:
                [parent, key, left, right, size]
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
        """ Serialized the binary tree.

        See: http://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
        for usage example.

        Returns:
            A list with all keys in the tree in sorted order.
        """
        return self.in_order_traversal()

    def in_order_traversal(self):
        """ Return a list of node keys ordered LEFT, ROOT then RIGHT. """
        output = []

        def traversal(node):
            if node == None:
                return
            traversal(node[LEFT])
            output.append(node[KEY])
            traversal(node[RIGHT])

        traversal(self.root)
        return output

    def pre_order_traversal(self):
        """ Return a list of node keys ordered ROOT, LEFT then RIGHT. """
        output = []

        def traversal(node):
            if node == None:
                return
            output.append(node[KEY])
            traversal(node[LEFT])
            traversal(node[RIGHT])

        traversal(self.root)
        return output

    def post_order_traversal(self):
        """ Return a list of node keys ordered LEFT, RIGHT then ROOT """
        output = []

        def traversal(node):
            if node == None:
                return
            traversal(node[LEFT])
            traversal(node[RIGHT])
            output.append(node[KEY])

        traversal(self.root)
        return output

    def is_subtree(self, bst):
        """ Checks if input bst is a subtree of the current bst.

        Args:
            bst: object, instance of src.binary_search_tree.BST

        Returns:
            bool
        """
        def match_tree(root1, root2):
            if root1 == None and root2 == None:
                return True
            if (root1 == None or root2 == None):
                return False
            if root1[KEY] != root2[KEY]:
                return False
            if match_tree(root1[LEFT], root2[LEFT]) == False:
                return False
            return match_tree(root1[RIGHT], root2[RIGHT])

        root_key = bst.root[KEY]
        found_root = self.search(root_key)
        while found_root != None:
            match = match_tree(found_root, bst.root)
            if match is True:
                return True
            if found_root[LEFT] != None and found_root[LEFT][KEY] == root_key:
                found_root = found_root[LEFT]
            elif found_root[RIGHT] != None and found_root[RIGHT][KEY] == root_key:
                found_root = found_root[RIGHT]
            else:
                found_root = None

        return False

    # UTILITIES

    def decrement_sizes(self, node):
        """ Decrements the sizes of a given node and all it's acestors.

        Args:
            node: list, of format [parent, key, left, right, size]
        """
        while node:
            node[SIZE] -= 1
            node = node[PARENT]

    def rotate(self, node, DIRECTION=LEFT):
        """ Interchange between node and one of it's children.

        If direction is LEFT, then interchange between node and it' right child,
        otherwise if direction is RIGHT, interchange between node and it's
        left child.
        This operation is done in O(1) and preserves the search tree property.

        Schema (for right rotations):

                (P)                        (P)
                 |                          |
                (X)                        (Y)
               /   \           =>         /   \
            (A)    (Y)                 (X)    (C)
                  /   \               /   \
                (B)    (C)          (A)    (B)

        Schema (for left rotations):

                (P)                        (P)
                 |                          |
                (X)                        (Y)
               /   \           =>         /   \
            (Y)    (C)                 (A)    (X)
           /   \                             /   \
         (A)   (B)                        (B)    (C)

        Note! P, A, B and/or C can be None, this method accomodates that case.

        Args:
            node: list, format [parent, key, left, right, size]
            DIRECTION: number, either LEFT or RIGHT constants indicates the
                direction of the "soon to be rotated" node.
        """
        # Build a reference to the parent node and the direction of node
        # in relation to it's parent.
        parent = node[PARENT] # coresponds to P from schemas.
        if parent != None:
            if parent[LEFT] == node:
                PARENT_DIRECTION = LEFT
            else:
                PARENT_DIRECTION = RIGHT

        # Compute the other
        if DIRECTION == LEFT:
            OTHER_DIRECTION = RIGHT
        else:
            OTHER_DIRECTION = LEFT

        # Compute pointers to the nodes that will move position:
        child = node[DIRECTION] # Coresponds to Y from schemas.
        other_child = child[OTHER_DIRECTION] # Corresponds to B in schemas.

        # Update sizes for rotated nodes.
        child[SIZE] = node[SIZE]
        node[SIZE] = 1
        if node[OTHER_DIRECTION] != None:
            node[SIZE] += node[OTHER_DIRECTION][SIZE]
        if child[OTHER_DIRECTION] != None:
            node[SIZE] += child[OTHER_DIRECTION][SIZE]

        # Swap node with it's child.
        # Rewire pointers for parent, node, child and other_child.
        if parent != None:
            parent[PARENT_DIRECTION] = child
        child[PARENT] = parent
        child[OTHER_DIRECTION] = node
        node[PARENT] = child
        node[DIRECTION] = other_child
        if other_child != None:
            other_child[PARENT] = node
        if parent == None:
            self.root = child

    def to_string(self):
        """ Prints a human readable version of the current tree.

        Return:
            str, text representation of the current tree
        """
        out = ''
        nodes = [self.root]
        while (len(nodes) != 0):
            node = nodes.pop()
            if node[LEFT] != None:
                nodes.insert(0, node[LEFT])
                out += '{parent}-l>{left}; '.format(parent=node[KEY],
                                                   left=node[LEFT][KEY])
            if node[RIGHT] != None:
                nodes.insert(0, node[RIGHT])
                out += '{parent}-r>{right}; '.format(parent=node[KEY],
                                                    right=node[RIGHT][KEY])
        return out

    def depth(self, vertex):
        """ Computes the depth of a node in a binary search tree, ie. the
        number levels the subtree whose root the given vertex is.

        Args:
            vertex: name of the vertex to compute depth for.

        Return:
            int: depth of input node.
        """
        if vertex is None:
            return 0
        left = 1 + self.depth(vertex[LEFT])
        right = 1 + self.depth(vertex[RIGHT])
        return max(left, right)

    def diameter(self):
        """ Computes the diameter of the current binary tree. """
        return self.diameter_subtree(self.root)

    def diameter_subtree(self, root):
        """ Computes the diameter of a binary tree given by root.

        The diameter (or the width) of a tree is the longest path from two
        leaves in the tree. Can be one of three quantities:
        - the diameter of the tree's left subtree
        - the diameter of the tree's right subtree
        - the longest path between leaves that goes through a common root
            (this can be computed from the heights of the subtrees)

        Args:
            root: format [parent, key, left, right, size] root of the subtree
                to compute the diameter for.

        Returns:
            int: the diameter of the current tree.
        """
        if root == None:
            return 0

        left_depth = self.depth(root[LEFT])
        right_depth = self.depth(root[RIGHT])
        left_diameter = self.diameter_subtree(root[LEFT])
        right_diameter = self.diameter_subtree(root[RIGHT])

        return max((left_depth + right_depth + 1), \
                    max(left_diameter, right_diameter))

    @staticmethod
    def is_ballanced_binary_search_tree(bst):
        """ Method checks if the tree is maintains the ballanced binary search
        tree invariants:
        - left subtree keys are always smaller than the root key, right subtree
        keys are always larger than root key
        - all the layers of the tree are completely filled except for the last
        one which is partially filled.

        To make it easier, compute the largest depth and the smallest depth.
        They should not be more then 1 apart.

        Args:
            bst: instance of src.binary_search_tree.BST

        Returns:
            bool
        """
        if BST.is_binary_search_tree(bst.root) == False:
            return False

        def min_max_depth(node):
            if node == None:
                return (0, 0)

            (min_left, max_left) = min_max_depth(node[LEFT])
            (min_right, max_right) = min_max_depth(node[RIGHT])

            return (1 + min(min_left, min_right), 1 + max(max_left, max_right))

        (min_depth, max_depth) = min_max_depth(bst.root)
        return 0 <= max_depth - min_depth <= 1

    @staticmethod
    def is_binary_search_tree(root):
        """ Static method verifies the binary search tree requirement for all
        nodes in the tree.

        That is for each node in the tree, it's left child, if it exists, is
        smaller, while it's right child, if it exists, must be larger.

        Complexity: O(nlogn)

        Args:
            root: list, format [parent, key, left, right, size] is the root
                of the tree under inspection.

        Returns:
            bool
        """
        def check(node):
            if node[LEFT] is not None:
                if node[LEFT][KEY] > node[KEY]:
                    return False
                else:
                    node = node[LEFT]
                    return check(node)
            if node[RIGHT] is not None:
                if node[RIGHT][KEY] < node[KEY]:
                    return False
                else:
                    node = node[RIGHT]
                    return check(node)
            return True

        return check(root)

    @classmethod
    def build(cls, keys):
        """ Static method which builds a binary search tree of an indicated type.

        Args:
            keys: list, of integers to add to the tree.

        Returns:
            An instance of BST class.
        """
        b = cls()
        for key in keys:
            b.insert(key)
        return b

    @classmethod
    def from_sorted(cls, sorted_list):
        """ Static method which transforms a sorted list of keys into a
        ballanced binary search tree.

        To make the tree ballanced given a sorted array, the root is the middle
        element, while the left child is the middle element of the left subarray,
        and the right child is the middle element of the right subarray.

        Complexity: O(n) - n is the length of input list.

        Args:
            sorted_list: list, of values in _ascending_ sorted order.

        Returns:
            object, instance of BST
        """

        def traverse(sorted_list, start, end):
            if start > end:
                return None

            mid = (start + end) / 2
            left = traverse(sorted_list, start, mid-1)
            right = traverse(sorted_list, mid+1, end)

            # Compute size of root!
            if left == None and right == None:
                size = 1
            elif left != None and right != None:
                size = max(left[SIZE], right[SIZE]) + 1
            elif left != None:
                size = left[SIZE] + 1
            elif right != None:
                size = right[SIZE] + 1

            root = [None, sorted_list[mid], left, right, size]

            # Hookup pointers to the parent for left/right nodes.
            if left != None:
                left[PARENT] = root
            if right != None:
                right[PARENT] = root

            return root

        bst = cls()
        bst.root = traverse(sorted_list, 0, len(sorted_list)-1)
        return bst

    @classmethod
    def join(cls, tree1, tree2):
        """ Joins two ballanced binary search trees toghether into a new
        ballanced binary search tree.

        What is important is to maintain the search tree property, make sure
        it is ballanced and correctly update each node's size.

        Methods: (n - # nodes of self; m - # nodes of other)
        1. Take all nodes in other and inserts them in self. Complexity O(mlogn)
        2. Convert self and other to sorted lists O(n) O(m), join them O(m+n),
        convert a sorted list into a ballanced binary search tree O(m+n)

        Args:
            tree1: object, instance of BST
            tree2: object, instance of BST

        Return:
            object, instance of BST
        """
        sorted1 = tree1.list_sorted()
        sorted2 = tree2.list_sorted()
        joined_sorted = merge(sorted1, sorted2)

        return cls.from_sorted(joined_sorted)
