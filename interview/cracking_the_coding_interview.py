# -*- coding: utf-8 -*-
from collections import deque
import sys

sys.path.insert(0, '../algo')
from src.stack import Stack

# Chapter 1: Arrays and Strings

def problem_1_1(data):
    """Implement an algorithm to determine if a string has all unique
    characters. What if you can not use additional data structures?

    Returns:
        bool, True if all characters are unique.
    """
    chars = set([])
    for c in data:
        if c in chars:
            return False
        chars.add(c)
    return True

def problem_1_1_bis(data):
    """ Same problem as above but without using the extra set. Solution is to
    use a single long int, where each bit corresponds to a possible character,
    when a character is visited, that bit is set to one.
    """
    class Filter(object):

        def __init__(self):
            self.seen = 0L

        def visit(self, char):
            index = ord(char)
            self.seen = self.seen | (1 << index)

        def is_visited(self, char):
            index = ord(char)
            return self.seen & (1 << index) != 0

    f = Filter()
    for c in data:
        if f.is_visited(c):
            return False
        f.visit(c)
    return True

def problem_1_2(data):
    """ Write code to reverse a C-Style String. (C-String means that “abcd” is
    represented as five characters, including the null character.
    """
    out = []
    for i in range(len(data)-2, -1, -1):
        out.append(data[i])
    out.append(data[len(data)-1])
    return ''.join(out)

def problem_1_3(data):
    """ Design an algorithm and write code to remove the duplicate characters
    in a string without using any additional buffer.
    NOTE: One or two additional variables are fine. An extra copy of the array
    is not.
    FOLLOW UP: Write the test cases for this method.

    Complexity: O(n)

    Idea: - move duplicate chars to the end of the array, this way shortening
        the array can be done without copying the array, just remove the last
        duplicate elements.
    - maintain a group of duplicate characters (no matter the order)
    - pass through all the char in the data, when a duplicate element is found,
        add it to the extra group, ie. update the boundaries, otherwise, move
        extra one character forward towards the end.
    """
    n = len(data)

    if n <= 1:
        return data

    data = list(data)
    extra = {'start': 0, 'end': 0}

    while extra['end'] + 1 < n:
        if data[extra['start']] == data[extra['end'] + 1]:
            # Add data[extra['end']] into the blog, ie. extend the end of blob.
            extra['end'] += 1
        else:
            # Move the blob one index to the left.
            if extra['start'] != extra['end']:
                data[extra['start'] + 1], data[extra['end'] + 1] = \
                    data[extra['end'] + 1], data[extra['start'] + 1]
            extra['start'] += 1
            extra['end'] += 1

    extra_length = extra['end'] - extra['start']
    if extra_length == 0:
        return ''.join(data)
    return ''.join(data[:-extra_length])

def problem_1_4(s1, s2):
    """ Write a method to decide if two strings are anagrams or not.

    Complexity: O(n^2) time but O(n) space (no extra data structure)
    """
    if len(s1) != len(s2):
        return False

    letters = {}
    for c in s1:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1
    for c in s2:
        if c not in letters:
            return False
        letters[c] -= 1
    for (__, count) in letters.iteritems():
        if count > 0:
            return False
    return True

def problem_1_5(data):
    """ Write a method to replace all spaces in a string with ‘%20’ """
    out = []
    for c in data:
        if c == ' ':
            out.append('%20')
        else:
            out.append(c)
    return ''.join(out)

def problem_1_6(arr):
    """ Given an image represented by an NxN matrix, where each pixel in the
    image is 4 bytes, write a method to rotate the image by 90 degrees. Can you
    do this in place?

    Complexity: O(n^2) in time, O(1) extra space, besides the array.
    """
    n = len(arr)
    for i in range(n/2):
        for j in range(i, n - i - 1):
            x = (i, j)
            y = (j, n - i - 1)
            z = (n - i - 1, n - j - 1)
            t = (n - j - 1, i)
            tmp = arr[x[0]][x[1]]
            arr[x[0]][x[1]] = arr[t[0]][t[1]]
            arr[t[0]][t[1]] = arr[z[0]][z[1]]
            arr[z[0]][z[1]] = arr[y[0]][y[1]]
            arr[y[0]][y[1]] = tmp
    return arr

def problem_1_7(arr):
    """ Write an algorithm such that if an element in an MxN matrix is 0, its
    entire row and column is set to 0
    """
    m = len(arr)
    if m == 0:
        return arr
    n = len(arr[0])

    # Step 1: pass through the array and find columns and rows should be zeroed.
    rows = set([])
    cols = set([])
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Step 2: go throuhg each element in the array and turn it to zero if either
    # it's the column or row have be already marked to be zeroed.
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                arr[i][j] = 0
    return arr

def problem_1_8(s1, s2):
    """ Assume you have a method isSubstring which checks if one word is a
    substring of another. Given two strings, s1 and s2, write code to check if
    s2 is a rotation of s1 using only one call to isSubstring (i.e.,
    “waterbottle” is a rotation of “erbottlewat”).
    """
    if s1 == '' or s2 == '':
        return False
    if len(s1) != len(s2):
        return False

    s = s1 * 2
    return s.find(s2) != -1

# Chapter 2: Linked Lists

class SingleLinkedListNode(object):
    """ A node in a single linked list. """
    def __init__(self, key):
        self.key = key
        self.next = None

    def to_list(self):
        out = [self.key]
        if self.next != None:
            out.extend(self.next.to_list())
        return out

    @classmethod
    def from_list(cls, l):
        if len(l) == 0:
            return None
        start = SingleLinkedListNode(l[0])
        node = start
        for i in range(1, len(l)):
            new_node = SingleLinkedListNode(l[i])
            node.next = new_node
            node = new_node
        return start


def problem_2_1(node):
    """ Write code to remove duplicates from an unsorted linked list.
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?
    """
    # This algorithm solves the harder follow-up problem.
    start = node
    while node != None:
        succ = node.next
        while succ != None and succ.key == node.key:
            succ = succ.next
        node.next = succ
        node = succ
    return start

