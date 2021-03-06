# -*- coding: utf-8 -*-

import unittest

from trees_and_graphs import Vertex, BinaryTreeNode, TreeNode, LinkedListNode, \
    is_route_between_nodes, minimal_tree, list_of_depths, is_balanced, is_bst, \
    successor, build_order, first_common_ancestor, bst_sequence, check_subtree, \
    random_node, path_with_sums

class TestTreesAndGraphs(unittest.TestCase):
    def test_is_route_between_nodes(self):
        graph = make_graph([(1, 2), (2, 3), (1, 3), (4, 5)], [6], directed=False)
        tests = [
           (1, 3, True),
           (1, 4, False),
           (1, 6, False),
        ]
        for test in tests:
            src = graph[test[0]]
            dest = graph[test[1]]
            actual = is_route_between_nodes(src, dest)
            expected = test[2]
            self.assertEqual(actual, expected, 'test={} failed with actual={}'.format(test, actual))

    def test_minimal_tree(self):
        tests = [
                ([1, 2, 3, 4, 5, 6], 3)
            ]
        for test in tests:
            tree = minimal_tree(test[0])
            actual = binary_tree_height(tree)
            expected = test[1]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))

    def test_list_of_depths(self):
        def extract_vals_from_nodes(nodes):
            return [i.value for i in nodes]
        tests = [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [[5], [7, 2], [8, 6, 3, 1], [9, 4]])
        ]
        for test in tests:
            tree = minimal_tree(test[0])
            actual = list_of_depths(tree)
            expected = test[1]
            for level in range(len(expected)):
                actual_list = extract_vals_from_nodes(linked_list_to_list(actual[level]))
                expected_list = expected[level]
                self.assertEqual(actual_list, expected_list,
                    'failed test={} on level={} with actual={} and expected={}'
                    .format(test, level, actual_list, expected_list))

    def test_is_balanced(self):
        tests = [
            (BinaryTreeNode(1, BinaryTreeNode(2, None, None), BinaryTreeNode(3, None, None)), True),
            (BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(3, None, None), None), None), False),
        ]
        for test in tests:
            actual = is_balanced(test[0])
            expected = test[1]
            self.assertEqual(actual, expected,
                    'failed test={} with actual={}'
                    .format(test, actual))

    def test_is_bst(self):
        tests = [
            # Only if input array is sorted, the resulting tree will be BST!
            ([1,2,3,4,5,6,7], True),
            ([9,2,3,10,5,6,7], False),
        ]
        for test in tests:
            tree = minimal_tree(test[0])
            actual = is_bst(tree)
            expected = test[1]
            self.assertEqual(actual, expected,
                    'failed test={} with actual={}'
                    .format(test, actual))

    def test_successor(self):
        tree = minimal_tree([1,2,3,4,5,6,7,8])
        tests = [
            (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)
        ]
        for test in tests:
            actual = successor(binary_tree_find(tree, test[0]))
            expected = binary_tree_find(tree, test[1])
            self.assertEqual(actual, expected,
                    'failed test={} with actual={}'
                    .format(test, actual))

    def test_build_order(self):
        tests = [
            (['a', 'b', 'c', 'd', 'e', 'f'],
             [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')],
             ['f', 'e', 'b', 'a', 'd', 'c']),
        ]
        for test in tests:
            actual = build_order(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected,
                    'failed test={} with actual={}'
                    .format(test, actual))

    def test_find_first_common_ancestor(self):
        tree = TreeNode('a', [
            TreeNode('b', [
                TreeNode('d', []),
                TreeNode('e', []),
            ]),
            TreeNode('c', [
                TreeNode('f', []),
                TreeNode('g', []),
            ]),
        ])
        tests = [
            (tree, tree, tree), # 'a' and 'a' -> 'a'
            (tree[0], tree, tree), # 'd' and 'a' -> 'a'
            (tree, tree[0][0], tree), # 'a' and 'd' -> 'a'
            (tree[0][1], tree[0], tree[0]), # 'e' and 'b' -> 'b'
            (tree[0][1], tree[1], tree), # 'e' and 'c' -> 'a'
            (tree[0][0], tree[1][1], tree), # 'd' and 'g' -> 'a'
        ]
        for test in tests:
            actual = first_common_ancestor(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected,
                    'failed test={} with actual={}'
                    .format(test, actual))

    def test_bst_sequence(self):
        tests = [
            (
                BinaryTreeNode(2, BinaryTreeNode(1), BinaryTreeNode(3)),
                [[2, 1, 3], [2, 3, 1]]
            ),
            (
                BinaryTreeNode(4, BinaryTreeNode(2, BinaryTreeNode(1), BinaryTreeNode(3)), BinaryTreeNode(5)),
                [
                    [4, 2, 1, 3, 5],
                    [4, 2, 1, 5, 3],
                    [4, 2, 5, 1, 3],
                    [4, 5, 2, 1, 3],
                    [4, 2, 3, 1, 5],
                    [4, 2, 3, 5, 1],
                    [4, 2, 5, 3, 1],
                    [4, 5, 2, 3, 1]
                ]
            )
        ]
        for test in tests:
            actual = bst_sequence(test[0])
            expected = test[1]
            for a in actual:
                self.assertIn(a, expected, 'expected {} to be in {}'.format(a, expected))

    def test_check_subtree(self):
        tree = BinaryTreeNode(1,
                    BinaryTreeNode(2,
                        BinaryTreeNode(3),
                        BinaryTreeNode(4)),
                    BinaryTreeNode(5,
                        BinaryTreeNode(6),
                        BinaryTreeNode(7)))
        tests = [
            (tree, None, True),
            (None, None, True),
            (tree, tree, True),
            (tree, tree.left, True), # '2' is a subtree
            (tree, tree.left.left, True), # '3' is a subtree
        ]
        for test in tests:
            actual = check_subtree(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected,
                    'failed test={} with actual={}'
                    .format(test, actual))

    def test_random_node(self):
        values = [1,2,3,4,5,6,7,8]
        tree = minimal_tree(values)
        actual = random_node(tree)
        self.assertNotEqual(actual, None, 'should not be none')
        self.assertIn(actual.value, values,
                'value {} does not exist in {}'.format(actual.value, values))

    def test_path_with_sums(self):
        tree = BinaryTreeNode(10,
                BinaryTreeNode(5,
                    BinaryTreeNode(3,
                        BinaryTreeNode(3),
                        BinaryTreeNode(-2)),
                    BinaryTreeNode(1,
                        None,
                        BinaryTreeNode(2))),
                BinaryTreeNode(-3,
                    None,
                    BinaryTreeNode(11)))
        actual = path_with_sums(tree, 8)
        expected = 3
        self.assertEqual(actual, expected, 'should find the correct number of sums')

# HELPERS

def make_graph(edges, extra_vertices, directed=False):
    graph = {}
    for edge in edges:
        skey, dkey = edge[0], edge[1]
        if skey not in graph:
            graph[skey] = Vertex(skey)
        if dkey not in graph:
            graph[dkey] = Vertex(dkey)
        graph[skey].adjacent.add(graph[dkey])
        if not directed:
            graph[dkey].adjacent.add(graph[skey])
    for vkey in extra_vertices:
        if vkey not in graph:
            graph[vkey] = Vertex(vkey)
    return graph

def binary_tree_height(root):
    if root == None:
        return 0
    return max(binary_tree_height(root.left), binary_tree_height(root.right)) + 1

def binary_tree_find(root):
    def printWithPrefix(prefix, root):
        if root == None:
            return
        print(prefix + str(root.value))
        printWithPrefix(prefix + "  ", root.left)
        printWithPrefix(prefix + "  ", root.right)
    printWithPrefix("", root)

def binary_tree_find(root, value):
    if root == None:
        return None
    if root.value == value:
        return root
    if root.value > value:
        return binary_tree_find(root.left, value)
    return binary_tree_find(root.right, value)

def linked_list_to_list(node):
    if node == None:
        return []
    rest = linked_list_to_list(node.next)
    rest.insert(0, node.value)
    return rest


#class TestRecapGraphAlgorithsm(unittest.TestCase):
#    def test_build_order(self):
#        tests = [
#            {
#                "projects": ['a', 'b', 'c', 'd', 'e', 'f'],
#                "dependencies": [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')],
#                "output": ['f', 'e', 'b', 'a', 'd', 'c'],
#            }
#        ]
#        for test in tests:
#            actual = build_order(test["projects"], test["dependencies"])
#            expected = test["output"]
#            self.assertEqual(actual, expected, "failed test={} with actual={}".format(test, actual))
#
#    def test_bst_sequence(self):
#        tests = [
#            {
#                "root": build_bst([2, 1, 3]),
#                "combinations": [
#                    [2, 1, 3],
#                    [2, 3, 1],
#                ]
#            },
#        ]
