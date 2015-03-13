import unittest

from src.ballanced_binary_search_tree import BST, PARENT, KEY, LEFT, RIGHT, SIZE


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

        actual = [node[KEY] for node in b.list_sorted()]
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
