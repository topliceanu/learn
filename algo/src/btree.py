# -*- coding: utf-8 -*-

import bisect

from src.binary_search_tree import BST


# TODO implement [Mond&Raz, 1985] to support a single pass-down.

class Btree(object):
    """ Acts as a facade to the root node of the BTree.

    Attrs:
        root: object, instance of src.btree.BTreeNode
    """

    def __init__(self, m):
        self.root = BTreeNode(m)

    @classmethod
    def build(cls, data, m):
        """ Builds a new BTree given a dictionary of (key, value) pairs.

        The method used is called "bulkloading

        Args:
            data: list, of tuples, format [(key, value)]
            m: int, order of the tree

        Returns:
            object, instance of src.btree.BTree
        """
        data = sorted(data, key=0) # Make sure pairs are sorted by key.
        nodes = {} # Holds nodes and they governing value as key.

        while True:
            # Split into chunks of size m
            chunks = [data[i:i+m] for i in range(0, len(data), m)]
            data = []
            for chunk in chunks:
                parent = chunk.pop()
                data.append(parent)
                node = BTreeNone(m)
                node.keys = map(lambda i: i[0], chunk)
                node.values = map(lambda i: i[0], chunk)
                nodes[parent[0]] = node



class BTreeNode(object):
    """ This class represents a node in the BTree data structure.

    Invariants for BTree of rank m:
    - every node has at most m children.
    - every non-leaf node (except for the root) has at least m/2 children.
    - the root has at least two children if not a leaf.
    - a non-leaf node with k children has k-1 keys.
    - all leave are on the same leve.

    References:
        http://www.cs.cornell.edu/courses/cs3110/2009sp/recitations/rec25.html
        https://gist.github.com/teepark/572734

    Attrs:
        m: rank fo the node, ie. you are only allowed to m children and m-1 values.
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

        Returns:
            object, instance of src.btree.BTree, the node where the value was inserted.
                which may have changed.
        """
        # Find the leaf node where to do the insertion.
        if not self.is_leaf():
            insert_point = self.get_position(key)
            return self.refs[insert_point].insert(key, value)

        # Located a leaf node, so insert the (key, value) pair.
        insert_point = self.get_position(key)
        self.keys.insert(insert_point, key)
        self.values.insert(insert_point, value)

        if not self.is_full():
            return self

        self.split()
        if self.parent == None:
            return self
        return self.parent.merge(self)

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

        if self.refs[k] == None:
            return None

        return self.refs[k].lookup(key)

    def traverse(self, recursive=False):
        """ Traverses all values of the node or the entire subtree.

        Args:
            recursive: bool, if True then this method traverses aver the entire tree.

        Returns:
            list, of keys in the node (or the entire subtree)
        """
        out = []
        for i in len(self.values)+1:
            if recursive == True and self.refs[i] != None:
                out.extend(self.refs[i].traverse(recursive=True))
            # When processing the last reference i+1, the value i was already added.
            if i < len(self.values):
                out.append[self.values[i]]
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
        pass

    def get_position(self, key):
        """ Method figures out which position in the keys list does key belong to. """
        return bisect.bisect(self.keys, key)

    def split(self):
        """ This method extracts two children from the current node.

        The current node remains with only one value, the median of the keys in
        the old set, while the two children contain keys left and right of the
        median.
        """
        pos_median = len(self.keys)/2
        keys_left = self.keys[:pos_median]
        keys_right = self.keys[pos_median+1:]
        values_left = self.values[:pos_median]
        values_right = self.values[pos_median+1:]

        left = BTree(self.m)
        left.parent = self
        left.keys = keys_left
        left.values = values_left

        right = BTree(self.m)
        right.parent = self
        right.keys = keys_right
        right.values = values_right

        self.keys = [self.keys[pos_median]]
        self.values = [self.values[pos_median]]
        self.refs = [left, right]

    def merge(self, child):
        """ Merges the current node with one of its children.

        This method merges keys and values, maintaining the sorted order. The
        references are also correctly inserted and merged.

        If the node overflows after the merge, it is split and merged
        recursively with it's parent.

        Args:
            other: object, instance of src.btree.BTree, the other node to merge with this one.

        Return:
            object, instance of src.btree.BTree either the current node or the new root.
        """
        for index, key in enumerate(other.keys):
            insert_point = self.get_position(key)
            self.keys.insert(insert_position, key)
            self.values.insert(insert_position, other.values[index])
            self.refs.insert(insert_position, other.refs[index])

        if not self.is_full():
            return self

        self.split()
        if self.is_root():
            return self
        else:
            self.parent.merge(self)
