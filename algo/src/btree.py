# -*- coding: utf-8 -*-

from src.ballanced_binary_search_tree import BST


class BTree(BST):
    """ Implements a BTree data structure.

    Args:
        m: int, the order of the b-tree. Every node has at most m children and
            every leaf has at least m/2 keys.

    See: http://en.wikipedia.org/wiki/B-tree
    """

    def __init__(self, m):
        self.m = m