def problem_2_2(start, n):
    """ Implement an algorithm to find the nth to last element of a singly
    linked list.
    """
    if start == None or n < 0:
        raise Exception("Incorrect input params")

    # First step: find the length of the list.
    length = 0
    node = start
    while node != None:
        node = node.next
        length += 1

    if length < n:
        return None

    # Second step: traverse through the target element.
    target = length - n
    i = 0
    node = start
    while True:
        if i == target:
            return node
        node = node.next
        i += 1

def problem_2_3(node):
    """ Implement an algorithm to delete a node in the middle of a single
    linked list, given only access to that node.

    EXAMPLE
    Input: the node ‘c’ from the linked list a->b->c->d->e
    Result: nothing is returned, but the new linked list looks like a->b->d->e
    """
    # Idea is to go through all the rest of the nodes and copy the value from
    # the next node to the current node. Will not work if the last node in the
    # list is given.
    if node == None:
        return
    if node.next == None:
        raise Exception('Cannot remove the last element from the list')

    while node.next.next != None:
        node.key = node.next.key
        node = node.next

    node.key = node.next.key
    node.next = None

def problem_2_4(l1, l2):
    """You have two numbers represented by a linked list, where each node
    contains a single digit. The digits are stored in reverse order, such that
    the 1’s digit is at the head of the list. Write a function that adds the
    two numbers and returns the sum as a linked list.

    EXAMPLE
    Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
    Output: 8 -> 0 -> 8
    """
    node1 = l1
    node2 = l2
    start = None
    out = None
    carry = 0

    while node1 != None or node2 != None:
        s = carry
        if node1 != None:
            s += node1.key
            node1 = node1.next
        if node2 != None:
            s += node2.key
            node2 = node2.next

        if s > 10:
            carry = s / 10
            s = s % 10
        else:
            carry = 0

        out_node = SingleLinkedListNode(s)
        if out == None:
            out = out_node
            start = out
        else:
            out.next = out_node
            out = out_node

    if carry != 0:
        out_node = SingleLinkedListNode(carry)
        out.next = out_node

    return start

def problem_2_5(node):
    """ Given a circular linked list, implement an algorithm which returns node
    at the beginning of the loop.

    DEFINITION
    Circular linked list: A (corrupt) linked list in which a node’s next pointer
    points to an earlier node, so as to make a loop in the linked list.
    EXAMPLE
    input: A -> B -> C -> D -> E -> C [the same C as earlier]
    output: C

    SOLUTION:
    - start two node traversals, one moving one node at a time, the other two
    nodes at a time.
    - if they meet, then the list has a loop, otherwise no loop.
    - the place where they meed is k nodes aways from the start of the loop,
    where k is the number of nodes from the begining of the list to the start of the loop.
    - move one traverser on the begining of the list
    - move both traversers one node at a time until they meet, this is the start of the loop.
    """
    n1 = node # moves one node at a time.
    n2 = node # moves two nodes at a time.

    # Advance to the meeting point or reach the end of the list.
    while n1 != None:
        n1 = n1.next
        n2 = n2.next.next
        if n1 == n2:
            break

    # If either n1 or n2 are None, then we found no loop.
    if n1 == None or n2 == None:
        return None

    # Find the starting point of the loop.
    n1 = node
    while n1 != n2:
        n1 = n1.next
        n2 = n2.next

    return n1

# Chapter 3: Stacks and Queues

def problem_3_1():
    """ Describe how you could use a single array to implement three stacks. """

    class ThreeStacks(object):
        """ Implement three stacks using one array.

        Array is split like so:
        arr[0] - index of the last element in the first stack
        arr[1] - index of the last element in the second stack
        arr[2] - index of the last element in the third stack
        arr[i:i+2] - an entry in a stack, such that:
            arr[i] - stores the id of the stack whose element this belongs to.
            arr[i+1] - stores the index of the previous value in the stack.
            arr[i+2] - stores the actual value of the element in the stack.
        """
        def __init__(self, num_stacks=3):
            self.num_stacks = num_stacks
            self.arr = [None] * self.num_stacks

        def push(self, stack_id, value):
            if not (0 <= stack_id <= self.num_stacks):
                raise Exception("Stack id must be between 0 and number of stacks")
            last_index = self.arr[stack_id]
            self.arr.append(stack_id)
            self.arr.append(last_index)
            self.arr.append(value)
            self.arr[stack_id] = len(self.arr) - 3

        def pop(self, stack_id):
            last_index = self.arr[stack_id]
            if last_index == None:
                return None

            previous_index = self.arr[last_index + 1]
            value = self.arr[last_index + 2]

            self.arr[stack_id] = previous_index
            for i in range(last_index, last_index + 3):
                self.arr[i] = '__'

            return value

    return ThreeStacks

def problem_3_2():
    """ How would you design a stack which, in addition to push and pop, also
    has a function min which returns the minimum element? Push, pop and min
    should all operate in O(1) time.
    """
    class MinStack(object):
        def __init__(self):
            self.values = []
            self.mins = []

        def push(self, value):
            self.values.append(value)
            if len(self.mins) == 0 or value < self.mins[-1]:
                self.mins.append(value)

        def pop(self):
            value = self.values.pop()
            while len(self.mins) > 0 and value >= self.mins[-1]:
                self.mins.pop()
            return value

        def min(self):
            if len(self.mins) == 0:
                return None
            return self.mins[-1]

    return MinStack

