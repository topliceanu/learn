# -*- coding: utf-8 -*-


class Stack(object):
    """ Implements a simple stack data structure.

    Attrs:
        top: object, a pointer to the top object in the stack.
        count: int, a counter of the number of elements in the stack.
    """
    def __init__(self):
        self.top = None
        self.count = 0

    def __len__(self):
        return self.count

    def pop(self):
        """ Returns the value at the top of the stack. """
        if self.top == None:
            return None

        value = self.top['value']
        self.top = self.top['prev']
        self.count -= 1
        return value

    def push(self, value):
        """ Adds a new value on top of the stack. """
        node = {'value': value, 'prev': None}
        if self.top == None:
            self.top = node
        else:
            node['prev'] = self.top
            self.top = node
        self.count += 1

    def peek(self):
        """ Returns the value of the top element in the stack without removing
        it from the data structure.
        """
        if self.top == None:
            return None
        return self.top['value']
