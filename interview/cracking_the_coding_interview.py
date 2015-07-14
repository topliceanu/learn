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
    """
    n = len(arr)
    for i in range(n/2):
        for j in range(i, n - i):
            x = (i, j)
            y = ()
    return arr

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

# Problem 3.3
class StackOfStacks(object):
    """ Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would likely start a new stack when the previous stack exceeds
    some threshold. Implement a data structure SetOfStacks that mimics this. SetOf-
    Stacks should be composed of several stacks, and should create a new stack once
    the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
    behave identically to a single stack (that is, pop() should return the same values as it
    would if there were just a single stack).
    Implement a function popAt(int index) which performs a pop operation on a specific
    sub-stack.

    Attrs:
        limit: int, number of values a single stack can support
        stacks: object, instance of algo.src.Stack

    TODO this needs further testing.
    """
    def __init__(self, limit):
        self.limit = limit
        self.stacks = Stack()

    def pop(self):
        """ Pops a value from the stack of stacks. """
        if len(self.stacks) == 0:
            return None

        if len(self.stacks) == 1:
            return self.stacks.peek().pop()

        top_stack = self.stacks.peek()
        value = top_stack.pop()
        if value == None:
            self.stacks.pop()
            return self.stacks.peek().pop()
        else:
            return value

    def push(self, value):
        """ Pushes a value in the stack of stacks. """
        if len(self.stacks) == 0:
            new_stack = Stack()
            new_stack.push(value)
            self.stacks.push(new_stack)
            return

        top_stack = self.stacks.peek()
        if len(top_stack) == self.limit:
            new_stack = Stack()
            new_stack.push(value)
            self.stacks.push(new_stack)
        else:
            top_stack.push(value)

# Problem 3.5

class MyQueue(object):
    """ Implement a MyQueue class which implements a queue using two stacks.

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
        if len(self.for_dequeue) != 0:
            return self.for_dequeue.pop()
        self._carry_over(self.for_enqueue, self.for_dequeue)
        return self.for_dequeue.pop()

    def _carry_over(self, src, dest):
        while len(src) != 0:
            dest.push(src.pop())
