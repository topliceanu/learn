# -*- coding: utf-8 -*-

from src.binary_search_tree import BST


class BTreeNode(object):
    """ A node in a btree structure.

    Args:
        m: rank fo the  node
        parent: object, pointer to the parent node of this node.
        keys: list, of keys stored in this node.
        children: list, pointers to other nodes or None, such that for each
            pair of consecutive keys there is a corresponding child node who's
            keys arein that interval.
    """

    def __init__(self, m):
        self.parent = None
        self.keys = [None for i in range(m-1)]
        self.children = [None for i in range(m)]


class BTree(BST):
    """ Implements a BTree data structure.

    Invariants for BTree of rank m:
    - any path from root to None must have the same height.
    - if a node contains max m children and it contains m-1 keys
    (determining m intervals for children).
    - each node (except for the root) is at least half full (at least m/2 keys)
    - the elements in a subtree have keys between the smallest and largest key
    in the parent of the subtree.
    - the root has at least two children if it's not a leaf.

    Args:
        m: int, the order of the b-tree (ie. the max number of children a node
            can have)

    See: http://www.cs.cornell.edu/courses/cs3110/2009sp/recitations/rec25.html
    Also: https://gist.github.com/teepark/572734
    """

    def __init__(self, m):
        self.m = m
        self.root = BTreeNode()

    def insert(self, value):
        pass

    def lookup(self, value):
        pass

    def delete(self, value):
        """ Removes value from the data structure."""
        pass

    def get_max(self):
        pass

    def get_min(self):
        pass

    def range_query(self, start, end):
        pass

    def list_sorted(self):
        pass

    # Utility methods