def problem_3_3():
    """ Imagine a (literal) stack of plates. If the stack gets too high, it
    might topple. Therefore, in real life, we would likely start a new stack
    when the previous stack exceeds some threshold.

    Implement a data structure SetOfStacks that mimics this. SetOfStacks
    should be composed of several stacks, and should create a new stack once
    the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
    should behave identically to a single stack (that is, pop() should return
    the same values as it would if there were just a single stack). Implement a
    function popAt(int index) which performs a pop operation on a specific
    sub-stack.
    """
    class SetOfStacks(object):
        """
        Attrs:
            limit: int, number of values a single stack can support
            stacks: list, of lists, each acting as a stack.
        """
        def __init__(self, limit):
            self.limit = limit
            self.stacks = []

        def push(self, value):
            """ Pushes a value in the stack of stacks.

            If no stack is present, it will first insert a new empty stack,
            then call itself again to insert the new values.

            Args:
                value: mixed, the value to push into the data structure.
            """
            if len(self.stacks) == 0:
                self.stacks.append([])
                return self.push(value)

            top_stack = self.stacks[-1]
            if len(top_stack) == self.limit:
                self.stacks.append([])
                return self.push(value)

            top_stack.append(value)

        def pop(self):
            """ Pops the last value of the stack of stacks.
            If the top stack is empty, pop it from the stack then try again.
            if stack of stacks is empty return None.
            """
            if len(self.stacks) == 0:
                return None

            top_stack = self.stacks[-1]
            if len(top_stack) == 0:
                self.stacks.pop()
                return self.pop()

            return top_stack.pop()

        def popAt(self, index):
            """ Pop a value from the stack with a given index.

            Args:
                index: int, the index of the user whose values
            """
            if index < 0 or index >= len(self.stacks):
                raise Exception('Cannot accesss stack index')

            stack = self.stacks[index]
            value = stack.pop()

            # Reballance the stacks.
            for i in range(index, len(self.stacks)-1):
                head = self.stacks[i+1][0]
                self.stacks[i+1] = self.stacks[i+1][1:]
                self.stacks[i].append(head)

            return value

    return SetOfStacks

def problem_3_4(rod1, rod2, rod3):
    """In the classic problem of the Towers of Hanoi, you have 3 rods and
    N disks of different sizes which can slide onto any tower. The puzzle
    starts with disks sorted in ascending order of size from top to bottom
    (e.g., each disk sits on top of an even larger one). You have the
    following constraints:
        (A) Only one disk can be moved at a time.
        (B) A disk is slid off the top of one rod onto the next rod.
        (C) A disk can only be placed on top of a larger disk.
    Write a program to move the disks from the first rod to the last using stacks.
    """
    def move_tower(height, fromPole, toPole, withPole):
        if height >= 1:
            move_tower(height-1,fromPole,withPole,toPole)
            toPole.append(fromPole.pop())
            move_tower(height-1,withPole,toPole,fromPole)

    move_tower(len(rod1), rod1, rod3, rod2)
    return (rod1, rod2, rod3)

def problem_3_5():
    """ Implement a MyQueue class which implements a queue using two stacks. """

    class MyQueue(object):
        """
        Attrs:
            for_enqueue: object, instance of algo.src.Stack
            for_dequeue: object, instance of algo.src.Stack
        """
        def __init__(self):
            self.for_enqueue = Stack()
            self.for_dequeue = Stack()

        def __len__(self):
            return len(self.for_enqueue) + len(self.for_dequeue)

        def enqueue(self, value):
            self.for_enqueue.push(value)

        def dequeue(self):
            if len(self.for_dequeue) == 0:
                self._carry_over(self.for_enqueue, self.for_dequeue)
            return self.for_dequeue.pop()

        def _carry_over(self, src, dest):
            while len(src) != 0:
                dest.push(src.pop())

    return MyQueue

def problem_3_6(stack):
    """ Write a program to sort a stack in ascending order. You should not make
    any assumptions about how the stack is implemented. The following are the
    only functions that should be used to write this program:
        push | pop | peek | isEmpty.

    Solution #1: use one more stack.
    Solution #1: no additional stack but using recursion.
    """
    def move_last(stack):
        """ Finds the max element in stack and moves it to to the top. """
        if len(stack) <= 1:
            return stack

        last = stack.pop()
        stack = move_last(stack)
        previous = stack.peek()
        if previous > last:
            previous = stack.pop()
            stack.push(last)
            stack.push(previous)
        else:
            stack.push(last)
        return stack

    def stack_sort(stack):
        if stack.is_empty():
            return stack
        stack = move_last(stack)
        last = stack.pop()
        stack = stack_sort(stack)
        stack.push(last)
        return stack

    return stack_sort(stack)

# Chapter 4: Trees and Graphs

class TreeNode(object):
    """ A node in a tree. """
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

    def is_leaf(self):
        return len(self.children) == 0

def problem_4_1(root):
    """ Implement a function to check if a tree is balanced. For the purposes
    of this question, a balanced tree is defined to be a tree such that no two
    leaf nodes differ in distance from the root by more than one.

    Solution: modify Pre-Order Traversal to collect the depth of each leaf.
    """
    max_leaf_depth = None
    node_stack = [(root, 0)]
    leaf_depths = set([])

    while len(node_stack) != 0:
        (node, depth) = node_stack.pop()
        if node.is_leaf():
            leaf_depths.add(depth)
        else:
            for child in node.children:
                node_stack.append((child, depth + 1))

    return max(leaf_depths) - min(leaf_depths) <= 1

class GraphVertex(object):
    def __init__(self, key):
        self.key = key
        self.adjacent = []

def problem_4_2(start, end):
    """ Given a directed graph, design an algorithm to find out whether there
    is a route between two nodes.
    Solution: Depth-First Search.
    """
    def bfs(start):
        vertex_stack = [start]
        explored_vertices = set([])
        while len(vertex_stack) != 0:
            vertex = vertex_stack.pop()
            explored_vertices.add(vertex.key)
            for neighbour_vertex in vertex.adjacent:
                if neighbour_vertex.key not in explored_vertices:
                    vertex_stack.append(neighbour_vertex)
        return explored_vertices

    explored_nodes = bfs(start)
    return end.key in explored_nodes

def problem_4_3(sorted_arr):
    """ Given a sorted (increasing order) array, write an algorithm to create
    a binary tree with minimal height.
    Solution: minimal height implies perfectly ballanced.
    """
    def build_node(arr, left, right):
        if left > right:
            return None
        middle = int(float(left + right) / 2)
        node = TreeNode(arr[middle])
        left = build_node(arr, left, middle - 1)
        right = build_node(arr, middle + 1, right)
        node.children = [left, right]
        return node

    return build_node(sorted_arr, 0, len(sorted_arr) - 1)

