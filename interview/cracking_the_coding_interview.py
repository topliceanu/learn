# -*- coding: utf-8 -*-
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

# BIT MANIPULATION

def problem_5_1(n, m, i, j):
    """ You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a
    method to set all bits between i and j in N equal to M (e.g., M becomes a substring of
    N located at i and starting at j).

    Example:
        Input: N = 10000000000, M = 10101, i = 2, j = 6
        Output: N = 10001010100
    """
    all_ones = 2**33 - 1
    left = all_ones - ((1 << (j+1)) - 1)
    right = (1 << i) - 1
    mask = left | right
    output = (n & mask) ^ (m << i)
    return output

def problem_5_2(n):
    """ Given a (decimal - e.g. 3.72) number that is passed in as a string,
    print the binary representation. If the number can not be represented
    accurately in binary, print ERROR.
    """
    # TODO

def problem_10_6(points, precision=4):
    """ Given a two dimensional graph with points on it, find a line which
    passes the most number of points.

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

    NOTE: THIS IS INCORRECT!

    Params:
        k: int, the index of the number to add.

    Returns:
        int
    """
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
