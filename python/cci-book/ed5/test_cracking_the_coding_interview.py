# -*- coding: utf-8 -*-

import unittest

from cracking_the_coding_interview import *


class CrackingTheCodeInterview(unittest.TestCase):

    # Chapter 1: Arrays and Strings

    def test_problem_1_1(self):
        data = 'alexandru'
        self.assertFalse(problem_1_1(data), 'should detect duplicate chars')

        data = 'alex'
        self.assertTrue(problem_1_1(data), 'all chars are unique')

        data = 'alexandru'
        self.assertFalse(problem_1_1_bis(data), 'should detect duplicate chars')

        data = 'alex'
        self.assertTrue(problem_1_1_bis(data), 'all chars are unique')

    def test_problem_1_2(self):
        data = 'alex$'
        expected = 'xela$'
        actual = problem_1_2(data)
        self.assertEqual(actual, expected, 'should invert correctly')

    def test_problem_1_3(self):
        data = ""
        expected = ""
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "a"
        expected = "a"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "abc"
        expected = "abc"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "abcc"
        expected = "abc"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "aabc"
        expected = "abc"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "abca"
        expected = "abca"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

        data = "aaaa"
        expected = "a"
        self.assertEqual(problem_1_3(data), expected, 'removed duplicate consecutive chars')

    def test_problem_1_4(self):
        s1 = 'cat'
        s2 = 'act'
        self.assertTrue(problem_1_4(s1, s2), 'are anagrams')

        s1 = 'cats'
        s2 = 'act'
        self.assertFalse(problem_1_4(s1, s2), 'are not anagrams')

        s1 = 'aab'
        s2 = 'aba'
        self.assertTrue(problem_1_4(s1, s2), 'are anagrams')

        s1 = 'aab'
        s2 = 'abc'
        self.assertFalse(problem_1_4(s1, s2), 'are not anagrams')

        s1 = 'zzz'
        s2 = 'zzzz'
        self.assertFalse(problem_1_4(s1, s2), 'found edge case where the letter was not counted correctly')

    def test_problem_1_5(self):
        s = '   '
        expected = '%20%20%20'
        actual = problem_1_5(s)
        self.assertEqual(actual, expected, 'correct url encode spaces')

        s = ' a '
        expected = '%20a%20'
        actual = problem_1_5(s)
        self.assertEqual(actual, expected, 'correct url encode spaces')

        s = 'ab'
        expected = 'ab'
        actual = problem_1_5(s)
        self.assertEqual(actual, expected, 'correct url encode spaces')

    def test_problem_1_6(self):
        arr = [
            [ 1,  2,  3,  4,  5],
            [ 6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        actual = problem_1_6(arr)
        expected = [
            [21, 16, 11,  6, 1],
            [22, 17, 12,  7, 2],
            [23, 18, 13,  8, 3],
            [24, 19, 14,  9, 4],
            [25, 20, 15, 10, 5]
        ]
        self.assertItemsEqual(actual, expected, 'should rotate array')

    def test_problem_1_7(self):
        arr = [
            [ 0,  2,  3,  4,  5],
            [ 6,  7,  8,  0, 10],
            [ 0, 12,  0, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        expected = [
            [ 0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0],
            [ 0, 17,  0,  0, 20],
            [ 0, 22,  0,  0, 25],
        ]
        actual = problem_1_7(arr)
        self.assertItemsEqual(actual, expected, 'should turn correct items to zero')

    def test_problem_1_8(self):
        s1 = 'waterbottle'
        s2 = 'erbottlewat'
        self.assertTrue(problem_1_8(s1, s2), 'should detect rotated string')

        s1 = 'waterbottle'
        s2 = 'wabottleter'
        self.assertFalse(problem_1_8(s1, s2), 'should not detect any rotated string')

        s1 = 'abcd'
        s2 = 'bcdab'
        self.assertFalse(problem_1_8(s1, s2), 'should not detect any rotated string')

    # Chapter 2: Linked Lists.

    def test_problem_2_1(self):
        initial = SingleLinkedListNode.from_list([1,2,2,2,3,4,5])
        actual = problem_2_1(initial)
        expected = [1,2,3,4,5]
        self.assertEqual(actual.to_list(), expected, 'should remove duplicate 2s')

    def test_problem_2_2(self):
        l = SingleLinkedListNode.from_list([1,2,3,4,5])
        expected = 4
        actual = problem_2_2(l, 2).key
        self.assertEqual(actual, expected, 'should detect the correct value')

        l = SingleLinkedListNode.from_list([1])
        expected = 4
        actual = problem_2_2(l, 2)
        self.assertIsNone(actual, 'should detect index error')

        self.assertRaises(Exception, problem_2_2, None, -2,
            'should detect bad input params and raise exception')

        l = SingleLinkedListNode.from_list([1,2,3,4,5])
        expected = 5
        actual = problem_2_2(l, 1).key
        self.assertEqual(actual, expected, 'should detect the correct value')

        l = SingleLinkedListNode.from_list([1,2,3,4,5])
        expected = 1
        actual = problem_2_2(l, 5).key
        self.assertEqual(actual, expected, 'should detect the correct value')

    def test_problem_2_3(self):
        l = SingleLinkedListNode.from_list([1,2,3,4,5])
        node = l.next.next # Node with key 3.
        problem_2_3(node)

        actual = l.to_list()
        expected = [1,2,4,5]
        self.assertEqual(actual, expected, 'should have removed the key 3')

        l = SingleLinkedListNode.from_list([1,2,3,4,5])
        node = l.next.next.next.next # Node with key 5.
        self.assertRaises(Exception, problem_2_3, node,
            'should detect the last node in the list')

    def test_problem_2_4(self):
        l1 = SingleLinkedListNode.from_list([2,3,4])
        l2 = SingleLinkedListNode.from_list([1,2,3])
        expected = SingleLinkedListNode.from_list([3,5,7])
        actual = problem_2_4(l1, l2)
        self.assertEqual(actual.to_list(), expected.to_list(),
            'should compute sum of two regular numbers')

        l1 = SingleLinkedListNode.from_list([])
        l2 = SingleLinkedListNode.from_list([1,2,3])
        expected = SingleLinkedListNode.from_list([1,2,3])
        actual = problem_2_4(l1, l2)
        self.assertEqual(actual.to_list(), expected.to_list(),
            'should compute sum when the other element is empty')

        l1 = SingleLinkedListNode.from_list([1,2,3])
        l2 = SingleLinkedListNode.from_list([2])
        expected = SingleLinkedListNode.from_list([3,2,3])
        actual = problem_2_4(l1, l2)
        self.assertEqual(actual.to_list(), expected.to_list(),
            'should compute sum when one number has less digits')

        l1 = SingleLinkedListNode.from_list([9,9,9])
        l2 = SingleLinkedListNode.from_list([9,9,9])
        expected = SingleLinkedListNode.from_list([8,9,9,1])
        actual = problem_2_4(l1, l2)
        self.assertEqual(actual.to_list(), expected.to_list(),
            'should compute sum when digit overflow occurs')

    def test_problem_2_5(self):
        l = SingleLinkedListNode.from_list([1,2,3,4,5,6,7])
        start = l.next.next # Node with key 3.
        last = start.next.next.next.next # Node with key 7.
        last.next = start

        actual = problem_2_5(l)
        self.assertEqual(actual, start, 'should detect the start node')

    # Chapter 3: Stacks and Queues

    def test_problem_3_1(self):
        ThreeStacks = problem_3_1()
        stacks = ThreeStacks()
        stacks.push(0, 1)
        stacks.push(0, 2)
        stacks.push(1, 3)
        stacks.push(1, 4)
        stacks.push(2, 5)
        stacks.push(2, 6)

        expected = [6, 12, 18, 0, None, 1, 0, 3, 2, 1, None, 3, 1, 9, 4, 2, None, 5, 2, 15, 6]
        self.assertEqual(stacks.arr, expected, 'array should look ok after all those inserts')

        value = stacks.pop(0)
        self.assertEqual(value, 2, 'stack #0 produces 2')
        value = stacks.pop(0)
        self.assertEqual(value, 1, 'stack #0 produces 1')
        value = stacks.pop(0)
        self.assertIsNone(value, 'stack #0 is now empty')

        value = stacks.pop(1)
        self.assertEqual(value, 4, 'stack #1 produces 4')
        value = stacks.pop(1)
        self.assertEqual(value, 3, 'stack #1 produces 3')
        value = stacks.pop(1)
        self.assertIsNone(value, 'stack #1 is now empty')

        value = stacks.pop(2)
        self.assertEqual(value, 6, 'stack #2 produces 6')
        value = stacks.pop(2)
        self.assertEqual(value, 5, 'stack #2 produces 5')
        value = stacks.pop(2)
        self.assertIsNone(value, 'stack #2 is now empty')

        expected = [None, None, None, '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__', '__']
        self.assertEqual(stacks.arr, expected, 'stacks are all empty')

    def test_problem_3_2(self):
        MinStack = problem_3_2()
        s = MinStack()

        s.push(2)
        self.assertEqual(s.min(), 2, 'should compute the min value')

        s.push(1)
        self.assertEqual(s.min(), 1, 'should compute the min value')

        s.pop()
        self.assertEqual(s.min(), 2, 'should compute the min value')

        s.pop()
        self.assertIsNone(s.min(), 'no more components in the stack')

    def test_problem_3_3(self):
        SetOfStacks = problem_3_3()

        s = SetOfStacks(2)
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(len(s.stacks), 3, 'should have built three stacks')
        self.assertEqual(s.stacks[0], [1, 2], 'should have filled the first stack')
        self.assertEqual(s.stacks[1], [3, 4], 'should have filled the second stack')
        self.assertEqual(s.stacks[2], [5], 'should have added to the third stack')

        value = s.pop()
        self.assertEqual(value, 5, 'removed the last value')
        self.assertEqual(s.stacks[2], [], 'last stack is now empty')

        value = s.pop()
        self.assertEqual(value, 4, 'removed the last value')
        self.assertEqual(len(s.stacks), 2, 'only two stacks are left')
        self.assertEqual(s.stacks[1], [3], 'last stack now has only one element')

        s.pop()
        s.pop()
        value = s.pop()
        self.assertEqual(value, 1, 'removed the last element from the set of stacks')
        self.assertEqual(len(s.stacks), 1, 'only one stack left')
        self.assertEqual(s.stacks[0], [], 'last stack left is empty')

        value = s.pop()
        self.assertIsNone(value, 'no more data in the set of stacks')
        self.assertEqual(len(s.stacks), 0, 'all stacks have been deleted')

        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        value = s.popAt(1)
        self.assertEqual(value, 4, 'should have returned the last value of the second stack')
        self.assertEqual(s.stacks[0], [1, 2], 'should have filled the first stack')
        self.assertEqual(s.stacks[1], [3, 5], 'should have the value from the last stack')
        self.assertEqual(s.stacks[2], [], 'should be left an empty stack')

    def test_problem_3_4(self):
        actual = problem_3_4([1,2,3,4,5,6], [], [])
        expected = ([], [], [1,2,3,4,5,6])
        self.assertEqual(actual, expected,
            'should have moved the disks to the last rod')

    def test_problem_3_5(self):
        MyQueue = problem_3_5()
        q = MyQueue()
        q.enqueue(1)
        q.enqueue(2)

        self.assertEqual(len(q), 2, 'two elements in the queue')
        self.assertEqual(q.dequeue(), 1, 'should return the first value')
        self.assertEqual(q.dequeue(), 2, 'should return the second value')
        self.assertIsNone(q.dequeue(), 'queue is empty')

    def test_problem_3_6(self):
        l = Stack()
        for i in [7, 2, 1, 8, 3]:
            l.push(i)

        problem_3_6(l)
        for i in [8, 7, 3, 2, 1]:
            self.assertEqual(i, l.pop(), 'should have sorted the queue')

    # Chapter 4: Trees and Graphs

    def test_problem_4_1(self):
        # Inballanced tree.
        r = TreeNode('r')
        n1 = TreeNode('1')
        n2 = TreeNode('2')
        n3 = TreeNode('3')
        n4 = TreeNode('4')
        n5 = TreeNode('5')
        n6 = TreeNode('6')
        r.children = [n1, n2, n3]
        n3.children = [n4, n5]
        n4.children = [n6]
        self.assertFalse(problem_4_1(r), 'should detect that the tree is inballanced')

        # Ballanced tree.
        r = TreeNode('r')
        n1 = TreeNode('1')
        n2 = TreeNode('2')
        n3 = TreeNode('3')
        n4 = TreeNode('4')
        n5 = TreeNode('5')
        n6 = TreeNode('6')
        r.children = [n1, n2, n3]
        n1.children = [n4, n5]
        n2.children = [n6]
        self.assertTrue(problem_4_1(r), 'should detect that the tree is ballanced')

    def test_problem_4_2(self):
        v1 = GraphVertex('1')
        v2 = GraphVertex('2')
        v3 = GraphVertex('3')
        v4 = GraphVertex('4')
        v5 = GraphVertex('5')
        v1.adjacent = [v2, v3]
        v2.adjacent = [v4]
        v3.adjacent = [v4]
        v5.adjacent = [v4]
        self.assertTrue(problem_4_2(v1, v4), 'there is a direct route from v1 to v4')
        self.assertTrue(problem_4_2(v5, v4), 'there is a direct route from v5 to v4')
        self.assertFalse(problem_4_2(v1, v5), 'there is no direct route from v1 to v5')

    def test_problem_4_3(self):
        arr = [1,2,3,4,5,6]
        actual = problem_4_3(arr)
        self.assertEqual(actual.key, 3)
        self.assertEqual(actual.children[0].key, 1)
        self.assertEqual(actual.children[0].children[1].key, 2)
        self.assertEqual(actual.children[1].key, 5)
        self.assertEqual(actual.children[1].children[0].key, 4)
        self.assertEqual(actual.children[1].children[1].key, 6)

    def test_problem_4_4(self):
        r = TreeNode('r')
        n1 = TreeNode('1')
        n2 = TreeNode('2')
        n3 = TreeNode('3')
        n4 = TreeNode('4')
        n5 = TreeNode('5')
        n6 = TreeNode('6')
        r.children = [n1, n2]
        n1.children = [n3, n4]
        n2.children = [n5, n6]

        lists = problem_4_4(r)
        self.assertEqual(len(lists), 3, 'three lists are produces')

        self.assertEqual(lists[0].key, r, 'the first list contains the root')
        self.assertEqual(lists[1].key, n1, 'first level of nodes')
        self.assertEqual(lists[1].next.key, n2, 'first level of nodes')
        self.assertEqual(lists[2].key, n3, 'second level of nodes')
        self.assertEqual(lists[2].next.key, n4, 'second level of nodes')
        self.assertEqual(lists[2].next.next.key, n5, 'second level of nodes')
        self.assertEqual(lists[2].next.next.next.key, n6, 'second level of nodes')

    def test_problem_4_5(self):
        """ The tree under test is the following:
                (4)
               /   \
            (2)     (6)
            / \     / \
          (1) (3) (5) (7)
        """
        n1 = BinaryTreeNode('1')
        n2 = BinaryTreeNode('2')
        n3 = BinaryTreeNode('3')
        n4 = BinaryTreeNode('4')
        n5 = BinaryTreeNode('5')
        n6 = BinaryTreeNode('6')
        n7 = BinaryTreeNode('7')
        n4.left = n2; n4.right = n6
        n2.left = n1; n2.right = n3
        n6.left = n5; n6.right = n7
        n2.parent = n6.parent = n4
        n1.parent = n3.parent = n2
        n5.parent = n7.parent = n6

        self.assertEqual(problem_4_5(n4), n5, 'successor to 4 is 5')
        self.assertEqual(problem_4_5(n6), n7, 'successor to 6 is 7')
        self.assertEqual(problem_4_5(n1), n2, 'successor to 1 is 2')

    def test_problem_4_6(self):
        """ The tree under test is the following:
                (1)
               / | \
            (2) (3) (4)
             |   | \
            (5) (6) (7)
        """
        n1 = TreeNode('1')
        n2 = TreeNode('2')
        n3 = TreeNode('3')
        n4 = TreeNode('4')
        n5 = TreeNode('5')
        n6 = TreeNode('6')
        n7 = TreeNode('7')
        n1.children = [n2, n3, n4]
        n2.children = [n5]
        n3.children = [n6, n7]
        n2.parent = n3.parent = n4.parent = n1
        n5.parent = n2
        n6.parent = n7.parent = n3
        self.assertEqual(problem_4_6(n5, n7), n1, '1 is root for 5 and 7')
        self.assertEqual(problem_4_6(n5, n2), n2, '2 is root for 5 and 2')

    def test_problem_4_7(self):
        n1 = BinaryTreeNode(1)
        n2 = BinaryTreeNode(2)
        n3 = BinaryTreeNode(3)
        n4 = BinaryTreeNode(4)
        n5 = BinaryTreeNode(5)
        n6 = BinaryTreeNode(6)
        n7 = BinaryTreeNode(7)
        n8 = BinaryTreeNode(8)
        n1.left = n4
        n1.right = n7
        n4.left = n3
        n4.rigth = n5
        n7.left = n6
        n7.right = n8
        n3.left = n2
        self.assertTrue(problem_4_7(n1, n7), '7 is the child of 1 so a subtree')

    def test_problem_4_8(self):
        # TODO make this work!
        pass

    # Chapter 5: Bit Manipulation.

    def test_problem_5_1(self):
        n = int('10000000000', 2)
        m = int('10101', 2)
        i = 2
        j = 6
        actual = problem_5_1(n, m, i, j)
        expected = int('10001010100', 2)
        self.assertEqual(actual, expected, 'should produce the correct value')

        n = int('11111111111', 2)
        m = int('10101', 2)
        i = 2
        j = 6
        actual = problem_5_1(n, m, i, j)
        expected = int('11111010111', 2)
        self.assertEqual(actual, expected, 'should produce the correct value')

    def test_problem_5_2(self):
        n = 3.75
        actual = problem_5_2(n)
        expected = '11,11'
        self.assertEqual(actual, expected, 'should return the correct value')

        n = 3.17
        self.assertRaises(Exception, problem_5_2, n,
            'should raise because no accurate representation can be computed')

    def test_problem_5_3(self):
        n = int('111', 2)
        self.assertRaises(Exception, problem_5_3, n, 'should detect that '+
            'there is no smaller number but with the same number of set bits')

        n = int('110', 2)
        actual = problem_5_3(n)
        expected = (int('101', 2), int('1001', 2))
        self.assertEqual(actual, expected, 'should produce the correct values')

    def test_problem_5_5(self):
        a = 31
        b = 14
        expected = 2
        actual = problem_5_5(a, b)
        self.assertEqual(actual, expected, 'should compute the number of different bits')

        a = 67
        b = 143
        expected = 4
        actual = problem_5_5(a, b)
        self.assertEqual(actual, expected, 'should compute the number of different bits')

    def test_problem_5_6(self):
        n = int('10', 2)
        expected = int('01', 2)
        actual = problem_5_6(n)
        self.assertEqual(actual, expected, 'should swap bits correctly')

        n = int('111011', 2)
        expected = int('110111', 2)
        actual = problem_5_6(n)
        self.assertEqual(actual, expected, 'should swap bits correctly')

        n = int('01110101', 2)
        expected = int('10111010', 2)
        actual = problem_5_6(n)
        self.assertEqual(actual, expected, 'should swap bits correctly')

    def x_test_problem_5_7(self):
        arr = [1,2,4,5,6,7,8,9]
        expected = 3
        actual = problem_5_7(arr)
        self.assertEqual(actual, expected, 'should detect the missing value')

    # Chapter 8: Recursion

    def test_problem_8_1(self):
        self.assertEqual(problem_8_1(3), 3,
            'should correctly compute the fib number')

    def test_problem_8_2(self):
        actual = problem_8_2(2)
        expected = 2
        self.assertEqual(actual, expected, 'only two ways to get from the '+
                                        'top left to the botton right corners')

        actual = problem_8_2(3)
        expected = 6
        self.assertEqual(actual, expected, 'only two ways to get from the '+
                                        'top left to the botton right corners')

    def test_problem_8_2_bis(self):
        grid = [
            [0, 0],
            [1, 0]
        ]
        actual = problem_8_2_bis(grid)
        expected = [[(0,0), (0,1), (1,1)]]
        self.assertItemsEqual(actual, expected,
            'should compute the correct available paths')

        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        actual = problem_8_2_bis(grid)
        expected = [[(0,0), (0,1), (0,2), (1,2), (2,2)]]
        self.assertItemsEqual(actual, expected,
            'should compute the correct available paths')

        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        actual = problem_8_2_bis(grid)
        expected = [[(0,0), (0,1), (0,2), (1,2), (2,2)]]
        self.assertItemsEqual(actual, expected,
            'should compute the correct available paths')

        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]
        actual = problem_8_2_bis(grid)
        expected = [[(0,0), (0,1), (0,2), (1,2), (2,2)]]
        self.assertItemsEqual(actual, expected,
            'should compute the correct available paths')

        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        actual = problem_8_2_bis(grid)
        expected = [[(0,0), (0,1), (0,2), (1,2), (2,2)],
                    [(0,0), (1,0), (2,0), (2,1), (2,2)]]
        self.assertItemsEqual(actual, expected,
            'should compute the correct available paths')

    def test_problem_8_3(self):
        data = set([1,2,3])
        expected = [set([1]), set([2]), set([3]), set([1,2]), set([1,3]),
                    set([2,3]), set([1,2,3]), set([])]
        actual = problem_8_3(data)
        self.assertItemsEqual(actual, expected,
            'should compute all the subsets of a set')

    def test_problem_8_4(self):
        data = 'abc'
        expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        actual = problem_8_4(data)
        self.assertItemsEqual(actual, expected,
            'should compute all permutations')

    def test_problem_8_5(self):
        expected = ['()()()', '()(())', '(())()', '((()))', '(()())']
        actual = problem_8_5(3)
        self.assertItemsEqual(actual, expected,
            'should produce correct prantheses')

    def test_problem_8_6(self):
        canvas = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 0, 1],
            [1, 0, 0, 0, 1]
        ]
        expected = [
            [1, 0, 0, 2, 0],
            [1, 0, 2, 2, 0],
            [0, 2, 2, 2, 0],
            [0, 2, 2, 0, 1],
            [1, 0, 0, 0, 1]
        ]

        problem_8_6(canvas, (2, 2), 2)
        self.assertItemsEqual(canvas, expected,
            'should color only on in straight line, not diagonals')

    def test_problem_8_7(self):
        change = 3
        expected = 1
        actual = problem_8_7(change)
        self.assertEqual(actual, expected,
            'should compute the number of combinations')

        change = 6
        expected = 2
        actual = problem_8_7(change)
        self.assertEqual(actual, expected,
            'should compute the number of combinations')

        change = 27
        expected = 32
        actual = problem_8_7(change)
        self.assertEqual(actual, expected,
            'should compute the number of combinations')

    def test_problem_8_8(self):
        actual = problem_8_8(4)
        expected = 2
        self.assertEqual(len(actual), expected, 'should compute how many ways '+
            'one can arrange 4 queens on a 4x4 table so that they do not attach each other')

        actual = problem_8_8(8)
        expected = 92
        self.assertEqual(len(actual), expected, 'should compute how many ways '+
            'one can arrange 8 queens on a 8x8 table so that they do not attach each other')

    # Chapter 9: Searching and Sorting

    def test_problem_9_1(self):
        arr1 = [1, 2, 3, 4, None, None, None]
        arr2 = [0, 5, 6]
        expected = [0, 1, 2, 3, 4, 5, 6]
        actual = problem_9_1(arr1, arr2)
        self.assertEqual(actual, expected, 'should merge the two arrays')

        arr1 = [1, 3, 5, 7, None, None, None, None]
        arr2 = [0, 2, 4, 6]
        expected = [0, 1, 2, 3, 4, 5, 6, 7]
        actual = problem_9_1(arr1, arr2)
        self.assertEqual(actual, expected, 'should merge the two arrays')

        arr1 = [2, 3, 4, None, None]
        arr2 = [0, 1]
        expected = [0, 1, 2, 3, 4]
        actual = problem_9_1(arr1, arr2)
        self.assertEqual(actual, expected, 'should merge the two arrays')

    def test_problem_9_2(self):
        strings = ['cat', 'act', 'boo', 'foo', 'baz']
        expected = ['cat', 'act', 'baz', 'boo', 'foo']
        actual = problem_9_2(strings)
        self.assertEquals(actual, expected,
            'should sort the list such that anagrams are near-by')

    def test_problem_9_3(self):
        arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        actual = problem_9_3(arr, 5)
        expected = 8 # index of 5 in arr.
        self.assertEqual(actual, expected, 'should compute the correct index')

        arr = [8, 9, 1, 2, 3, 4, 5, 6, 7]
        actual = problem_9_3(arr, 5)
        expected = 6 # index of 5 in arr.
        self.assertEqual(actual, expected, 'should compute the correct index')

        arr = [3, 4, 5, 6, 7, 8, 9, 1, 2]
        actual = problem_9_3(arr, 5)
        expected = 2 # index of 5 in arr.
        self.assertEqual(actual, expected, 'should compute the correct index')

    def test_problem_9_5(self):
        arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
        actual = problem_9_5(arr, 'ball')
        expected = 4
        self.assertEqual(actual, expected, 'should find the correct position of the word')

        arr = ["at", "", "", "", "", "ball", "car", "", "", "dad", "", ""]
        actual = problem_9_5(arr, 'ballcar')
        expected = -1
        self.assertEqual(actual, expected, 'should find the correct position of the word')

    def test_problem_9_6(self):
        mat = [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]
        ]
        self.assertTrue(problem_9_6(mat, 15), 'should find the element 15')
        self.assertTrue(problem_9_6(mat, 9), 'should find the element 9')
        self.assertTrue(problem_9_6(mat, 22), 'should find the element 22')
        self.assertFalse(problem_9_6(mat, 35), 'should not find element 35')
        self.assertFalse(problem_9_6(mat, -5), 'should not find element -5')

    def x_test_problem_9_7(self):
        data = [(75, 190), (70, 150), (68, 110), (65, 100), (60, 95), (56, 90)]
        expected = [(56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)]
        actual = problem_9_7(data)
        self.assertItemsEqual(actual, expected, 'should compute the highest tower')

        data = [(75, 190), (70, 150), (58, 140), (65, 100), (60, 95), (56, 90)]
        expected = [(75, 190), (70, 150), (65, 100), (60, 95), (56, 90)]
        actual = problem_9_7(data)
        self.assertItemsEqual(actual, expected, 'should compute the highest tower')

    # Chapter 10: Mathematical

    def test_problem_10_4(self):
        actual = problem_10_4('+', 10, 20)
        self.assertEqual(actual, 30, 'should produce the sum of the operands')

        actual = problem_10_4('-', 20, 10)
        self.assertEqual(actual, 10, 'should produce the diff of the operands')

        actual = problem_10_4('*', 4, 5)
        self.assertEqual(actual, 20, 'should produce the multiplication of the operands')

        actual = problem_10_4('/', 5, 4)
        self.assertEqual(actual, 1, 'should produce the div of the operands')

    def test_problem_10_5(self):
        expected = (0, 1)
        actual = problem_10_5(({'x': 1, 'y': 1}, {'x': 2, 'y': 1}),
                              ({'x': 3, 'y': 1}, {'x': 4, 'y': 1}))
        self.assertEqual(actual, expected,
            'should correctly compute the line between the two centers')

    def test_problem_10_6(self):
        points = [(2,3), (4,5), (6,7), (8,9), (1,1), (2,2), (3,3)]
        expected = {(2,3), (4,5), (6,7), (8,9)}
        actual = problem_10_6(points)
        self.assertEqual(actual, expected, 'should find largest set of points')

    def test_problem_10_7(self):
        # NOTE: THIS IS INCORRECT!
        self.assertEqual(problem_10_7(0), 3*5*7, 'should have worked')
        self.assertEqual(problem_10_7(1), 3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7(2), 3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7(3), 3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(4), 3*3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7(5), 3*3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7(6), 3*3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(7), 3*5*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7(8), 3*3*3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7(9), 3*5*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(10), 3*3*3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7(11), 3*5*7*7*7, 'should have worked')
        self.assertEqual(problem_10_7(12), 3*3*3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(13), 3*3*5*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(14), 3*3*3*5*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7(15), 3*3*5*5*5*7*7, 'should have worked')

    def test_problem_10_7_bis(self):
        self.assertEqual(problem_10_7_bis(0), 3*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(1), 3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(2), 3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(3), 3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(4), 3*3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(5), 3*3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(6), 3*3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(7), 3*5*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(8), 3*3*3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(9), 3*5*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(10), 3*3*3*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(11), 3*5*7*7*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(12), 3*3*3*5*7*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(13), 3*3*5*5*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(14), 3*3*3*3*3*5*7, 'should have worked')
        self.assertEqual(problem_10_7_bis(15), 3*3*5*5*7*7, 'should have worked')

    # Chapter 19. Additional Review Problems: Moderate

    def test_problem_19_1(self):
        a = 1
        b = 2
        (a, b) = problem_19_1(a, b)
        self.assertEqual(a, 2, 'replace value of a with value of b')
        self.assertEqual(b, 1, 'replace value of b with value of a')

    def test_problem_19_2(self):
        table = [
            [1, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ]
        self.assertIsNone(problem_19_2(table), 'no one wins this game')

        table = [
            [1, 1, 1],
            [1, 0, 0],
            [0, 1, 0]
        ]
        self.assertTrue(problem_19_2(table), '1 wins the game')

        table = [
            [0, 1, 1],
            [1, 0, 0],
            [0, 1, 0]
        ]
        self.assertFalse(problem_19_2(table), '0 wins the game')

    def test_problem_19_3(self):
        self.assertEqual(problem_19_3(6), 1, '6! has only 1 trailing zeros')
        self.assertEqual(problem_19_3(10), 2, '10! has only 2 trailing zeros')
        self.assertEqual(problem_19_3(26), 6, '26! has 6 trailing zeros')
        self.assertEqual(problem_19_3(100), 24, '10! has 24 trailing zeros')

    def test_problem_19_4(self):
        self.assertEqual(problem_19_4(10, 5), 10, 'should find max to be 10')
        self.assertEqual(problem_19_4(5, 6), 6, 'should find max to be 6')
        self.assertEqual(problem_19_4(20, 20), 20, 'numbers are equal')

    def test_problem_19_5(self):
        actual = problem_19_5('RGGB', 'YRGB')
        expected = (2, 1)
        self.assertEqual(actual, expected,
            'should return the accurate hits and pseudo-hits')

    def test_problem_19_6(self):
        num = 12
        expected = 'Twelve'
        actual = problem_19_6(num)
        self.assertEqual(actual, expected, 'should print the number in letters')

        num = 67
        expected = 'Sixty Seven'
        actual = problem_19_6(num)
        self.assertEqual(actual, expected, 'should print the number in letters')

        num = 1000
        expected = 'One Thousand'
        actual = problem_19_6(num)
        self.assertEqual(actual, expected, 'should print the number in letters')

        num = 1001
        expected = 'One Thousand, One'
        actual = problem_19_6(num)
        self.assertEqual(actual, expected, 'should print the number in letters')

        num = 123
        expected = 'One Hundred and Twenty Three'
        actual = problem_19_6(num)
        self.assertEqual(actual, expected, 'should print the number in letters')

        num = 99909
        expected = 'Ninty Nine Thousands, Nine Hundreds and Nine'
        actual = problem_19_6(num)
        self.assertEqual(actual, expected, 'should print the number in letters')

        num = 999999
        expected = 'Nine Hundreds and Ninty Nine Thousands, Nine Hundreds and Ninty Nine'
        actual = problem_19_6(num)
        self.assertEqual(actual, expected, 'should print the number in letters')

        num = 1234
        expected = 'One Thousand, Two Hundreds and Thirty Four'
        actual = problem_19_6(num)
        self.assertEqual(actual, expected, 'should print the number in letters')

    def test_problem_19_7(self):
        arr = [2, -8, 3, -2, 4, -10]
        expected = [3, -2, 4]
        actual = problem_16_7(arr)
        self.assertEqual(actual, expected, 'should return the highest sum sequence')

        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        actual = problem_16_7(arr)
        self.assertEqual(actual, expected, 'should return the highest sum sequence')

        arr = [1, 2, -3, 4] # two highest sum lists: [1, 2, -3, 4] and [4]
        expected = [1, 2, -3, 4]
        actual = problem_16_7(arr)
        self.assertEqual(actual, expected, 'should return the highest sum sequence')

        arr = [1, -2] # only one digit in the list
        expected = [1]
        actual = problem_16_7(arr)
        self.assertEqual(actual, expected, 'should return the highest sum sequence')

        arr = [1, -2] # only one digit in the list
        expected = [1]
        actual = problem_16_7(arr)
        self.assertEqual(actual, expected, 'should return the highest sum sequence')

        arr = [-3, -1, -2] # maximum is negative
        expected = [-1]
        actual = problem_16_7(arr)
        self.assertEqual(actual, expected, 'should return the highest sum sequence')