def problem_4_4(tree):
    """ Given a binary search tree, design an algorithm which creates a linked
    list of all the nodes at each depth (i.e., if you have a tree with depth D,
    you’ll have D linked lists).

    Solution: use pre-order traversal to pass through each node and it's depth.
    """
    linked_lists_start = []
    linked_lists_end = []

    node_queue = deque([(tree, 0)])
    while len(node_queue) != 0:
        (node, depth) = node_queue.popleft()
        linked_list_node = SingleLinkedListNode(node)
        if depth == len(linked_lists_start):
            linked_lists_start.append(linked_list_node)
            linked_lists_end.append(linked_list_node)
        else:
            linked_lists_end[depth].next = linked_list_node
            linked_lists_end[depth] = linked_list_node
        for child in node.children:
            node_queue.append((child, depth + 1))

    return linked_lists_start

class BinaryTreeNode(object):
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def problem_4_5(tree):
    """ Write an algorithm to find the ‘next’ node (i.e., in-order successor)
    of a given node in a binary search tree where each node has a link to its
    parent.

    Solution: There are two cases:
    1. the node has a right subtree, in which case his immediate successor is
    the smallest node in the right subtree.
    2. if the node has ane empty right subtree, then go up the ancestors until
    you reach a right one. If you reach the root, then the node has on successor
    because it's the max node.
    """
    def get_min(node):
        if node.left == None:
            return node
        return get_min(node.left)

    def successor(node):
        if node.right != None:
            return get_min(node.right)
        while node != None:
            if node.parent.left == node:
                return node.parent
            node = node.parent
        return None

    return successor(tree)

def problem_4_6(node1, node2):
    """ Design an algorithm and write code to find the first common ancestor of
    two nodes in a binary tree. Avoid storing additional nodes in a data
    structure. NOTE: This is not necessarily a binary search tree.
    """
    n1 = node1
    while n1 != None:
        n2 = node2
        while n2 != None:
            if n2 == n1:
                return n1
            n2 = n2.parent
        n1 = n1.parent
    return None

def problem_4_7(T1, T2):
    """ You have two very large binary trees: T1, with millions of nodes, and
    T2, with hundreds of nodes. Create an algorithm to decide if T2 is a
    subtree of T1.
    """
    def is_identical(t1, t2):
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        return t1.key == t2.key and \
               is_identical(t1.left, t2.left) and \
               is_identical(t1.right, t2.right)

    def is_subtree(t1, t2):
        """ Check if t2 is subtree of t1. """
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        if t1.key == t2.key:
            if is_identical(t1, t2) == True:
                return True
        return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)

    return is_subtree(T1, T2)

def problem_4_8(tree, value):
    """ You are given a binary tree in which each node contains a value. Design
    an algorithm to print all paths which sum up to that value. Note that it
    can be any path in the tree, it does not have to start at the root.
    """
    def find_paths(node, s):
        """ Retrive all paths that sum to s and start with node.
        Once it finds a path it can stop!
        Returns:
            list, of lists, of keys
        """
        if node == None:
            return []

        paths = []
        if node.key == s:
            paths.append([])
        paths.extend(find_paths(node.left, s - node.key))
        paths.extend(find_paths(node.right, s - node.key))
        for p in paths:
            p.insert(0, node.key)
        return paths

    def traverse(node, s):
        """ Find all paths in the tree rooted in node with sum up to s.
        Returns:
            list, of lists of keys which sum up to s.
        """
        if node == None:
            return
        sums = find_paths(node, s)
        if node.left != None:
            sums.extend(traverse(node.left, s))
        if node.right != None:
            sums.extend(traverse(node.right, s))
        return sums

    return traverse(tree, value)

# Chapter 5: Bit Manipulation

def problem_5_1(n, m, i, j):
    """ You are given two 32-bit numbers, N and M, and two bit positions, i and
    j. Write a method to set all bits between i and j in N equal to M (e.g., M
    becomes a substring of  N located at i and starting at j).

    Example:
        Input: N = 10000000000, M = 10101, i = 2, j = 6
        Output: N = 10001010100
    """
    x = ((2**(len(bin(n))-j)-1) << (j+1)) + (2**i - 1)
    return n & x | m << i

def problem_5_2(n):
    """ Given a (decimal - e.g. 3.72) number that is passed in as a string,
    print the binary representation. If the number can not be represented
    accurately in binary, print ERROR.
    """
    out = ''

    # Find the largest power of 2.
    i = 0
    while 2**i < n:
        i += 1
    i -= 1

    # Continuously find the highest power of 2 within the value.
    while n > 0 and i > -20:
        if n >= 2**i:
            out += '1'
            n -= 2**i
        else:
            out += '0'
        if i == 0:
            out += ','
        i -= 1

    if i == -20:
        raise Exception('Cannot be accurately represented')

    return out

def problem_5_3(n):
    """ Given an integer, print the next smallest and next largest number that
    have the same number of 1 bits in their binary representation.

    Returns
        tuple, format (smallest, largest)
    """
    has_no_zero_bits = (n+1) & n == 0
    if has_no_zero_bits:
        raise Exception('There is no smaller number with the same number of bits')

    def count_set_bits(n):
        """ Returns the number of bits set to 1 in input. """
        count = 0
        for i in range(len(bin(n)) - 2):
            if (1 << i) & n != 0:
                count += 1
        return count

    num_bits = count_set_bits(n)

    # Find the next smallest number with the same number of bits.
    next_smallest = n
    while True:
        next_smallest -= 1
        if count_set_bits(next_smallest) == num_bits:
            break

    # Find the next larget number with the same number of bits.
    next_largest = n
    while True:
        next_largest += 1
        if count_set_bits(next_largest) == num_bits:
            break

    return (next_smallest, next_largest)

def problem_5_4():
    """ Explain what the following code does: ((n & (n-1)) == 0)
    Solution: determins if n is a power of 2.
    """

def problem_5_5(a, b):
    """ Write a function to determine the number of bits required to convert
    integer A to integer B.
    Input: 31, 14
    Output: 2

    Solution: compute (a XOR b) and produce the number of 1 bits in the result.
    """
    def num_set_bits(n):
        count = 0
        while n != 0:
            last_bit = n & 1
            if last_bit == 1:
                count += 1
            n = n >> 1
        return count

    return num_set_bits(a ^ b)

