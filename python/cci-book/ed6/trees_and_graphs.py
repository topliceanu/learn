# -*- coding: utf-8 -*-

import random

class Vertex(object):
    """ Graph node.
    Concepts:
    edge - link between two nodes
    node or vertex - an object in the graph
    adjacent vertices - where there is an edge between them
    neighbours - list of vertices reachable from a source vertex
    """
    def __init__(self, key):
        self.key = key
        self.adjacent = set([]) # :Set<Vertex>
        self.value = None

class TreeNode(object):
    def __init__(self, value, children=[]):
        self.value = value
        self.parent = None
        self.children = children
        for ch in self.children:
            ch.parent = self
    def __getitem__(self, index):
        return self.children[index]

class BinaryTreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.parent = None
        self.left = left
        self.right = right
        if left != None:
            left.parent = self
        if right != None:
            right.parent = self

class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def is_route_between_nodes(src, dest):
    """ 4.1 Route Between Nodes: Given a directed graph, design an algorithm to
    find out whether there is a route between two nodes.
    Args:
        src, dest: Vertex instances
    Returns:
        bool
    Solution: Use BFS to collect all reachable nodes from the given source node.
    """
    def visit(visited, src):
        visited.add(src.key)
        for adjacent in src.adjacent:
            if adjacent.key not in visited: # O(1)
                visit(visited, adjacent)

    reachable = set([])
    visit(reachable, src)
    return dest.key in reachable

def minimal_tree(arr):
    """ 4.2 Minimal Tree: Given a sorted (increasing order) array with unique
    integer elements, write an algorithm to create a binary search tree with
    minimal height.
    """
    def build_minimal_tree(arr, left, right):
        if left > right:
            return None
        if left == right:
            return BinaryTreeNode(arr[left])
        middle = (right + left) / 2
        left_node = build_minimal_tree(arr, left, middle - 1)
        right_node = build_minimal_tree(arr, middle + 1, right)
        root = BinaryTreeNode(arr[middle])
        if left_node:
            root.left = left_node
            left_node.parent = root
        if right_node:
            root.right = right_node
            right_node.parent = root
        return root

    return build_minimal_tree(arr, 0, len(arr) - 1)

def list_of_depths(root):
    """ 4.3 List of Depths: Given a binary tree, design an algorithm which
    creates a linked list of all the nodes at each depth (e.g., if you have
    a tree with depth D, you'll have D linked lists).

    FIXME: the lists for each level are in reverse order.
    """
    def link_nodes(acc, node, depth):
        if node == None:
            return
        if depth not in acc:
            acc[depth] = LinkedListNode(node)
        else:
            head = LinkedListNode(node)
            head.next = acc[depth]
            acc[depth] = head
        link_nodes(acc, node.left, depth + 1)
        link_nodes(acc, node.right, depth + 1)

    lists = {}
    link_nodes(lists, root, 0)
    return lists

def is_balanced(node):
    """ 4.4 Check Balanced: Implement a function to check if a binary tree is
    balanced. For the purposes of this question, a balanced tree is defined to
    be a tree such that the heights of the two subtrees of any node never
    differ by more than one
    """
    def max_and_min_heights(node):
        if node == None: # reached a leaf
            return (0, 0)
        else:
            max_left, min_left = max_and_min_heights(node.left)
            max_right, min_right = max_and_min_heights(node.right)
            return (max(max_left, max_right) + 1, min(min_left, min_right) + 1)

    (max_h, min_h) = max_and_min_heights(node)
    return max_h <= min_h + 1

def is_bst(node):
    """ 4.5 Validate BST: Implement a function to check if a binary tree
    is a binary search tree.
    """
    if node == None:
        return True
    if node.left != None and node.left.value > node.value:
        return False
    if node.right != None and node.right.value <= node.value:
        return False
    if not is_bst(node.left):
        return False
    if not is_bst(node.right):
        return False
    return True

def successor(node):
    """ 4.6 Successor: Write an algorithm to find the "next" node
    (i.e., in-order successor) of a given node in a binary search tree.
    You may assume that each node has a link to its parent.
    """
    def get_min(node):
        if node.left != None:
            return get_min(node.left)
        return node

    if node.right != None:
        return get_min(node.right)
    while node.parent != None:
        if node.parent.left == node:
            return node.parent
        node = node.parent
    return None

def build_order(projects, dependencies):
    """ 4.7 Build Order: You are given a list of projects and a list of
    dependencies (which is a list of pairs of projects, where the second
    project is dependent on the first project). All of a project's
    dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there
    is no valid build order, return an error.

    Example
    Input:
        projects: a, b, c, d, e, f
        dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
    Output: f, e, a, b, d, c

    Args:
        projects, list of chars, project ids
        dependencies, list of pairs where each snd depends on fst.
    Returns:
        list of projects in order of completion

    Solution: canonical problem for topological sort!
    """
    # process the input to build the graph data structure
    vertices = {}
    for project in projects:
        vertices[project] = Vertex(project)
    for dep in dependencies:
        dependent_on = vertices[dep[0]]
        dependent_by = vertices[dep[1]]
        dependent_on.adjacent.add(dependent_by)

    # topological sort on the input.
    def dfs(vertex, visited, output):
        if vertex in visited:
            return
        visited.add(vertex)
        for v in vertex.adjacent:
            dfs(v, visited, output)
        output.insert(0, vertex)

    visited = set([])
    output = []
    for v in vertices:
        dfs(vertices[v], visited, output)

    # process the output
    return [n.key for n in output]

