# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

def is_ballanced(node):
    """ 4.4 Check Balanced: Implement a function to check if a binary tree is
    balanced. For the purposes of this question, a balanced tree is defined to
    be a tree such that the heights of the two subtrees of any node never
    differ by more than one
    """
    def max_and_min_heights(node):
        if len(self.children) == 0: # is leaf
            return (0, 0)
        else:
            max_h_p = float('-inf')
            min_h_p = float('inf')
            for child in self.children:
                (max_h_c, min_h_c) = max_and_min_heights(child)
                max_h_p = max(max_h_p, max_h_c)
                min_h_p = max(min_h_p, min_h_c)
            return (max_h_p, min_h_p)

    (max_h, min_h) = max_and_min_heights(node)
    return max_h <= min_h + 1

class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.adjacent = [] # :Array<Vertex>

def is_route(src, dest):
    """ 4.4 Check Balanced: Implement a function to check if a binary tree is
    balanced. For the purposes of this question, a balanced tree is defined to
    be a tree such that the heights of the two subtrees of any node never differ
    by more than one
    """
    def get_reachable_vertices(root):
        # DFS
        stack = [root]
        visited_keys = set([])
        while len(stack) != 0:
            node = stack.pop()
            if node.key in visited_keys:
                continue
            visited_keys.add(node.key)
            for n in node.adjacent:
                if n.key not in visited_keys:
                    stack.append(n)

    vertices = get_reachable_vertices(src)
    return dest in src
