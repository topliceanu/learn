# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/symmetric-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rec_is_symmetric(node1, node2):
    if node1 == None and node2 == None:
        return True
    if node1 == None or node2 == None:
        return False
    return node1.val == node2.val and \
        rec_is_symmetric(node1.left, node2.right) and \
        rec_is_symmetric(node1.right, node2.left)

def is_symmetric(tree):
    return rec_is_symmetric(tree, tree)