def problem_5_6(n):
    """ Write a program to swap odd and even bits in an integer with as few
    instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit
    3 are swapped, etc).
    """
    def is_set_bit(x, i):
        return (x & (1 << i)) != 0

    def toggle_bit(x, i):
        return (x ^ (1 << i))

    def reverse(x, i):
        """ Reverses bit i with bit i+1 in number x. """
        i_is_set = is_set_bit(x, i)
        j_is_set = is_set_bit(x, i+1)
        if (not i_is_set and j_is_set) or (i_is_set and not j_is_set):
            x = toggle_bit(x, i)
            x = toggle_bit(x, i+1)
        return x

    num_bits = len(bin(n)) - 2
    for i in range(0, num_bits, 2):
        n = reverse(n, i)
    return n

def problem_5_7(arr):
    """ An array A[1...n] contains all the integers from 0 to n except for one
    number which is missing. In this problem, we cannot access an entire
    integer in A with a single operation. The elements of A are represented in
    binary, and the only operation we can use to access them is “fetch the jth
    bit of A[i]”, which takes constant time. Write code to find the missing
    integer. Can you do it in O(n) time?

    Solution:
    - first sort the ints, being mostly consecutive ints, radix sort will work in O(n).
    - second, iterate through all of them to find two number which are not consecutive.
    """
    def fetch_bit(arr, i, j):
        """ Returns the bit j in the ith number in arr. """
        return (arr[i] & (1 << j)) != 0

    def radix_sort(arr):
        """ Sorts a list of ints in-place using the radix-search method. """
        return arr

    def is_offset(arr, i):
        """ Figures out is the position i in arr has the value i. """
        different_bits = i ^ (i+1)
        bit_index = 0
        while different_bits != 0:
            last_bit = different_bits & 1
            if last_bit == 1:
                if fetch_bit(arr, i, bit_index) == 1:
                    return False
            different_bits = different_bits << 0
        return True

    sorted_arr = radix_sort(arr)
    for i in range(len(sorted_arr)):
        if is_offset(sorted_arr, i):
            return i - 1

# Chapter 8: Recursion

def problem_8_1(x):
    """ Write a method to generate the nth Fibonacci number. """
    def fib(n):
        if n < 0:
            raise Exception('No fibonacci number below 0')
        if n == 0 or n == 1:
            return 1
        return fib(n-1) + fib(n-2)

    return fib(x)

def problem_8_2(n):
    """Imagine a robot sitting on the upper left hand corner of an NxN grid.
    The robot can only move in two directions: right and down. How many
    possible paths are there for the robot?

    FOLLOW UP
    Imagine certain squares are “off limits”, such that the robot can not step
    on them. Design an algorithm to get all possible paths for the robot.
    """
    def paths(i, j):
        if i == 0 or j == 0:
            return 1 # The bot just gets dumped at the begining of the track.
        return paths(i-1, j) + paths(i, j-1)

    return paths(n-1, n-1)

def problem_8_2_bis(grid):
    """ Folowup to the previous question:
    Imagine certain squares are “off limits”, such that the robot can not step
    on them. Design an algorithm to get all possible paths for the robot.
    """
    OFF_LIMITS = 1
    def paths(grid, i, j):
        """ Returns a list of lists of paths to get to position (i, j). """
        if i == 0 and j == 0:
            return [[(0, 0)]]

        so_far = []
        if j == 0 and i != 0: # On the left border.
            if grid[i-1][j] != OFF_LIMITS:
                so_far.extend(paths(grid, i-1, j))
        elif j != 0 and i == 0: # On the top border.
            if grid[i][j-1] != OFF_LIMITS:
                so_far.extend(paths(grid, i, j-1))
        else: # Somewhere in the middle of the screen.
            if grid[i][j-1] != OFF_LIMITS:
                so_far.extend(paths(grid, i, j-1))
            if grid[i-1][j] != OFF_LIMITS:
                so_far.extend(paths(grid, i-1, j))

        for p in so_far:
            p.append((i, j))
        return so_far

    # Compute all paths ending in the bottom-right corner.
    n = len(grid)
    all_paths = paths(grid, n-1, n-1)
    return all_paths

def problem_8_3(data):
    """ Write a method that returns all subsets of a set.

    Complexity: O(2^n)
    """

    def subsets(s):
        """ Returns a list of sets given the input set. """
        if len(s) == 0:
            return [set()]

        head = s.pop()
        subs = subsets(s)
        out = subs[:]

        for sub in subs:
            tmp = set(sub)
            tmp.add(head)
            out.append(tmp)

        return out

    return subsets(data)

def problem_8_4(data):
    """ Write a method to compute all permutations of a string. """

    def inject(letter, s):
        """ Inserts a given letter in evey possion of s. Complexity: O(n^2). """
        out = []
        for i in range(len(s)+1):
            t = s[:i]+letter+s[i:]
            out.append(t)
        return out

    def permutations(s):
        """ Compute all permutation of a given string s, recursively by
        computing the permutations of the string without the first letter,
        then injecting the letter in evey possible locations.
        """
        if len(s) == 1:
            return [s]

        head = s[0]
        tail = s[1:]
        perms = permutations(tail)

        out = []
        for p in perms:
            out.extend(inject(head, p))
        return out

    return permutations(data)

def problem_8_5(n):
    """ Implement an algorithm to print all valid (e.g., properly opened and
    closed) combinations of n-pairs of parentheses.

    EXAMPLE:
    input: 3 (e.g., 3 pairs of parentheses)
    output: ['()()()', '()(())', '(())()', '((()))']
    """
    def parantheses(n):
        """ Composes n pairs of parantheses correctly.
        Returns:
            list, of strings
        """
        if n == 1:
            return ['()']

        subs = parantheses(n-1)
        out = []
        for s in subs:
            out.append('()'+s)
            out.append('('+s+')')
            out.append(s+'()')
        out = list(set(out))
        return out

    return parantheses(n)

