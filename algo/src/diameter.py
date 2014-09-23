# -*- coding: utf8 -*-

from src.ballanced_binary_search_tree import PARENT, KEY, LEFT, RIGHT


def depth(node):
    if node is None:
        return 0
    left = 1 + depth(node[LEFT])
    right = 1 + depth(node[RIGHT])
    return max(left, right)

def diameter(root):
    left = depth(root[LEFT])
    right = depth(root[RIGHT])
    return left + right + 1
