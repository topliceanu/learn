import unittest

from src.ballanced_binary_search_tree import BBST


class TestBBST(unittest.TestCase):
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

    def test_insert(self):
        data = [3,1,2,5,4]

        b = BBST()
        for key in data:
            b.insert(key)

        self.assertEqual(b.length, 5, 'should have inserted 5 keys')

    def test_search(self):
        data = [3,1,2,5,4]

        b = BBST()
        for key in data:
            b.insert(key)

        self.assertTrue(b.search(3), 'should find 3 in the bst')
        self.assertTrue(b.search(1), 'should find 1 in the bst')
        self.assertTrue(b.search(2), 'should find 2 in the bst')
        self.assertTrue(b.search(5), 'should find 5 in the bst')
        self.assertTrue(b.search(4), 'should find 4 in the bst')
        self.assertFalse(b.search(10), 'should not find 10 in the bst')
