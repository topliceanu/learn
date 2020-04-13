import unittest

from src.binary_search_tree import BST, PARENT, KEY, LEFT, RIGHT, SIZE, \
    BinarySearchTreeNode


class TestBinarySearchTreeNode(unittest.TestCase):

    def test_insert(self):
        bst = BinarySearchTreeNode('x', 1)
        y_node = bst.insert('y', 2)
        u_node = bst.insert('u', 3)

        self.assertEqual(bst.key, 'x', 'root is the correct value')
        self.assertEqual(bst.left.key, 'u', 'right node is correct')
        self.assertEqual(bst.right.key, 'y', 'left node is correct')

        self.assertEqual(bst.parent, None, 'root has no parent')
        self.assertEqual(bst.left.parent, bst, 'left has root as parent')
        self.assertEqual(bst.right.parent, bst, 'right has root as parent')

        self.assertEqual(bst.size, 3, 'should update correct size of a node')

        actual = bst.insert('v', 4)
        self.assertEqual(actual.key, 'v', 'should insert with correct key')
        self.assertEqual(actual.value, 4, 'should insert with correct value')
        self.assertEqual(actual.parent, u_node, 'should have the correct parent')

    def test_lookup(self):
        bst = BinarySearchTreeNode('y', 1)
        bst.insert('x', 2)
        bst.insert('z', 3)

        actual = bst.lookup('x')
        expected = bst.left
        self.assertEqual(actual, expected, 'should return the entire object')

        actual = bst.lookup('t')
        self.assertIsNone(actual, 'should not find node with key t')

    def test_get_min(self):
        bst = BinarySearchTreeNode('y', 1)
        bst.insert('x', 2)
        bst.insert('z', 3)

        expected = bst.get_min()
        actual = bst.left
        self.assertEqual(actual, expected, 'produced correct min node')
        self.assertEqual(actual.key, 'x', 'produced correct min node key')

    def test_get_max(self):
        bst = BinarySearchTreeNode('y', 1)
        bst.insert('x', 2)
        bst.insert('z', 3)

        expected = bst.get_max()
        actual = bst.right
        self.assertEqual(actual, expected, 'produced correct max node')
        self.assertEqual(actual.key, 'z', 'produced correct max node key')

    def test_predecessor(self):
        """ Following tree structure:
                (x)
               /   \
             (t)   (y)
               \      \
              (u)     (z)
                \
                (v)
        """
        x_node = BinarySearchTreeNode('x', 1)
        y_node = x_node.insert('y', 2)
        z_node = x_node.insert('z', 3)
        t_node = x_node.insert('t', 4)
        u_node = x_node.insert('u', 5)
        v_node = x_node.insert('v', 6)

        self.assertEqual(x_node.predecessor(), v_node, 'predecessor of x is u')
        self.assertEqual(y_node.predecessor(), x_node, 'predecessor of y is x')
        self.assertEqual(z_node.predecessor(), y_node, 'predecessor of z is y')
        self.assertEqual(t_node.predecessor(), None, 't has no predecessor')
        self.assertEqual(u_node.predecessor(), t_node, 'predecessor of u is t')
        self.assertEqual(v_node.predecessor(), u_node, 'predecessor of v is u')

    def test_successor(self):
        """ Following tree structure:
                (x)
               /   \
             (t)   (y)
               \      \
              (u)     (z)
                \
                (v)
        """
        x_node = BinarySearchTreeNode('x', 1)
        y_node = x_node.insert('y', 2)
        z_node = x_node.insert('z', 3)
        t_node = x_node.insert('t', 4)
        u_node = x_node.insert('u', 5)
        v_node = x_node.insert('v', 6)

        self.assertEqual(x_node.successor(), y_node, 'successor of x is y')
        self.assertEqual(y_node.successor(), z_node, 'successor of y is z')
        self.assertEqual(z_node.successor(), None, 'z has no successor')
        self.assertEqual(t_node.successor(), u_node, 'successor of t is u')
        self.assertEqual(u_node.successor(), v_node, 'successor of u is v')
        self.assertEqual(v_node.successor(), x_node, 'successor of v is x')

    def test_rank(self):
        """ Following tree structure:
                (x)
               /   \
             (t)   (y)
            /  \      \
          (r)  (u)    (z)
          / \    \
        (q) (s)  (v)

        This will yield: [q, r, s, t, u, v, x, y, z]
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        self.assertEqual(q_node.rank(), 0, 'q is on index 0')
        self.assertEqual(r_node.rank(), 1, 'r is on index 1')
        self.assertEqual(s_node.rank(), 2, 's is on index 2')
        self.assertEqual(t_node.rank(), 3, 't is on index 3')
        self.assertEqual(u_node.rank(), 4, 'u is on index 4')
        self.assertEqual(v_node.rank(), 5, 'v is on index 5')
        self.assertEqual(x_node.rank(), 6, 'x is on index 6')
        self.assertEqual(y_node.rank(), 7, 'y is on index 7')
        self.assertEqual(z_node.rank(), 8, 'z is on index 8')

    def test_select(self):
        """ Following tree structure:
                (x)
               /   \
             (t)   (y)
            /  \      \
          (r)  (u)    (z)
          / \    \
        (q) (s)  (v)

        This will yield: [q, r, s, t, u, v, x, y, z]
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        self.assertEqual(x_node.select(0), q_node, 'q is on index 0')
        self.assertEqual(x_node.select(1), r_node, 'r is on index 1')
        self.assertEqual(x_node.select(2), s_node, 's is on index 2')
        self.assertEqual(x_node.select(3), t_node, 't is on index 3')
        self.assertEqual(x_node.select(4), u_node, 'u is on index 4')
        self.assertEqual(x_node.select(5), v_node, 'v is on index 5')
        self.assertEqual(x_node.select(6), x_node, 'x is on index 6')
        self.assertEqual(x_node.select(7), y_node, 'y is on index 7')
        self.assertEqual(x_node.select(8), z_node, 'z is on index 8')
        self.assertEqual(x_node.select(10), None, 'there is no node on index 10')
        self.assertEqual(x_node.select(-5), None, 'there is no node on index -5')

    def test_delete(self):
        """ Following tree structure:
                (x)
               /   \
             (t)   (y)
            /  \      \
          (r)  (u)    (z)
          / \    \
        (q) (s)  (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        # Case 1: delete leaf.
        #         (x)                   (x)
        #        /   \                 /   \
        #      (t)   (y)             (t)   (y)
        #     /  \      \    =>     /  \      \
        #   (r)  (u)    (z)       (r)  (u)    (z)
        #   / \    \              / \
        # (q) (s)  (v)          (q) (s)
        v_node.delete()
        self.assertEqual(u_node.right, None, 'node u has no left child')
        self.assertEqual(v_node.parent, None, 'v was completely detached')

        # Case 2: delete internal node with one child.
        #         (x)                 (x)
        #        /   \               /   \
        #      (t)   (y)           (t)   (z)
        #     /  \     \   =>     /  \
        #   (r)  (u)   (z)      (r)  (u)
        #   / \                 / \
        # (q) (s)             (q) (s)
        y_node.delete()
        self.assertEqual(x_node.right, z_node, 'right child of x is now z')
        self.assertEqual(z_node.parent, x_node, 'parent of z is now x')
        self.assertEqual(y_node.parent, None, 'y was detached from its parent')
        self.assertEqual(y_node.right, None, 'y was completly detached from its right child')

        # Case 3, delete internal node with two children.
        #          (x)                 (x)
        #         /   \               /   \
        #       (t)   (z)           (s)   (z)
        #      /  \         =>     /  \
        #    (r)  (u)            (r)  (u)
        #   /  \                /
        # (q)  (s)            (q)
        t_node.delete()
        self.assertEqual(t_node.parent, None, 't was detached from parent')
        self.assertEqual(t_node.left, None, 't was detached from left child')
        self.assertEqual(t_node.right, None, 't was detached from right child')
        self.assertEqual(s_node.parent, x_node, 's new parent is x')
        self.assertEqual(s_node.left, r_node, 's left child is r')
        self.assertEqual(s_node.right, u_node, 's right child is u')
        self.assertEqual(r_node.right, None, 's was displaced from being right child of r')

        # Case 3, delete the root.
        #          (x)                 (u)
        #         /   \               /   \
        #       (s)   (z)           (s)   (z)
        #      /  \         =>     /
        #    (r)  (u)            (r)
        #   /                   /
        # (q)                 (q)
        x_node.delete()
        self.assertEqual(x_node.parent, None, 'root x was detached')
        self.assertEqual(x_node.left, None, 'root x was detached from left child')
        self.assertEqual(x_node.right, None, 'root x was detached from right child')
        self.assertEqual(u_node.parent, None, 'u is the new root')
        self.assertEqual(u_node.left, s_node, 'left child of root u is now s')
        self.assertEqual(u_node.right, z_node, 'right child of root us is now z')

    def test_in_order_traversal(self):
        """ Uses following tree structure:
                (x)
               /   \
             (t)   (y)
            /  \      \
          (r)  (u)    (z)
          / \    \
        (q) (s)  (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        expected = ['q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
        nodes = x_node.in_order_traversal()
        actual = map(lambda n: n.key, nodes)
        self.assertEqual(actual, expected, 'correct in-order traversal')

    def test_pre_order_traversal(self):
        """ Uses following tree structure:
                (x)
               /   \
             (t)   (y)
            /  \      \
          (r)  (u)    (z)
          / \    \
        (q) (s)  (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        expected = ['x', 't', 'r', 'q', 's', 'u', 'v', 'y', 'z']
        nodes = x_node.pre_order_traversal()
        actual = map(lambda n: n.key, nodes)
        self.assertEqual(actual, expected, 'correct pre-order traversal')

    def test_post_order_traversal(self):
        """ Uses following tree structure:
                (x)
               /   \
             (t)   (y)
            /  \      \
          (r)  (u)    (z)
          / \    \
        (q) (s)  (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        expected = ['q', 's', 'r', 'v', 'u', 't', 'z', 'y', 'x']
        nodes = x_node.post_order_traversal()
        actual = map(lambda n: n.key, nodes)
        self.assertEqual(actual, expected, 'correct pre-order traversal')

    def test_common_ancestor(self):
        """ Uses following tree structure:
                (x)
               /   \
             (t)   (y)
            /  \      \
          (r)  (u)    (z)
          / \    \
        (q) (s)  (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        self.assertEqual(t_node.common_ancestor_prime(t_node), t_node, 'both nodes are the same')
        self.assertEqual(t_node.common_ancestor_prime(v_node), t_node, 't is ancestor of v')
        self.assertEqual(v_node.common_ancestor_prime(u_node), u_node, 'u is parent of v')
        self.assertEqual(q_node.common_ancestor_prime(x_node), x_node, 'x is root')
        self.assertEqual(q_node.common_ancestor_prime(z_node), x_node, 'x is root')

    def test_common_ancestor_prime(self):
        """ Uses following tree structure:
                (x)
               /   \
             (t)   (y)
            /  \      \
          (r)  (u)    (z)
          / \    \
        (q) (s)  (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        self.assertEqual(t_node.common_ancestor_prime(t_node), t_node, 'both nodes are the same')
        self.assertEqual(t_node.common_ancestor_prime(v_node), t_node, 't is ancestor of v')
        self.assertEqual(v_node.common_ancestor_prime(u_node), u_node, 'u is parent of v')
        self.assertEqual(q_node.common_ancestor_prime(x_node), x_node, 'x is root')
        self.assertEqual(q_node.common_ancestor_prime(z_node), x_node, 'x is root')

    def test_is_identical(self):
        """ Using the following tree structure and two test candidates:
                (x)                (x)               (x)
               /   \              /   \             /   \
             (t)   (y)          (t)   (y)         (t)   (y)
            /  \      \        /  \      \       /  \      \
          (r)  (u)    (z)    (r)  (u)    (z)   (r)  (u)    (z)
          / \    \           / \    \          / \
        (q) (s)  (v)       (q) (s)  (v)      (q) (s)
             (root)            (subject1)        (subject2)
        """
        root = BinarySearchTreeNode('x')
        root.insert('y')
        root.insert('z')
        root.insert('t')
        root.insert('u')
        root.insert('v')
        root.insert('r')
        root.insert('s')
        root.insert('q')

        subject1 = BinarySearchTreeNode('x')
        subject1.insert('y')
        subject1.insert('z')
        subject1.insert('t')
        subject1.insert('u')
        subject1.insert('v')
        subject1.insert('r')
        subject1.insert('s')
        subject1.insert('q')

        self.assertTrue(root.is_identical(subject1), 'should detect identical trees')

        subject2 = BinarySearchTreeNode('x')
        subject2.insert('y')
        subject2.insert('z')
        subject2.insert('t')
        subject2.insert('u')
        subject2.insert('r')
        subject2.insert('s')
        subject2.insert('q')

        self.assertFalse(root.is_identical(subject2), 'should detect non-identical trees')

    def test_is_subtree_of(self):
        """ Using the following tree structure and two test candidates:
                (x)
               /   \                    (u)
             (t)   (y)         (r)        \
            /  \      \       /  \        (v)
          (r)  (u)    (z)   (q)  (s)        \
          / \    \                          (w)
        (q) (s)  (v)
             (root)        (subject1)  (subject2)
        """
        root = BinarySearchTreeNode('x')
        root.insert('y')
        root.insert('z')
        root.insert('t')
        root.insert('u')
        root.insert('v')
        root.insert('r')
        root.insert('s')
        root.insert('q')

        subject1 = BinarySearchTreeNode('r')
        subject1 = BinarySearchTreeNode('q')
        subject1 = BinarySearchTreeNode('s')

        self.assertTrue(subject1.is_subtree_of(root), 'should find the subtree')

        subject2 = BinarySearchTreeNode('u')
        subject2 = BinarySearchTreeNode('v')
        subject2 = BinarySearchTreeNode('w')

        self.assertFalse(subject2.is_subtree_of(root), 'should not find the subtree')

    def test_diameter(self):
        """ Using the following tree structure:
                (x)
               /   \
             (t)   (y)
            /  \      \
          (r)  (u)    (z)
          / \    \
        (q) (s)  (v)
                   \
                   (w)
        """
        root = BinarySearchTreeNode('x')
        y_node = root.insert('y')
        z_node = root.insert('z')
        t_node = root.insert('t')
        u_node = root.insert('u')
        v_node = root.insert('v')
        w_node = root.insert('w')
        r_node = root.insert('r')
        s_node = root.insert('s')
        q_node = root.insert('q')
        self.assertEqual(root.diameter(), 7, 'max diameter of this tree is 6')

    def test_is_ballanced(self):
        """ Using the following tree structure:
                (x)                  (x)
               /   \                /   \
             (t)   (y)            (t)   (y)
            /  \      \          /  \      \
          (r)  (u)    (z)      (r)  (u)    (z)
          / \    \
        (q) (s)  (v)
                   \
                   (w)
            (unballanced)         (ballanced)
        """
        unballanced = BinarySearchTreeNode('x')
        unballanced.insert('y')
        unballanced.insert('z')
        unballanced.insert('t')
        unballanced.insert('u')
        unballanced.insert('v')
        unballanced.insert('w')
        unballanced.insert('r')
        unballanced.insert('s')
        unballanced.insert('q')
        self.assertFalse(unballanced.is_ballanced(),
            'subject tree is not ballanced')

        ballanced = BinarySearchTreeNode('x')
        ballanced.insert('y')
        ballanced.insert('z')
        ballanced.insert('t')
        ballanced.insert('u')
        ballanced.insert('r')
        self.assertTrue(ballanced.is_ballanced(),
            'subject tree is ballanced')

    def test_merge(self):
        """ Given two binary search trees check if they are correctly merged:

                (y)       (a)               (c)
               /   \         \             /   \
             (x)   (z)  +    (b)    =   (a)    (y)
                                \         \    / \
                                (c)      (b) (x) (z)
              (first)     (second)        (result)
        """
        first = BinarySearchTreeNode('y')
        first.insert('x')
        first.insert('z')

        second = BinarySearchTreeNode('a')
        second.insert('b')
        second.insert('c')

        result = first.merge(second)

        self.assertEqual(result.key, 'c', 'root is c')
        self.assertEqual(result.left.key, 'a', 'left child of c is a')
        self.assertEqual(result.right.key, 'y', 'right child of c is y')
        self.assertEqual(result.left.right.key, 'b', 'right child of a is b')
        self.assertEqual(result.right.left.key, 'x', 'left child of y is x')
        self.assertEqual(result.right.right.key, 'z', 'right child of y is z')

    # Utilities

    def test_swap(self):
        """ Following tree structure is used:
                (x)
               /   \
             (t)   (y)
            /  \     \
          (r)  (u)   (z)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        r_node = x_node.insert('r')
        u_node = x_node.insert('u')

        # 1. Swap leaf and it's parent node.
        #       (x)               (x)
        #      /   \             /   \
        #    (t)   (y)   =>    (r)   (y)
        #   /  \     \        /  \     \
        # (r)  (u)   (z)    (t)  (u)   (z)
        r_node.swap(t_node)
        self.assertEqual(r_node.parent, x_node, 'x is now parent of r')
        self.assertEqual(r_node.left, t_node, 't is left child of r')
        self.assertEqual(r_node.right, u_node, 'u is left child of r')
        self.assertEqual(t_node.parent, r_node, 'r is now parent of t')
        self.assertEqual(t_node.left, None, 't has no left child')
        self.assertEqual(t_node.right, None, 't has no right child')

        # 2. Swap leaf with another middle node.
        #       (x)               (x)
        #      /   \             /   \
        #    (r)   (y)   =>    (r)   (u)
        #   /  \     \        /  \     \
        # (t)  (u)   (z)    (t)  (y)   (z)

        u_node.swap(y_node)
        self.assertEqual(u_node.parent, x_node, 'x is now parent of u')
        self.assertEqual(u_node.left, None, 'u has no left child')
        self.assertEqual(u_node.right, z_node, 'z is right child of u')
        self.assertEqual(y_node.parent, r_node, 'r is now parent of y')
        self.assertEqual(y_node.left, None, 'y has no left child')
        self.assertEqual(y_node.right, None, 'y has no right child')

        # 3. Swap leaf with another leaf.
        #       (x)               (x)
        #      /   \             /   \
        #    (r)   (u)   =>    (r)   (u)
        #   /  \     \        /  \     \
        # (t)  (y)   (z)    (z)  (y)   (t)
        t_node.swap(z_node) #
        self.assertEqual(t_node.parent, u_node, 'u is now parent of t')
        self.assertEqual(t_node.left, None, 't has no left child')
        self.assertEqual(t_node.right, None, 't has no right child')
        self.assertEqual(z_node.parent, r_node, 'r is now parent of z')
        self.assertEqual(z_node.left, None, 'y has no left child')
        self.assertEqual(z_node.right, None, 'y has no right child')

        # 3. Swap leaf with root.
        #       (x)               (z)
        #      /   \             /   \
        #    (r)   (u)   =>    (r)   (u)
        #   /  \     \        /  \     \
        # (z)  (y)   (t)    (x)  (y)   (t)
        z_node.swap(x_node)
        self.assertEqual(z_node.parent, None, 'z is now a root so no parent')
        self.assertEqual(z_node.left, r_node, 'left child of z is r')
        self.assertEqual(z_node.right, u_node, 'right child of z is u')
        self.assertEqual(x_node.parent, r_node, 'r is now parent of x')
        self.assertEqual(x_node.left, None, 'x has no left child')
        self.assertEqual(x_node.right, None, 'x has no right child')

    def test_rotate_left(self):
        """ Uses following tree structure, test rotate left between
        nodes t and u:
                    (x)                  (x)
                   /   \                /   \
                 (t)   (y)            (u)   (y)
                /  \      \   =>     /  \      \
              (r)  (u)    (z)      (t)  (v)    (z)
              / \    \             /
            (q) (s)  (v)         (r)
                                /  \
                              (q)  (s)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        t_node.rotate('left')

        self.assertEqual(u_node.parent, x_node, 'parent of u is now x')
        self.assertEqual(x_node.left, u_node, 'left child of x is u')
        self.assertEqual(u_node.left, t_node, 'left node of u is t')
        self.assertEqual(t_node.parent, u_node, 'parent of t is u')
        self.assertEqual(u_node.right, v_node, 'right node of u if v')
        self.assertEqual(v_node.parent, u_node, 'parent of v is u')
        self.assertEqual(t_node.parent, u_node, 'parent of t is u')
        self.assertEqual(t_node.left, r_node, 'left child of t is r')
        self.assertEqual(r_node.parent, t_node, 'parent node of r is t')

        # Test sizes of the newly rotated nodes
        self.assertEqual(t_node.size, 4, 't can now reach 4 nodes')
        self.assertEqual(u_node.size, 6, 'u can now reach 6 nodes')

    def test_rotate_right(self):
        """ Uses following tree structure, test rotate right between
        nodes r and t.
                    (x)                  (x)
                   /   \                /   \
                 (t)   (y)            (r)   (y)
                /  \      \   =>     /  \      \
              (r)  (u)    (z)      (q)  (t)    (z)
              / \    \                 /  \
            (q) (s)  (v)             (s)  (u)
                                            \
                                            (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        t_node.rotate('right')

        self.assertEqual(r_node.parent, x_node, 'x is parent of r')
        self.assertEqual(x_node.left, r_node, 'left child of x is r')
        self.assertEqual(r_node.left, q_node, 'q is left child of r')
        self.assertEqual(q_node.parent, r_node, 'parent of q is r')
        self.assertEqual(r_node.right, t_node, 'x is right child of r')
        self.assertEqual(t_node.parent, r_node, 'parent of r is t')
        self.assertEqual(t_node.left, s_node, 'left child of t is s')
        self.assertEqual(s_node.parent, t_node, 'new parent of s is t')
        self.assertEqual(u_node.parent, t_node, 'no change in the parent of u')

        # Test sizes of the newly rotated nodes
        self.assertEqual(t_node.size, 4, 't can now reach 4 nodes')
        self.assertEqual(r_node.size, 6, 'u can now reach 6 nodes')

    def test_depth(self):
        """ Using the following tree:
                    (x)
                   /   \
                 (t)   (y)
                /  \      \
              (r)  (u)    (z)
              / \    \
            (q) (s)  (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        self.assertEqual(x_node.depth(), 0, 'x is root so its depth is 0')
        self.assertEqual(v_node.depth(), 3, 'v is leaf with depth 3')

    def test_height(self):
        """ Using the following tree:
                    (x)
                   /   \
                 (t)   (y)
                /  \      \
              (r)  (u)    (z)
              / \    \
            (q) (s)  (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        self.assertEqual(x_node.height(), 3, 'x is root so its height is 3')
        self.assertEqual(t_node.height(), 2, 'height of t is 2')
        self.assertEqual(v_node.height(), 0, 'height of leaf v is 0')
        self.assertEqual(r_node.height(), 1, 'x is root so its height is 3')
        self.assertEqual(t_node.height(), 2, 'x is root so its height is 3')

    def test_min_depth(self):
        """ Using the following tree:
                    (x)
                   /   \
                 (t)   (y)
                /  \      \
              (r)  (u)    (z)
              / \    \
            (q) (s)  (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        self.assertEqual(x_node.min_depth(), (z_node, 2),
            'z node is the leaf with minimum depth of 2')

    def test_max_depth(self):
        """ Using the following tree:
                    (x)
                   /   \
                 (t)   (y)
                /  \      \
              (r)  (u)    (z)
              / \    \
            (q) (s)  (v)
        """
        x_node = BinarySearchTreeNode('x')
        y_node = x_node.insert('y')
        z_node = x_node.insert('z')
        t_node = x_node.insert('t')
        u_node = x_node.insert('u')
        v_node = x_node.insert('v')
        r_node = x_node.insert('r')
        s_node = x_node.insert('s')
        q_node = x_node.insert('q')

        self.assertEqual(x_node.max_depth(), (q_node, 3),
            'q node is the first leaf with maximum depth of 3')

    # Statics

    def test_from_sorted_list(self):
        """ Build the following tree:
                    (d)
                   /   \
                 (b)   (f)
                /  \   /  \
              (a) (c) (e) (g)
        """
        arr = [('a',1), ('b',2), ('c',3), ('d',4), ('e',5), ('f',6), ('g',7)]
        root = BinarySearchTreeNode.from_sorted_list(arr)

        self.assertEqual(root.key, 'd', 'd is root')
        self.assertEqual(root.left.key, 'b',  'left child of d is b')
        self.assertEqual(root.right.key, 'f', 'right child of d is f')
        self.assertEqual(root.left.left.key, 'a', 'left child of b is a')
        self.assertEqual(root.left.right.key, 'c', 'left child of b is c')
        self.assertEqual(root.right.left.key, 'e', 'left child of f is e')
        self.assertEqual(root.right.right.key, 'g', 'left child of f is e')


class TestBST(unittest.TestCase):
    """ Running examples:
                                        (5)
                                        /
            (3)                       (4)
           /   \                      /
        (1)     (5)                 (3)
          \     /                   /
          (2) (4)                 (2)
                                  /
                                (1)
    """

    def test_build(self):
        b = BST.build([3,1,2,5,4])

    def test_insert(self):
        b = BST.build([])
        actual = b.insert(3)
        expected = [None, 3, None, None, 1]
        self.assertEqual(actual, expected, 'should have inserted the '+
                                    'correct single node into the BST')

        actual = b.insert(1)
        self.assertEqual(actual[PARENT][KEY], 3, 'should be a child of 3')
        self.assertIsNone(actual[LEFT], 'should have no left child')
        self.assertIsNone(actual[RIGHT], 'should have not right child')
        self.assertEqual(actual[SIZE], 1, 'new node is a leaf')

        self.assertEqual(b.root[SIZE], 2, 'root can access 2 nodes')

    def test_search(self):
        b = BST.build([3,1,2,5,4])

        self.assertIsNotNone(b.search(3), 'should find 3 in the bst')
        self.assertIsNotNone(b.search(1), 'should find 1 in the bst')
        self.assertIsNotNone(b.search(2), 'should find 2 in the bst')
        self.assertIsNotNone(b.search(5), 'should find 5 in the bst')
        self.assertIsNotNone(b.search(4), 'should find 4 in the bst')
        self.assertIsNone(b.search(10), 'should not find 10 in the bst')

    def test_max(self):
        b = BST.build([3,1,2,5,4])

        self.assertEqual(b.get_max()[KEY], 5, 'should find the max value')

    def test_min(self):
        b = BST.build([3,1,2,5,4])

        self.assertEqual(b.get_min()[KEY], 1, 'should find the min value')

    def test_output(self):
        b = BST.build([3,1,2,5,4])

        actual = b.list_sorted()
        expected = [1,2,3,4,5]
        self.assertEqual(actual, expected, 'should list the key in order')

    def test_predecessor(self):
        b = BST.build([3,1,2,5,4])

        actual = b.predecessor(6)
        self.assertIsNone(actual, 'did not find any node with key 6')

        actual = b.predecessor(1)
        self.assertIsNone(actual, '1 is min, so no predecessor')

        actual = b.predecessor(2)
        self.assertEqual(actual[KEY], 1, 'predecessor of 2 is 1')

        actual = b.predecessor(3)
        self.assertEqual(actual[KEY], 2, 'predecessor of 3 is 2')

        actual = b.predecessor(4)
        self.assertEqual(actual[KEY], 3, 'predecessor of 4 is 3')

        actual = b.predecessor(5)
        self.assertEqual(actual[KEY], 4, 'predecessor of 4 is 3')

    def test_successor(self):
        b = BST.build([3,1,2,5,4])

        actual = b.successor(6)
        self.assertIsNone(actual, 'did not find any node with key 6')

        actual = b.successor(1)
        self.assertEqual(actual[KEY], 2, 'successor of 1 is 2')

        actual = b.successor(2)
        self.assertEqual(actual[KEY], 3, 'successor of 2 is 3')

        actual = b.successor(3)
        self.assertEqual(actual[KEY], 4, 'successor of 3 is 4')

        actual = b.successor(4)
        self.assertEqual(actual[KEY], 5, 'successor of 4 is 5')

        actual = b.successor(5)
        self.assertIsNone(actual, '5 is max of tree so no successor')

    def test_range_query(self):
        b = BST.build([3,1,2,5,4])
        actual = b.range_query(2, 4)
        expected = [2,3,4]
        self.assertEqual(actual, expected, 'should return a range of data')

    def test_delete(self):
        b = BST.build([3,1,2,5,4])

        removed = b.delete(2) # Node is a leaf.
        self.assertEqual(removed[KEY], 2, 'returns the removed node')
        self.assertIsNone(b.search(2), 'should not find 2 anymore')
        self.assertIsNone(b.search(1)[RIGHT], '1 has no more children')

        removed = b.delete(5) # Node has only one child.
        self.assertEqual(removed[KEY], 5, 'returns the removed node')
        self.assertIsNone(b.search(5), 'should have removed 5')
        self.assertEqual(b.search(4)[PARENT][KEY], 3, 'should have hoisted 4')

        removed = b.delete(3) # Node has both children.
        self.assertEqual(removed[KEY], 3, 'returns the removed node')
        self.assertIsNone(b.search(3), 'should have removed 3')
        self.assertEqual(b.root[KEY], 1, 'new root is 1')

    def test_node_size_gets_modified_on_insertion(self):
        b = BST.build([3,1,2,5,4])
        self.assertEqual(b.root[SIZE], 5, 'root has size of 5')

        b.insert(6)
        self.assertEqual(b.root[SIZE], 6, 'new root size is now 6')
        self.assertEqual(b.search(1)[SIZE], 2, '1 has size 2')
        self.assertEqual(b.search(2)[SIZE], 1, '2 has size 1')
        self.assertEqual(b.search(3)[SIZE], 6, '3 has size 6')
        self.assertEqual(b.search(4)[SIZE], 1, '4 has size 1')
        self.assertEqual(b.search(5)[SIZE], 3, '5 has size 3')
        self.assertEqual(b.search(6)[SIZE], 1, '6 has size 1')

    def test_node_size_gets_modified_on_deletion(self):
        b = BST.build([3,1,2,5,4])
        self.assertEqual(b.search(3)[SIZE], 5, '3 has size 6')

        b.delete(2) # Node is a leaf.
        self.assertEqual(b.search(1)[SIZE], 1, '1 has no more children')
        self.assertEqual(b.search(3)[SIZE], 4, 'root has 4 children now')

        b.delete(5) # Node is in the middle.
        self.assertEqual(b.search(4)[SIZE], 1, 'the size of 1 is unchanged')
        self.assertEqual(b.search(3)[SIZE], 3, 'root has 3 children after del')

        b.delete(3) # Node is the root.
        self.assertEqual(b.search(4)[SIZE], 1, 'the size of 1 is unchanged')
        self.assertEqual(b.search(1)[SIZE], 2, 'the new root is 1 and has size of 2')

    def test_select(self):
        b = BST.build([3,1,2,5,4])
        self.assertEqual(b.select(1)[KEY], 1, '1st elem is 1')
        self.assertEqual(b.select(2)[KEY], 2, '2nd elem is 2')
        self.assertEqual(b.select(3)[KEY], 3, '3rd elem is 3')
        self.assertEqual(b.select(4)[KEY], 4, '4th elem is 4')
        self.assertEqual(b.select(5)[KEY], 5, '5th elem is 5')

    def test_rank(self):
        b = BST.build([3,1,2,5,4])
        self.assertEqual(b.rank(1), 0, '0 keys smaller than 1')
        self.assertEqual(b.rank(2), 1, '1 key smaller than 2')
        self.assertEqual(b.rank(3), 2, '2 keys smaller than 3')
        self.assertEqual(b.rank(4), 3, '3 keys smaller than 4')
        self.assertEqual(b.rank(5), 4, '4 keys smaller than 5')
        self.assertIsNone(b.rank(6), 'key 6 does not exist')

    def test_rotate(self):
        """ Test the following right rotation, switching 5 and 7.
                (3)                      (3)
               /   \                    /   \
            (1)     (5)              (1)     (7)
              \     / \         =>     \     / \
             (2)  (4) (7)             (2)  (5) (8)
                      /  \                /  \
                    (6)  (8)            (4)  (6)
        """
        b = BST.build([3,1,2,5,4,7,8,6])
        b.rotate(b.search(5), RIGHT)

        root = b.search(3)
        node = b.search(5)
        child = b.search(7)

        self.assertEqual(root[LEFT][KEY], 1, 'root right child unchanged')
        self.assertEqual(root[RIGHT][KEY], 7, '7 swapped places with 5')
        self.assertEqual(node[PARENT][KEY], 7, '7 new parent of 5')
        self.assertEqual(node[LEFT][KEY], 4, 'left child of 5 remains unchanged')
        self.assertEqual(node[RIGHT][KEY], 6, 'left child of 7 becomes new '+
                                              'right child of 5')
        self.assertEqual(child[PARENT][KEY], 3, 'new parent of 7 is root')
        self.assertEqual(child[LEFT][KEY], 5, 'left child of 7 is now '+
                                              'its old parent 5')
        self.assertEqual(child[RIGHT][KEY], 8, '7 old right child is unchanged')

    def test_rotate_correctly_updates_sizes(self):
        """ Makes sure the rotate operation updates node sizes accordingly.
                (3)                      (3)
               /   \                    /   \
            (1)     (5)              (1)     (7)
              \     / \         =>     \     / \
             (2)  (4) (7)             (2)  (5) (8)
                      /  \                /  \
                    (6)  (8)            (4)  (6)
        """
        b = BST.build([3,1,2,5,4,7,8,6])
        b.rotate(b.search(5), RIGHT)

        self.assertEqual(b.search(3)[SIZE], 8, 'root has the same size')
        self.assertEqual(b.search(5)[SIZE], 3, 'rotated node has new size')
        self.assertEqual(b.search(7)[SIZE], 5, 'rotated node has new size')

    def test_rotate_in_isolation(self):
        """ Test makes sure the rotation operation works in isolation:
        No parent P, no subtrees A,B or C. Here's the tree format:

        Schema (for right rotations):

               (None)                     (None)
                 |                          |
                (2)                        (3)
               /   \           =>         /   \
           (None)  (3)                 (2)  (None)
                  /   \               /   \
              (None) (None)       (None) (None)

        Schema (for left rotations):

               (None)                     (None)
                 |                          |
                (3)                        (2)
               /   \           =>         /   \
            (2)  (None)                 (A)   (3)
           /   \                             /   \
       (None) (None)                     (None) (None)
        """
        b1 = BST.build([2,3])
        n2 = b1.search(2)
        n3 = b1.search(3)
        b1.rotate(n2, RIGHT)
        self.assertEqual(b1.root[KEY], 3, 'root has changed')
        self.assertEqual(n2[PARENT], n3)
        self.assertIsNone(n2[LEFT])
        self.assertIsNone(n2[RIGHT])
        self.assertIsNone(n3[PARENT])
        self.assertEqual(n3[LEFT], n2)
        self.assertIsNone(n3[RIGHT])

        b2 = BST.build([3,2])
        n2 = b2.search(2)
        n3 = b2.search(3)
        b2.rotate(n3, LEFT)
        self.assertEqual(b2.root[KEY], 2, 'root has changed')
        self.assertIsNone(n2[PARENT])
        self.assertIsNone(n2[LEFT])
        self.assertEqual(n2[RIGHT], n3)
        self.assertEqual(n3[PARENT], n2)
        self.assertIsNone(n3[LEFT])
        self.assertIsNone(n3[RIGHT])

    def test_join(self):
        """ Tests the method to join the current tree with another one. """

        bst1 = BST.build([1,3,5])
        bst2 = BST.build([2,4,6])
        joined = BST.join(bst1, bst2)

        self.assertTrue(BST.is_binary_search_tree(joined.root),
            'should have built a binary search tree')

        self.assertEqual(joined.root[KEY], 3)
        self.assertEqual(joined.root[SIZE], 3)
        self.assertEqual(joined.root[LEFT][KEY], 1)
        self.assertEqual(joined.root[LEFT][SIZE], 2)
        self.assertEqual(joined.root[LEFT][RIGHT][KEY], 2)
        self.assertEqual(joined.root[LEFT][RIGHT][SIZE], 1)
        self.assertEqual(joined.root[RIGHT][KEY], 5)
        self.assertEqual(joined.root[RIGHT][SIZE], 2)
        self.assertEqual(joined.root[RIGHT][LEFT][KEY], 4)
        self.assertEqual(joined.root[RIGHT][LEFT][SIZE], 1)
        self.assertEqual(joined.root[RIGHT][RIGHT][KEY], 6)
        self.assertEqual(joined.root[RIGHT][RIGHT][SIZE], 1)

    def test_in_order_traversal(self):
        """ Running examples:
                    (3)
                   /   \
                (1)     (5)
               /  \     / \
             (0)  (2) (4) (7)
        """
        tree = BST.build([3, 1, 0, 2, 5, 4, 7])
        expected = [0, 1, 2, 3, 4, 5, 7]
        actual = tree.in_order_traversal()
        self.assertEqual(actual, expected, 'in-order traversal')

    def test_pre_order_traversal(self):
        """ Running examples:
                    (3)
                   /   \
                (1)     (5)
               /  \     / \
             (0)  (2) (4) (7)
        """
        tree = BST.build([3, 1, 0, 2, 5, 4, 7])
        expected = [3, 1, 0, 2, 5, 4, 7]
        actual = tree.pre_order_traversal()
        self.assertEqual(actual, expected, 'pre-order traversal')

    def test_post_order_traversal(self):
        """ Running examples:
                    (3)
                   /   \
                (1)     (5)
               /  \     / \
             (0)  (2) (4) (7)
        """
        tree = BST.build([3, 1, 0, 2, 5, 4, 7])
        expected = [0, 2, 1, 4, 7, 5, 3]
        actual = tree.post_order_traversal()
        self.assertEqual(actual, expected, 'post-order traversal')

    def test_is_subtree(self):
        """ Given the following binary tree:
                    (3)
                   /   \
                (1)     (5)
               /  \     / \
             (0)  (2) (4) (7)
        """
        tree = BST.build([3, 1, 0, 2, 5, 4, 7])
        subtree1 = BST.build([1, 0, 2]) # Left subtree
        subtree2 = BST.build([2]) # A leaf.
        subtree3 = BST.build([3, 1, 0, 2, 5, 4, 7]) # The same tree.
        subtree4 = BST.build([5, 4, 8]) # Modified right subtree.

        self.assertTrue(tree.is_subtree(subtree1), 'the left subtree')
        self.assertTrue(tree.is_subtree(subtree2), 'a tree with only leaf')
        self.assertTrue(tree.is_subtree(subtree3), 'the same as original tree')
        self.assertFalse(tree.is_subtree(subtree4), 'modified right subtree')

    def test_is_subtree_in_case_of_duplicate_root_keys(self):
        """ Given the following binary tree:
                    (4)
                   /   \
                (2)     (5)
               /
             (2)
            /
          (1)


        """
        tree = BST.build([4, 2, 2, 1, 5])
        subtree = BST.build([2, 1])
        actual = tree.is_subtree(subtree)
        self.assertTrue(actual, 'should discover the correct subtree')

    def test_is_subtree_when_duplicate_key_is_not_immediate_descendant(self):
        """  Given the following tree and the lookup subtree:
            (3)
           /  \
         (2)  (6)           (3)
             /   \            \
           (3)   (7)          (5)
              \
              (5)
        """
        tree = BST.build([3, 2, 6, 3, 7, 5, 3])
        subtree = BST.build([3, 3])
        actual = tree.is_subtree(subtree)
        self.assertTrue(actual, 'should discover the correct subtree')

    def test_diameter(self):
        """ Given the following binary search tree:
                (3)
               /  \
             (2)  (4)
            /        \
          (1)        (5)
        """
        tree = BST.build([3,2,1,4,5])
        actual = tree.diameter()
        expected = 5
        self.assertEqual(actual, expected, 'should return the path with '+
                                           'the max number of vertices')

    def test_unballanced_graph_diameter(self):
        """ Given the following binary search tree:
                (1)
                  \
                  (2)
                     \
                     (3)
                       \
                       (4)
                          \
                          (5)
        """
        tree = BST.build([1,2,3,4,5])
        actual = tree.diameter()
        expected = 5
        self.assertEqual(actual, expected, 'should return the path with '+
                                           'the max number of vertices')

    def test_is_ballanced_binary_search_tree(self):
        """ Test three cases:
              (3)        (3)               (3)
                        /   \             /   \
                     (1)     (7)       (1)     (7)
                       \     / \               /  \
                      (2)  (5) (10)          (5) (10)
                          /  \
                        (4) (6)
        """
        bst1 = BST.build([3])
        bst2 = BST.build([3, 1, 2, 7, 5, 4, 6, 10])
        bst3 = BST.build([3, 1, 7, 5, 10])

        self.assertTrue(BST.is_ballanced_binary_search_tree(bst1))
        self.assertFalse(BST.is_ballanced_binary_search_tree(bst2))
        self.assertTrue(BST.is_ballanced_binary_search_tree(bst3))

    def test_is_binary_search_tree(self):
        """ Construct two trees, a plain one and a binary search tree:
        - binary search tree -    - non-search-tree -
                (3)                      (3)
               /   \                    /   \
            (1)     (5)              (9)     (7)
              \     / \                \     / \
             (2)  (4) (7)             (2)  (5) (4)
                      /  \                /  \
                    (6)  (8)            (10)  (6)
        """
        n10 = [None, 10, None, None]
        n6 = [None, 6, None, None]
        n4 = [None, 4, None, None]
        n2 = [None, 2, None, None]
        n5 = [None, 5, n10, n6]
        n10[PARENT] = n5
        n6[PARENT] = n5
        n7 = [None, 7, n5, n4]
        n5[PARENT] = n7
        n4[PARENT] = n7
        n9 = [None, 9, None, n2]
        n2[PARENT] = n9
        n3 = [None, 3, n9, n7]
        n9[PARENT] = n3
        n7[PARENT] = n3
        notSearchTree = n3

        trueSearchTree = BST.build([3,1,2,5,4,7,8,9]).root

        self.assertTrue(BST.is_binary_search_tree(trueSearchTree),
            'should detect a correct search tree')
        self.assertFalse(BST.is_binary_search_tree(notSearchTree),
            'should detect a when a tree is not search tree')

    def test_from_sorted(self):
        """ Tests construction of a BST from a sorted array. """

        a = [1,2,3,4,5,5,6]
        tree = BST.from_sorted(a)
        self.assertTrue(BST.is_binary_search_tree(tree.root),
            'should have built a binary search tree')

        self.assertEqual(tree.root[KEY], 4)
        self.assertEqual(tree.root[SIZE], 3)
        self.assertEqual(tree.root[LEFT][KEY], 2)
        self.assertEqual(tree.root[LEFT][SIZE], 2)
        self.assertEqual(tree.root[LEFT][LEFT][KEY], 1)
        self.assertEqual(tree.root[LEFT][LEFT][SIZE], 1)
        self.assertEqual(tree.root[LEFT][RIGHT][KEY], 3)
        self.assertEqual(tree.root[LEFT][RIGHT][SIZE], 1)
        self.assertEqual(tree.root[RIGHT][KEY], 5)
        self.assertEqual(tree.root[RIGHT][SIZE], 2)
        self.assertEqual(tree.root[RIGHT][LEFT][KEY], 5)
        self.assertEqual(tree.root[RIGHT][LEFT][SIZE], 1)
        self.assertEqual(tree.root[RIGHT][RIGHT][KEY], 6)
        self.assertEqual(tree.root[RIGHT][RIGHT][SIZE], 1)

    def test_from_sorted_with_an_inballanced_tree(self):
        """ Tests construction of a BST from a sorted array. """

        a = [1,2]
        tree = BST.from_sorted(a)
        self.assertTrue(BST.is_binary_search_tree(tree.root),
            'should have built a binary search tree')
        self.assertEqual(tree.root[KEY], 1)
        self.assertEqual(tree.root[SIZE], 2)
        self.assertEqual(tree.root[RIGHT][KEY], 2)
        self.assertEqual(tree.root[RIGHT][SIZE], 1)