def problem_8_6(canvas, point, new_color):
    """ Implement the "paint fill" function that one might see on many image
    editing programs. That is, given a screen (represented by a 2 dimensional
    array of Colors), a point, and a new color, fill in the surrounding area
    until you hit a border of that color.

    Solution: flood-fill algorithms (or a more efficient line-fill).
    """
    def fill(canvas, point, current_color, new_color):
        (x, y) = point

        if canvas[x][y] != current_color:
            return
        canvas[x][y] = new_color

        n = len(canvas)
        m = len(canvas[0])

        if x - 1 >= 0: # up.
            fill(canvas, (x-1, y), current_color, new_color)
        if x + 1 < n: # down.
            fill(canvas, (x+1, y), current_color, new_color)
        if y - 1 >= 0: # left.
            fill(canvas, (x, y-1), current_color, new_color)
        if y + 1 < m: # right.
            fill(canvas, (x, y+1), current_color, new_color)

    current_color = canvas[point[0]][point[1]]
    return fill(canvas, point, current_color, new_color)

def problem_8_7(cents):
    """ Given an infinite number of quarters (25 cents), dimes (10 cents),
    nickels (5 cents) and pennies (1 cent), write code to calculate the number
    of ways of representing n cents.
    """
    smaller_vals = {
        25: 10,
        10: 5,
        5: 1
    }

    def num_combinations(change, val):
        """ Count the number of combination of value which sum up to change.
        Args:
            change: int,
            val: int, one of 25, 10, 5 or 1
        Returns:
            int, the number of combinations.
        """
        if val == 1: # Only one way to return change using only pennies.
            return 1

        # Compute the change using smaller values first.
        smaller_val = smaller_vals[val]
        ways = num_combinations(change, smaller_val)

        # Compute change using current value and
        times = change / val
        for i in range(times):
            ways += num_combinations(change - i*val, smaller_val)

        return ways

    return num_combinations(cents, 25)

def problem_8_8(num_queens):
    """ Write an algorithm to print all ways of arranging eight queens on a
    chess board so that none of them share the same row, column or diagonal.

    Solution: use recursive backtracking to compute all combinations.
    """
    def expand_solution(solution, num):
        """ Expands the current solution by adding another queen.
        Only produces valid partial solutions.
        """
        taken_columns = set([c for c in solution])
        taken_first_diagonals = set([i+j for (i, j) in enumerate(solution)])
        taken_second_diagonals = set([j-i for (i, j) in enumerate(solution)])
        i = len(solution)

        candidates = []
        for j in range(num):
            if j in taken_columns or \
               i+j in taken_first_diagonals or \
               j-i in taken_second_diagonals:
                continue
            tmp = solution[:]
            tmp.append(j)
            candidates.append(tmp)
        return candidates

    def recurse(partial_solution, size):
        if len(partial_solution) == size:
            return [partial_solution]

        solutions = []
        for candidate in expand_solution(partial_solution, size):
            solutions.extend(recurse(candidate, size))
        return solutions

    return recurse([], num_queens) # No queen is positioned in initial solution.

# Chapter 9: Sorting and Searching

def problem_9_1(arr1, arr2):
    """ You are given two sorted arrays, A and B, and A has a large enough
    buffer at the end to hold B. Write a method to merge B into A in sorted
    order.
    """
    m = len(arr2) - 1
    p = len(arr1) - 1
    n = len(arr1) - len(arr2) - 1

    while n >= 0 and m >= 0:
        if arr1[n] > arr2[m]:
            arr1[p] = arr1[n]
            n -= 1
        else:
            arr1[p] = arr2[m]
            m -= 1
        p -= 1

    if n < 0:
        while p >= 0:
            arr1[p] = arr2[m]
            p -= 1
            m -= 1
    if m < 0:
        while p >= 0:
            arr1[p] = arr2[n]
            p -= 1
            n -= 1

    return arr1

def problem_9_2(arr):
    """ Write a method to sort an array of strings so that all the anagrams
    are next to each other.
    """
    def is_anagram(x, y):
        letters = {}
        for l in x:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
        for l in y:
            if l not in letters:
                return False
            else:
                letters[l] -= 1
            if letters[l] == 0:
                del letters[l]
        return len(letters) == 0

    def str_compare(x, y):
        if is_anagram(x, y):
            return 0
        else:
            return cmp(x, y)

    return sorted(arr, cmp=lambda x, y: str_compare(x, y))

def problem_9_3(arr, key):
    """ Given a sorted array of n integers that has been rotated an unknown
    number of times, give an O(log n) algorithm that finds an element in the
    array. You may assume that the array was originally sorted in increasing
    order.

    Example:
    Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
    Output: 8 (the index of 5 in the array)

    Solution: There are two rotation cases:
    i.  [8,9,1,2,3,4,5,6,7] - inflexion point is before middle.
    ii. [3,4,5,6,7,8,9,1,2] - inflexion point is after middle.

    Use modified divide and conquer binary search. There are 8 cases
    defined by comparing the key with left, right and middle positions. Thus
    identify the rotation case and recurse on the appropriate array.
    """
    def modified_binary_search(arr, key, left, right):
        if left > right:
            return None

        middle = (left + right) / 2

        if arr[middle] == key:
            return middle

        if arr[left] <= arr[middle]:
            if key > arr[middle]:
                return modified_binary_search(arr, key, middle+1, right)
            elif key >= arr[left]:
                return modified_binary_search(arr, key, left, middle-1)
            else:
                return modified_binary_search(arr, key, middle+1, right)
        elif key < arr[middle]:
            return modified_binary_search(arr, key, left, middle-1)
        elif key <= arr[right]:
            return modified_binary_search(arr, key, middle+1, right)
        else:
            return modified_binary_search(arr, key, left, middle-1)
        return None

    return modified_binary_search(arr, key, 0, len(arr) - 1)

def problem_9_4(lines):
    """ If you have a 2 GB file with one string per line, which sorting
    algorithm would you use to sort the file and why?

    Solution: a variant of merge sort, it can be optimized to read a full chunk
    from the disk at a time.
    """

