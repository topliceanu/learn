# -*- coding: utf-8 -*-

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
        self.adjacent = [] # :Array<Vertex>
        self.value = None

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

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
    """
    def visit(visited, src):
        visited.add(src.key)
        for adjacent in src.adjacent:
            if adjacent.key not in visited: # O(1)
                visit(visited, adjacent)

    reachable = visit(set([]), src)
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
        middle = right + left / 2
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

def successor(root):
    """ 4.6 Successor: Write an algorithm to find the "next" node
    (i.e., in-order successor) of a given node in a binary search tree.
    You may assume that each node has a link to its parent.
    """
    pass

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
        dependent_on.adjacent.append(dependent_by)

    # topological sort on the input.
    current_label = len(vertices) - 1
    visited = set([])

    global current_label
    global visited

    def dfs(vertex):
        if vertex in visited:
            return
        visited.add(vertex)
        for v in vertex.adjacent:
            dfs(v)
        global current_label
        vertex.value = current_label
        current_label -= 1

    for v in vertices:
        dfs(vertices[v])

    # extract the output
    out = [None] * len(vertices)
    for _, v in vertices.items():
        out[v.value] = v.key
    return out

