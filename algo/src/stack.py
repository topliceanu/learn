# -*- coding: utf-8 -*-


class Stack(object):
    """ Implements a simple stack data structure.

    Attrs:
        top: a pointer to the top object in the stack.
    """
    def __init__(self):
        self.top = None

    def pop(self):
        """ Returns the value at the top of the stack. """
        if self.top == None:
            return None

        value = self.top['value']
        self.top = self.top['prev']
        return value

    def push(self, value):
        """ Adds a new value on top of the stack. """
        node = {'value': value, 'prev': None}
        if self.top == None:
            self.top = node
        else:
            node['prev'] = self.top
            self.top = node
