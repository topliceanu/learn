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

    def test_delete(self):
        b = BST.build([3,1,2,5,4])

        b.delete(2)
        self.assertIsNone(b.search(2), 'should not find 2 anymore')
        self.assertIsNone(b.search(1)[RIGHT], '1 has no more children')

        b.delete(5)
        self.assertIsNone(b.search(5), 'should have removed 5')
        self.assertEqual(b.search(4)[PARENT][KEY], 3, 'should have hoisted 4')

        b.delete(3)
        self.assertIsNone(b.search(3), 'should have removed 3')

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

        b.delete(2)
        self.assertEqual(b.search(1)[SIZE], 1, '1 has no more children')
        self.assertEqual(b.search(3)[SIZE], 4, 'root has 4 children now')

        b.delete(5)
        self.assertEqual(b.search(4)[SIZE], 1, 'the size of 1 is unchanged')
        self.assertEqual(b.search(3)[SIZE], 3, 'root has 3 children after del')

        b.delete(3)
        self.assertEqual(b.search(4)[SIZE], 1, 'the size of 1 is unchanged')
        self.assertEqual(b.search(1)[SIZE], 2, 'the new root is 1 and has size of 2')
