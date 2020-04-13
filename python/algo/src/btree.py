# -*- coding: utf-8 -*-

import bisect

from src.binary_search_tree import BST


# TODO implement [Mond&Raz, 1985] to support a single pass-down.

class BTree(object):
    """ Acts as a facade to the root node of the BTree.

    Attrs:
        m: tree order, the number of children allowed for a node. Consequently
           the a node can only host m-1 values.
        root: object, src.btree.BTreeNode, root of the tree structure.
    """
    def __init__(self, m):
        self.m = m
        self.root = BTreeNode(m)

    def traverse(self):
        """ Traverses all values in the tree in a structured order. """
        return self.root.traverse()

    def lookup(self, key):
        """ Searches the value corresponding to the key. """
        return self.root.lookup(key)

    def insert(self, key, value):
        """ Inserts a new value in the tree. This may lead to the formation of
        a new root, which this method handles as well.
        """
        self.root.insert(key, value)

        # Update the new root if need be.
        node = self.root
        while node.parent != None:
            node = node.parent
        self.root = node

    def merge(self, other_btree):
        """ Merges another btree into the current one. """
        pass

    @classmethod
    def build(cls, m, data):
        """ Builds a new BTree given a dictionary of (key, value) pairs.

        The method used is called "bulkloading

        Args:
            m: int, order of the tree
            data: list, of tuples, format [(key, value)]

        Returns:
            object, instance of src.btree.BTree
        """
        # TODO
        data = sorted(data, key=lambda x: x[0]) # Sort pairs by key.
        nodes = {} # Holds nodes and they governing value as key.

        while True:
            # Split into chunks of size m
            chunks = [data[i:i+m] for i in range(0, len(data), m)]
            data = []
            for chunk in chunks:
                parent = chunk.pop()
                data.append(parent)
                node = BTreeNode(m)
                node.keys = map(lambda i: i[0], chunk)
                node.values = map(lambda i: i[0], chunk)
                nodes[parent[0]] = node