def problem_9_5(words, word):
    """ Given a sorted array of strings which is interspersed with empty
    strings, write a method to find the location of a given string.

    Example: find “ball” in [“at”, “”, “”, “”, “ball”, “”, “”, “car”, “”, “”, “dad”, “”, “”] will return 4
    Example: find “ballcar” in [“at”, “”, “”, “”, “”, “ball”, “car”, “”, “”, “dad”, “”, “”] will return -1

    Solution: variant of binary search, whereby you ignore the empty spaces.
    """
    # TODO understand how this one works!

    def modified_binary_search(arr, key, left, right):
        if left > right:
            return -1

        # Discover a middle index whose value is not an empty string, first we
        # go left, then right in this search.
        middle = (left + right) / 2
        if arr[middle] == '':
            while arr[middle] == '' and left <= middle:
                middle -= 1
            while arr[middle] == '' and middle <= right:
                middle +=1

        if arr[middle] == key:
            return middle
        if arr[middle] < key:
            return modified_binary_search(arr, key, left, middle-1)
        else:
            return modified_binary_search(arr, key, middle+1, right)

    return modified_binary_search(words, word, 0, len(words)-1)

def problem_9_6(matrix, key):
    """ Given a matrix in which each row and each column is sorted, write a
    method to find an element in it. Matrix is size M*N such that each row is
    sorted left to right and each column is sorted top to bottom.

    Solution: divide and conquer.
    """
    m = len(matrix)
    n = len(matrix[0])
    i = 0 # traversed rows.
    j = n - 1 # traverses columns.

    while i < m and j >= 0:
        if key == matrix[i][j]:
            return True
        elif key < matrix[i][j]: # key will be smaller then matrix[..][j]
            j -= 1
        else: # key will larger than matrix[i][...]
            i += 1

    return False

def problem_9_7(pairs):
    """ A circus is designing a tower routine consisting of people standing
    atop one another’s shoulders. For practical and aesthetic reasons, each
    person must be both shorter and lighter than the person below him or her.
    Given the heights and weights of each person in the circus, write a method
    to compute the largest possible number of people in such a tower.

    EXAMPLE:
    Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
    Output: The longest tower is length 6 and includes from top to bottom:
        (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)
    """
    # TODO implement this one!


# Chapter 10: Mathematical

def problem_10_4(operator, operand1, operand2):
    """ Write a method to implement *, - , / operations.
    You should use only the + operator
    """
    def multiply(x, y):
        """ Implement x * y using only +. """
        i = 0
        out = 0
        while i < y:
            i += 1
            out += x
        return out

    def subtract(x, y):
        """ Implement x - y using only +. """
        i = 0
        while i + y < x:
            i += 1
        return i

    def divide(x, y):
        """ Implement x / y using only +. """
        s = y
        out = 0
        while s < x:
            s += y
            out += 1
        return out

    if operator == '*':
        return multiply(operand1, operand2)
    elif operator == '-':
        return subtract(operand1, operand2)
    elif operator == '/':
        return divide(operand1, operand2)
    elif operator == '+':
        return operand1 + operand2

def problem_10_5(square1, square2):
    """ Given two squares on a two dimensional plane, find a line that would
    cut these two squares in half.

    Solution: Compute the ecuation of the line passing through the center of
    the two squares.

    Args:
        square1: tuple, of dicts, format ({x, y}, {x, y})
        square2: tuple, of dicts, format ({x, y}, {x, y})

    Returns:
        tuple, format (sloape, intercept)
    """
    (p1, p2) = square1
    (p3, p4) = square2

    c1 = {'x': float(p1['x'] + p2['x']) / 2, 'y': float(p1['y'] + p2['y']) / 2}
    c2 = {'x': float(p3['x'] + p4['x']) / 2, 'y': float(p3['y'] + p4['y']) / 2}

    slope = float(c2['y'] - c1['y']) / (c2['x'] - c1['x'])
    intercept = float(p1['y'] * p2['x'] - p1['x'] * p2['y']) / (p2['x'] - p1['x'])

    return (slope, intercept)

def problem_10_6(points, precision=4):
    """ Given a two dimensional graph with points on it, find a line which
    passes the most number of points.

    Solution: compute the line params (sloape, intercept) for all pairs of
    points in the set. Then aggregate all points that share the same line.

    Complexity: O(n^2)

    Params:
        points: list of points, format [(x, y)]
        precision: int, number of decimals to consider.

    Returns:
        set, of points, format {(x, y)}
    """
    def compute_line(p, q, precision):
        if q[0] - p[0] == 0:
            slope = 0
        else:
            slope = (q[1] - p[1])/float(q[0] - p[0])
        intercept = p[1] - p[0]*slope
        return (round(slope, precision), round(intercept, precision))

    n = len(points)
    lines = {}
    for i in range(n-1):
        for j in range(i+1, n):
            line = compute_line(points[i], points[j], precision)
            if line not in lines:
                lines[line] = {points[i], points[j]}
            else:
                lines[line].add(points[i])
                lines[line].add(points[j])

    (__, colinear_points) = max(lines.iteritems(), key=lambda t: len(t[1]))
    return colinear_points

def problem_10_7(k):
    """ Design an algorithm to find the kth number such that the only prime
    factors are 3, 5, and 7.

    Params:
        k: int, the index of the number to add.

    Returns:
        int
    """
    # TODO fix this!

    if k < 0:
        return 0

    index = 0
    base = 3*5*7
    power = 0
    factors = [1, 3, 5, 7, 3*3, 3*5, 3*7, 5*5, 3*3*3, 5*7, 5*3*3, 7*7, 7*3*3]
    number = base

    while index <= k:
        factor = factors[index % len(factors)]
        if index % len(factors) == 0:
            power += 1
        number = (base ** power) * factor
        index += 1

    return number

def problem_10_7_bis(k):
    """ Same problem as above but with a correct and elegant solution. """
    if k == 0:
        return 3*5*7

    q3 = [3*3*5*7]
    q5 = [3*5*5*7]
    q7 = [3*5*7*7]

    index = 0
    while index != k:
        index += 1
        number = min(q3[0], q5[0], q7[0])


        if number == q7[0]:
            q7 = q7[1:]
        else:
            if number == q5[0]:
                q5 = q5[1:]
            else:
                q3 = q3[1:]
                q3.append(number*3)
            q5.append(number*5)
        q7.append(number*7)

    return number

# Chapter 19. Additional Review Problems: Moderate

def problem_19_1(x, y):
    """ Write a function to swap a number in place without temporary variables. """
    # Bit-wise operations.
    #x = x ^ y
    #y = x ^ y
    #x = x ^ y
    #return (x, y)

    # Arithmetic operations.
    x = x - y
    y = y + x
    x = y - x
    return (x, y)