def first_common_ancestor(node1, node2):
    """ 4.8 First Common Ancestor: Design an algorithm and write code to find
    the first common ancestor of two nodes in a binary tree.
    Avoid storing additional nodes in a data structure.
    NOTE: This is not necessarily a binary search tree.

    Complexity: O(n) in time, O(1) in space
    We can do: O(n) in time and O(n) in space

    Args:
        node1, node: TreeNode in the same tree
    Returns:
        TreeNode
    """
    def find_in_subtree(root, other):
        if root == None:
            return False
        if root == other:
            return True
        for ch in root.children:
            if find_in_subtree(ch, other) == True:
                return True
        return False

    def find_in_upper_tree(node, other):
        if node.parent == None:
            return None
        if node.parent == other:
            return node.parent
        for ch in node.parent.children:
            if ch != node and find_in_subtree(ch, other):
                return node.parent
        return find_in_upper_tree(node.parent, other)

    # if node2 is in node1's subtree, then return node1
    if find_in_subtree(node1, node2):
        return node1

    # recursively check parent nodes and the other subtrees for the other node
    # until the root is reached.
    return find_in_upper_tree(node1, node2)

def bst_sequence(root):
    """ 4.9 BST Sequences: A binary search tree was created by traversing
    through an array from left to right and inserting each element.
    Given a binary search tree with distinct elements, print all possible
    arrays that could have led to this tree.
    Time complexity: O(n)

    The idea is that the root always comes first, this determines what comes to
    the left and right. Either child has to be next after the root in the array,
    the other one can be anywhere.
    """
    def combine(prefix, left, right):
        if len(left) == 0 or len(right) == 0:
            return [ prefix[:] + left + right ]

        lhead, ltail = left[0], left[1:]
        rhead, rtail = right[0], right[1:]

        return combine(prefix[:] + [lhead], ltail, right) + \
               combine(prefix[:] + [rhead], left, rtail)

    def traverse(node):
        if node == None:
            return []
        left = traverse(node.left)
        right = traverse(node.right)
        if len(left) == 0:
            return combine([node.value], [], right)
        if len(right) == 0:
            return combine([node.value], left, [])
        out = []
        for l in left:
            for r in right:
                out = out + combine([node.value], l, r)
        return out

    return traverse(root)

def check_subtree(t1, t2):
    """ 4.1 O Check Subtree: T1 and T2 are two very large binary trees, with
    T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree
    of T1.

    A tree T2 is a subtree of T1 if there exists a node n in T1 such that the
    subtree of n is identical to T2. That is, if you cut off the tree at node n,
    the two trees would be identical.

    Args:
        t1, t2: BinaryTreeNode
    Returns:
        bool
    """
    def traverse(haystack, needle):
        if haystack == None and needle == None:
            return True
        if haystack == None or needle == None:
            return False
        if haystack.value == needle.value and match(haystack, needle):
            return True
        return traverse(haystack.left, needle) or \
            traverse(haystack.right, needle)

    def match(haystack, needle):
        if haystack == None or needle == None:
            return needle == haystack
        if haystack.value != needle.value:
            return False
        return match(haystack.left, needle.left) and \
               match(haystack.right, needle.right)

    if t2 == None:
        return True
    return traverse(t1, t2)

def random_node(root):
    """ 4.11 Random Node: You are implementing a binary search tree class from scratch
    which, in addition to insert, find, and delete, has a method getRandomNode()
    which returns a random node from the tree.
    All nodes should be equally likely to be chosen.
    Design and implement an algorithm for getRandomNode, and explain how you
    would implement the rest of the methods.

    Args:
        root, TreeNode
    """

    def size(node):
        if node == None:
            return 0
        return 1 + size(node.left) + size(node.right)

    def find(node, index):
        if node == None:
            return None
        lsize = size(node.left)
        if index == lsize:
            return node
        if index > lsize:
            return find(node.right, index - lsize - 1)
        else:
            return find(node.left, index)

    tree_size = size(root)
    rnd_idx = random.randrange(0, tree_size)
    return find(root, rnd_idx)

def path_with_sums(root, total):
    """ 4.12 Paths with Sum: You are given a binary tree in which each node
    contains an integer value (which might be positive or negative).
    Design an algorithm to count the number of paths that sum to a given value.
    The path does not need to start or end at the root or a leaf, but it must
    go downwards (traveling only from parent nodes to child nodes).
    """

    def attach_sums(node, total):
        """ Replace each node's value with a pair: first is the original
        value, second is the sum from root to the node.
        """
        if node == None:
            return
        new_total = node.value + total
        node.value = (node.value, new_total)
        attach_sums(node.left, new_total)
        attach_sums(node.right, new_total)

    def traverse(node, total, mapping):
        if node == None:
            return 0
        (value, sum_from_root) = node.value

        if sum_from_root not in mapping:
            mapping[sum_from_root] = 0
        mapping[sum_from_root] += 1

        diff_total = sum_from_root - total
        res = 0
        if diff_total in mapping:
            res += mapping[diff_total]
        res += traverse(node.left, total, mapping)
        res += traverse(node.right, total, mapping)

        mapping[sum_from_root] -= 1
        return res

    attach_sums(root, 0)
    return traverse(root, total, {})