class BTreeNode(object):
    """ This class represents a node in the BTree data structure.

    Invariants for BTree of rank m:
    - every node has at most m children.
    - every non-leaf node (except for the root) has at least m/2 children.
    - a node has at least two children if not a leaf.
    - a non-leaf node with k-1 keys has k children.
    - all keys in a node are sorted, and all keys in the tree are sorted.
    - all leaves are on the same level.

    Complexity: O(log n) for most operations (lookup, insert)

    References:
        http://www.cs.cornell.edu/courses/cs3110/2009sp/recitations/rec25.html
        https://gist.github.com/teepark/572734
        http://www.geeksforgeeks.org/b-tree-set-1-introduction-2/ - proactive approach to insertion.
        http://en.wikipedia.org/wiki/B-tree
        http://www.semaphorecorp.com/btp/algo.html
        http://www.bluerwhite.org/btree/

    Attrs:
        m: rank fo the node, ie. you are only allowed m children and m-1 values.
        parent: object, pointer to the parent node of this node.
        keys: list, of sorted items. The format is [(key, value, ref)]
        values: list, of values stored in the node associated with the keys
        refs: list, of reference to a lower lever instance of the BTreeNode
    """
    def __init__(self, m):
        """ A new node can be created in two ways: either an empty node or
        prepopulate node with keys and values.
        """
        self.m = m
        self.parent = None
        self.keys = []
        self.values = []
        self.refs = []

    def insert(self, key, value):
        """ Inserts a new value in the tree.

        Algorithm:
        - a new tree is always inserted at the leafs level, so first, lookup
          the appropriate leaf, the insert the key.
        - if this causes an overflow (ie. the node has more keys than the rank)
          which leads to a node split.
        - to split a node, find the median value of all values in the node,
          insert that median into the parent node, create two new nodes, with
          keys left and right of the median, and fix the parrent pointers to
          point to the two new nodes.
        - this may cause the parrent o overflow, in which case it must be split
          also. This recurses up until there is no more parent that needs
          splitting.

        Returns:
            object, instance of src.btree.BTreeNode, the
        """
        # Find the leaf node where to do the insertion.
        if not self.is_leaf():
            insert_point = self.get_position(key)
            return self.refs[insert_point].insert(key, value)

        # Located a leaf node, so insert the (key, value) pair.
        insert_point = self.get_position(key)
        self.keys.insert(insert_point, key)
        self.values.insert(insert_point, value)

        if self.is_full():
            self.split()

        return self

    def split(self):
        """ Splits the node into two nodes.

        The current node, keeps the left keys, the new sibling keeps the right
        keys and the parent gets the median key.

        If the parent overflows injecting the median, it is split as well, and
        so on and so forth.

        If the node being split is a root, a new root is created and pointer
        wired correctly.

        Args:
            other: object, instance of src.btree.BTree, the other node to merge with this one.

        Return:
            object, instance of src.btree.BTree either the current node or the new root.
        """
        pos_median = len(self.keys)/2
        key_median = self.keys[pos_median]
        value_median = self.values[pos_median]
        keys_left = self.keys[:pos_median]
        keys_right = self.keys[pos_median+1:]
        values_left = self.values[:pos_median]
        values_right = self.values[pos_median+1:]
        if self.is_leaf():
            refs_left = []
            refs_right = []
        else:
            refs_left = self.refs[:pos_median]
            refs_right = self.refs[pos_median+1:]

        # Update the current node.
        self.keys = keys_left
        self.values = values_left
        self.refs = refs_left

        # Create a new sibling with the right data.
        sibling = BTreeNode(self.m)
        sibling.parent = self.parent
        sibling.keys = keys_right
        sibling.values = values_right
        sibling.refs = refs_right
        for ref in sibling.refs:
            ref.parent = sibling

        # If the current node is root, we need to create a new root.
        if self.is_root():
            new_root = BTreeNode(self.m)
            new_root.keys = [key_median]
            new_root.values = [value_median]
            new_root.refs = [self, sibling]
            self.parent = new_root
            sibling.parent = new_root
        else:
            index = self.parent.refs.index(self)
            self.parent.keys.insert(index+1, key_median)
            self.parent.values.insert(index+1, value_median)
            self.parent.refs.insert(index+1, sibling)

            if self.parent.is_full():
                self.parent.split()

    def lookup(self, key):
        """ Find the first value in keys larger than input key.

        If the values is not present in the current node, then recurse to the
        appropriate child node.

        Args:
            key: any, the key we lookup the corresponding value.

        Returns:
            any, the appropriate value corresponding to the given key
            None, if the key is not present.
        """
        k = self.get_position(key)

        if self.keys[k] == key:
            return node.values[k]

        # Lookup in the child node.
        if self.refs[k+1] == None:
            return None
        return self.refs[k+1].lookup(key)

    def traverse(self, recursive=False):
        """ Traverses all values of the node or the entire subtree.

        Args:
            recursive: bool, if True then this method traverses aver the entire tree.

        Returns:
            list, of keys in the node (or the entire subtree)
        """
        out = []
        for i in range(len(self.keys)):
            if recursive == True and self.refs[i] != None:
                out.extend(self.refs[i].traverse(recursive=True))
            out.append[self.values[i]]
        if recursive == True:
            out.extend(self.refs[i+1].traverse(recursive=True))
        return out

    def delete(self, value):
        """ Removes value from the data structure."""
        pass

    def get_max(self):
        pass

    def get_min(self):
        pass

    def predecessor(self, key):
        pass

    def successor(self, key):
        pass

    def range_query(self, start, end):
        pass

    def select(self, index):
        pass

    def rank(self, key):
        pass

    # HELPERS

    def is_full(self):
        """ Whether or not this BTree node is full or empty. """
        return len(self.keys) > self.m

    def is_leaf(self):
        """ A node is a leaf when it has no children references. """
        return len(self.refs) == 0

    def is_root(self):
        """ A node is root only if it has no parent. """
        return self.parent == None

    def get_position(self, key):
        """ Method figures out which position in the keys list does key belong to.

        Finds and returns the first key that is greater than or equal to key.
        """
        return bisect.bisect_left(self.keys, key)
