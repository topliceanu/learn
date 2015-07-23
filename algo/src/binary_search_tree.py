# -*- coding: utf-8 -*-

from src.merge_sort import merge


PARENT = 0
KEY = 1
LEFT = 2
RIGHT = 3
SIZE = 4


class BinarySearchTreeNode(object):
    """ A node in a binary search tree.

    Implements all binary search tree algorithms recursively.

    Attrs:
        key: any, used to sort the tree.
        value: any, the value to store under the key.
        size: int, the number of nodes in the subtree rooted at current node.
        parent: object, reference to the parent node or None
        left: object, reference to the left child node or None
        right: object, reference to the right child node or None
    """
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.size = 1
        self.parent = None
        self.left = None
        self.right = None

    # Public API.

    def insert(self, key, value=None):
        """ Insert the new value in the appropriate direction. """
        if self.key > key:
            direction = 'left'
        else:
            direction = 'right'

        child = getattr(self, direction)
        if child == None:
            node = BinarySearchTreeNode(key, value)
            node.parent = self
            setattr(self, direction, node)

            # Recursively increment size of all parents of the newly inserted node.
            node = node.parent
            while node != None:
                node.size += 1
                node = node.parent
        else:
            child.insert(key, value)

    def lookup(self, key):
        """ Find a node with the given key in the subtree rooted by the current
        node.
        """
        if self.key == key:
            return self

        if self.key > key:
            direction = 'left'
        else:
            direction = 'right'
        child = getattr(self, direction)

        if child == None:
            return None
        else:
            return child.lookup(key)

    def get_min(self):
        """ Retrieves the node with the smallest key in the subtree rooted at
        the current node.
        """
        if self.left == None:
            return self
        return self.left.get_min()

    def get_max(self):
        """ Retrieves the node with the largest key in the subtree rooted at
        the current node.
        """
        if self.right == None:
            return self
        return self.right.get_max()

    def predecessor(self):
        """ Compute the node with the key immediately before the current
        node's key in the list of sorted keys.
        Two cases:
            1. node has a left child, return the maximum of the tree rooted in
                the left child.
            2. node has no left child, in which case we need to go up the parent
                list until we find a parent on the left side to return it or
                return None if the root is reached.
        """
        if self.left != None:
            return self.left.get_max()

        # Recurse up the parent stack until a parent in the right direction is found.
        node = self
        while node.parent != None:
            if node.parent.right == node:
                node = node.parent
            else:
                return node
        return None

    def successor(self):
        """ Compute the node whose key is immediately larger than current
        node's key in the list of sorted keys.
        Three cases:
            1. node has a right child, return the node with minimum key in the
                subtree rooted in the right child.
            2. node has no right child,
        """
        if self.right != None:
            return self.right.get_min()

        # Recurse up the parent stack until a parent in the left direction is found.
        node = self
        while node.parent != None:
            if node.parent.left == node:
                node = node.parent
            else:
                return node
        return None

    def rank(self):
        """ Returns the index of the current node in the array obtained by
        sorting all the nodes in the tree. OR. Returns the number of elements
        with the keys smaller or equal to the current node's key.

        A node is larger than all nodes in it's left subtree and all his
        ancestors from the right direction and the nodes in their left subtrees.
        """
        index = 0
        if self.left != None:
            index += self.left.size

        node = self.parent
        while node != None:
            if node.parent.right == node:
                index += 1
                if node.parent.left != None:
                    index += node.parent.left.rank()
            node = node.parent

        return index

    def select(self, index):
        """ Find the node whose position in the sorted array of keys of the
        subindexed tree is index.

        If node has less ancestors in the left side than the required index,
        then recurse on the right side, otherwise, recurse on the left side.
        """
        if self.left == None:
            left = 0
        else:
            left = self.size

        if index == left + 1:
            return node
        elif index < left + 1:
            return self.left.select(index)
        else:
            return self.right.select(index - left - 1)

    def delete(self):
        """ Removes the current node at the same time maintaining the search
        tree invariant.

        Cases:
        1. is node is leaf, then simply remove the node.
        2. if the node has one child, swap the child in place of the node.
        3. if the node has both children, compute the predecessor, swap it in
        place of the node, then call delete on the predecessor.
        """
        direction = 'left' if self.parent.left == self else 'right'

        if self.is_leaf(): # Case 1.
            setattr(self.parent, direction, None)
            setattr(self.parent, None)
            return self

        if self.left == None or self.right == None: # Case 2
            child_direction = 'left' if self.left != None else 'right'
            child = getattr(self.child_direction)
            setattr(self.parent, direction, child)
            setattr(child, 'parent', self.parent)
            self.parent.size -= 1
            self.parent = None
            setattr(self, child_direction, None)
            return self

        if self.left != None and self.right != None: # Case 3
            predecessor = self.predecessor()
            self.swap(predecessor)
            self.delete()

    def in_order_traversal(self):
        """ Traverse the tree rooted in this node, in the following order:
        left subtree, root, right subtree.
        """
        out = []
        if self.left != None:
            out.extend(self.left.in_order_traversal())
        out.append(self)
        if self.right != None:
            out.extend(self.right.in_order_traversal())
        return out

    def pre_order_traversal(self):
        """ Traverse the tree rooted in this node, in the following order:
        root, left subtree, right subtree.
        """
        out = [self]
        if self.left != None:
            out.extend(self.left.in_order_traversal())
        if self.right != None:
            out.extend(self.right.in_order_traversal())
        return out

    def post_order_traversal(self):
        """ Traverse the tree rooted in this node, in the following order:
        left subtree, right subtree, root.
        """
        out = []
        if self.left != None:
            out.extend(self.left.in_order_traversal())
        if self.right != None:
            out.extend(self.right.in_order_traversal())
        out.append(self)
        return out

    def common_ancestor(self, other):
        """ Detect the first common ancestor between the current node the
        passed other node.

        Start by checking if other is a descendent of self, if not, move up to
        the parent of self and see if other is found on the other child, etc.
        """
        if self == other:
            return self
        if self.left.lookup(other.key) == other:
            return self

        node = self
        while node != None:
            if node == other:
                return node
            if node.right != None and node.right.lookup(other.key) == other:
                return node
            node = node.parent
        return None

    def is_subtree(self, other):
        """ Check if the given other node is a subtree of the tree rooted in
        the current node.
        """
        if other == None:
            return False
        if self.key == other.key:
            return self.is_identical(other)
        is_left_subtree = self.left.is_subtree(other) if self.left != None else True
        is_right_subtree = self.right.is_subtree(other) if self.right != None else True
        return is_left_subtree and is_right_subtree

    def is_identical(self, other):
        """ Checks if two nodes have the same subtree keys. """
        if other == None:
            return False
        if self.key != other.key:
            return False
        if self.is_leaf() and other.is_leaf():
            return self.key == other.key
        if (self.is_leaf() and not other.is_leaf()) or (not self.is_leaf() and other.is_leaf()):
            return False

        return self.left.is_identical(other.left) and \
               self.right.is_identical(other.right)

    def is_leaf(self):
        """ Returns True if the node has no children. """
        return self.left == None and self.right == None

    def is_root(self):
        """ Returns True if the current node is the root of the tree. """
        return self.parent == None

    def diameter(self):
        """ Computes the diameter of the tree rooted in the current node.

        The diameter is the longest path of any two nodes in the subtree.
        It is computed as the maximum of:
        - the diameter of the left subtree
        - the diameter of the right subtree
        - the height of the left subtree plus the height of the right subtree
        """
        height_left = self.left.height() if self.left != None else 0
        height_right = self.right.height() if self.right != None else 0
        diameter_left = self.left.diameter() if self.left != None else 0
        diameter_right = self.right.diameter() if self.right != None else 0
        return max([height_left + height_right, diameter_left, diameter_right])

    def is_ballanced(self):
        """ Checks if the tree rooted in the current node is ballanced.

        Solution: a tree is ballanced if all the levels are fully completed
        except of the last one, ie. the depths of all leaves are not more than
        one unit of difference.
        """
        return self.max_depth() - self.min_depth() <= 1

    def merge(self, other):
        """ Merges the given binary tree into the current one. The result is a
        new data structure. This does not modify the current tree.
        """
        self_data = self.in_order_traversal()
        other_data = other.in_order_traversal()

        def merge(arr1, arr2):
            m = len(arr1)
            n = len(arr2)
            i = j = 0
            out = []

            while i < m and j < n:
                if arr1[i] < arr2[j]:
                    i += 1
                    out.append(arr1[i])
                else:
                    j += 1
                    out.append(arr2[j])

            if i == m:
                out.extend(arr2[j:])
            else:
                out.extend(arr1[i:])

            return out

        composed_data = merge(self_daata, other_data)
        return BinarySearchTreeNode.from_sorted_list(composed_data)

    # Utilities

    def swap(self, other):
        """ Interchange the current node with the other node by properly
        rewiring the pointers for parent, left and right children.
        """
        other_parent_direction = 'left' if other.parent.left == other else 'right'
        self_parent_direction = 'left' if self.parent.left == self else 'right'

        # Replace parent pointers for the two nodes.
        self.parent[self_parent_direction] = other
        other.parent[other_parent_direction] = self

        # Replace the two nodes' pointers to parents.
        tmp = other.parent
        other.parent = self.parent
        self.parent = tmp

        # Replace pointers for the children of two nodes.
        for direction in ['left', 'right']:
            tmp = getattr(self, direction)
            self_child = getattr(self, direction)
            other_child = getattr(other, direction)
            setattr(self, direction , other_child)
            setattr(other, direction, self_child)
            other_child.parent = self
            self_child.parent = other

    def rotate(self, direction):
        """ Rotate the current node with either his left or right child given
        by the direction parameter. Returns the new node.

        Left Rotation Schema:
                (p)                       (p)
                 |                         |
                (x)           =>          (y)
               /   \                     /   \
             ...   (y)                 (x)   ...
                  /   \               /   \
                (a)   ...           ...   (a)

        Right Rotation Schema:
                (p)                       (p)
                 |                         |
                (x)           =>          (y)
               /   \                     /   \
             (y)   ...                ...   (x)
            /   \                           /   \
          ...   (a)                       (a)   ...
        """
        parent_direction = 'left' if self.parent.left == self else 'right'
        other_direction = 'left' if direction == 'right' else 'right'

        x = self
        y = getattr(self, other_direction)
        a = getattr(y, direction)

        # Handle parent pointers.
        y.parent = x.parent
        if y.parent != None:
            setattr(y.parent, parent_direction, y)

        # Handle exchange between x and y.
        setattr(y, direction, x)
        x.parent = y

        # Handle rewire pointer for a node.
        setattr(x, other_direction, a)
        a.parent = x

    def depth(self):
        """ Compute the number nodes exist between current node and root. """
        if self.is_root():
            return 0
        return 1 + self.parent.depth()

    def height(self):
        """ Compute the number of node between current node and the furthest leaf.
        """
        if self.is_leaf():
            return 1
        heights = []
        if self.left != None:
            heights.append(self.left.height())
        if self.right != None:
            heights.append(self.right.height())
        return 1 + max(depths)

    def min_depth(self):
        """ Find the leaf in the subtree rooted the current node with the
        minimum depth.
        """
        if self.is_leaf():
            return 1
        min_left_depth = float('inf') if self.left == None else self.left.min_depth()
        min_right_depth = float('inf') if self.right == None else self.right.min_depth()
        return 1 + min([min_left_depth, min_right_depth])

    def max_depth(self):
        """ Find the leaf in the subtree rooted at the current node with the
        maximum depth.
        """
        if self.is_leaf():
            return 1
        max_left_depth = float('-inf') if self.left == None else self.left.max_depth()
        max_right_depth = float('-inf') if self.right == None else self.right.max_depth()
        return 1 + min([min_left_depth, min_right_depth])

    # Statics

    @classmethod
    def from_list(cls, arr):
        """ Builds a new binary search tree by sequentially inserting each
        element in arr.

        Args:
            arr: list of tuples, format [(key, value)]

        Return:
            object, instance of src.binary_search_tree.BinarySearchTreeNode
        """
        root = cls(arr[0][0], arr[0][1])
        for (key, value) in arr[1:]:
            root.insert(key, value)
        return root

    @classmethod
    def from_sorted_list(cls, arr):
        """ Given a previously sorted array, builds a ballanced binary search
        tree.
        """

        def build(arr, left, right):
            """ Builds a ballanced binary search tree given a slice of a
            sorted list.
            """
            if left > right:
                return None

            middle = (right + left) / 2
            root = cls(arr[middle])
            root.size = len(arr[left:middle])
            root.left = build(arr, left, middle-1)
            root.right = build(arr, middle+1, right)
            return root

        return build(arr, 0, len(arr))


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
            A list representing the newly inserted node. Format:
                [parent, key, left, right, size]
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

    def search(self, key, node=None):
        """ Looks up a key in the data structure.

        Complexity: O(log n)

        Args:
            key: immutable value to look for.
            node: node to start the search from. By default it is the root.
                Format: [parent, key, left, right, size]

        Returns:
            The node found in format [parent, key, left, right, size] or None.
        """
        if node == None:
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

        A tree can have multiple keys with the same value. The convention
        adopted in this implementation is that all identical keys are sent to
        the self subtree upon insertion. This method exploits this behaviour by
        only searching the left subtree after a failed match against a found
        node with the similar key as the root of bst.

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

            if found_root[LEFT] != None:
                found_root = self.search(root_key, found_root[LEFT])
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
            node: list, corresponds to X in the schemas. Format:
                [parent, key, left, right, size]
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

    def depth(self, node):
        """ Computes the depth of a node in a binary search tree, ie. the
        number levels the subtree whose root the given node is.

        Args:
            node: name of the node to compute depth for.

        Return:
            int: depth of input node.
        """
        if node is None:
            return 0
        left = 1 + self.depth(node[LEFT])
        right = 1 + self.depth(node[RIGHT])
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