def problem_19_2(table):
    """ Design an algorithm to figure out if someone has won in a game of
    tic-tac-toe.

    Complexity: O(n^2)
    Args:
        table: list of list, dimentions NxN, filled with 1s and 0s
    Returns:
        boolean, True if 1 wins or False if 0 wins.
    """
    n = len(table)
    sum_cols = [0] * n
    sum_rows = [0] * n
    sum_diag = [0] * 2

    for row in range(n):
        for col in range(n):
            sum_rows[row] += table[row][col]
            sum_cols[col] += table[row][col]
            if row == col:
                sum_diag[0] += table[row][col]
            if row == n - col:
                sum_diag[1] += table[row][col]

    for sum_col in sum_cols:
        if sum_col == n:
            return True
        elif sum_col == 0:
            return False

    for sum_row in sum_rows:
        if sum_row == n:
            return True
        elif sum_row == 0:
            return False

    for i in range(2):
        if sum_diag[i] == n:
            return True
        elif sum_diag[i] == 0:
            return False

    return None

def problem_19_3(n):
    """ Write an algorithm which computes the number of trailing zeros in
    n factorial.

    Solution: It's enough to count the power of 5 in the factoring of n!
    That is the number of trailing zeros.
    """
    cache = {}

    def get_pow_5(n):
        if n % 5 != 0:
            return 0
        if n in cache:
            return cache[n]
        pow_5 = 1 + get_pow_5(n/5)
        cache[n] = pow_5
        return pow_5

    # Trailing zeroes are composed of multiples of 2 and 5.
    count_pow_5 = 0
    for i in range(2, n+1):
        pow_5 = get_pow_5(i)
        count_pow_5 += pow_5

    return count_pow_5

def problem_19_4(a, b):
    """ Write a method which finds the maximum of two numbers. You should not
    use if-else or any other comparison operator.

    Example: input: 5, 10; output: 10

    Solution: identify the first bit which is different in the two numbers. The
    number which has that bit set to 1 is larger.
    """
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    bin_len = max(len(bin_a), len(bin_b))
    bin_a = '0'*(bin_len-len(bin_a))+bin_a
    bin_b = '0'*(bin_len-len(bin_b))+bin_b

    for i in range(bin_len):
        if bin_a > bin_b:
            return a
        elif bin_b > bin_a:
            return b
    return a # Drawn.

def problem_19_5(solution, guess):
    """ The Game of Master Mind is played as follows:

    The computer has four slots containing balls that are red (R), yellow (Y),
    green (G) or blue (B). For example, the computer might have RGGB (e.g.,
    Slot #1 is red, Slots #2 and #3 are green, Slot #4 is blue).

    You, the user, are trying to guess the solution. You might, for example,
    guess YRGB. When you guess the correct color for the correct slot, you get
    a “hit”. If you guess a color that exists but is in the wrong slot, you get
    a “pseudo-hit”. For example, the guess YRGB has 2 hits and one pseudo hit.

    For each guess, you are told the number of hits and pseudo-hits.

    Write a method that, given a guess and a solution, returns the number of
    hits and pseudo hits.

    Complexity: O(n)

    Returns:
        tuple, format (hits, pseudo_hits)
    """
    if len(solution) != len(guess):
        raise Exception('Inputs are wrong')

    hits = 0
    pseudo_hits = 0
    missed = {
        'solution': {},
        'guess': {}
    }

    for i in range(len(solution)):
        a = solution[i]
        b = guess[i]
        if a == b:
            hits += 1
        else:
            if a not in missed['solution']:
                missed['solution'][a] = 1
            else:
                missed['solution'][a] += 1
            if b not in missed['guess']:
                missed['guess'][b] = 1
            else:
                missed['guess'][b] += 1

    for (char, count) in missed['solution'].iteritems():
        if char in missed['guess']:
            pseudo_hits += min(missed['solution'][char], missed['guess'][char])

    return (hits, pseudo_hits)

def problem_19_6(n):
    """ Given an integer between 0 and 999,999, print an English phrase that
    describes the integer (eg, “One Thousand, Two Hundred and Thirty Four”).
    """
    words = {
        0:    'Zero',
        1:    'One',
        2:    'Two',
        3:    'Three',
        4:    'Four',
        5:    'Five',
        6:    'Six',
        7:    'Seven',
        8:    'Eight',
        9:    'Nine',
        10:   'Ten',
        11:   'Eleven',
        12:   'Twelve',
        13:   'Thirteen',
        14:   'Fourteen',
        15:   'Fifteen',
        16:   'Sixteen',
        17:   'Seventeen',
        18:   'Eighteen',
        19:   'Nineteen',
        20:   'Twenty',
        30:   'Thirty',
        40:   'Fourty',
        50:   'Fifty',
        60:   'Sixty',
        70:   'Seventy',
        80:   'Eighty',
        90:   'Ninty',
        100:  'Hundred',
        1000: 'Thousand'
    }

    def digits(n):
        if n == 0:
            return ''
        return words[n]

    def tens(n):
        if n < 10:
            return digits(n)
        if n in words:
            return words[n]

        first = n / 10
        return words[first*10] + ' ' + digits(n % 10)

    def hundreds(n):
        if n < 100:
            return tens(n)
        first = n / 100

        if first == 0:
            return tens(n % 100)
        else:
            word = 'Hundred' if first == 1 else 'Hundreds'
            out = words[first] + ' ' + word
            rest = tens(n % 100)
            if rest != '':
                out += ' and ' + rest
            return out

    def thousands(n):
        if n > 999999:
            raise Exception('Input number is too large')
        if n < 1000:
            return hundreds(n)

        word = 'Thousands' if n > 1999 else 'Thousand'
        out = hundreds(n / 1000) + ' ' + word

        rest = hundreds(n % 1000)
        if rest != '':
            out += ', ' + rest
        return out


    return thousands(n)

def problem_16_7(arr):
    """ You are given an array of integers (both positive and negative). Find the continuous sequence with the largest sum. Return the sum.
    Example:
    Input: {2, -8, 3, -2, 4, -10}
    Output: 5 (i.e., {3, -2, 4} )

    Solution: dynamic programming.
    """
