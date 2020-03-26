# -*- coding: utf-8 -*-


class Queue(object):
    """ Implement a queue data structure, ie. FIFO.

    Attrs:
        head: head of the queue.
        tail: tail of the queue.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = {'value': value, 'prev': None}

        if self.head == None:
            self.head = self.tail = node
        else:
            self.head['prev'] = node
            self.head = node

    def dequeue(self):
        if self.tail == None:
            return None

        value = self.tail['value']
        self.tail = self.tail['prev']
        if self.tail == None:
            self.head = None
        return value
