# -*- coding: utf-8 -*-


class DynamicallyResizeArray(object):
    """ Implementation for an array who's size does not have to be precomputed.
    A.k.a. ArrayList.

    When the array is full, and the client want's to insert a new element into
    a full array, a new array is created, twice the size of the original array,
    all data is copied over, the new value is also inserted.

    This expensive operation is amortized by the ratio of fast gets and inserts
    which the array supports.
    """
    def __init__(self):
        self.size = 4
        self.data = [None] * self.size

    def insert(self, index, value):
        if len(self.data) == self.size:
            self._enlarge()
        self.data.insert(index, value)

    def remove(self, index):
        self.data.remove(index)
        self._shrink()

    def _enlarge(self):
        new = []
        for i in self.data:
            new.append(self.data[i])
        for i in range(len(self.data)):
            new.append(None)
        self.data = new

    def _shrink(self):
        if len(self.data) > self.size / 2:
            return
        new = []
        for i in self.data:
            new.append[i]
        self.data = new
