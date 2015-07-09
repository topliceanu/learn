# -*- coding: utf-8 -*-


class Item(object):
    """ An item in the double linked list. """
    def __init__(self, value):
        self.value = value
        self.pred = None
        self.succ = None

    def set_pred(self, item):
        """ Sets the given item as the predecessor of current item. """
        self.pred = item
        item.succ = self

class DoubleLinkedList(object):
    """ Implements a double linked list. This exposes the endpoints for read,
    remove and append.
    """
    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0

    def peek_head(self, value):
        if self.head == None:
            return None
        return self.head.value

    def peek_last(self, value):
        if self.last == None:
            return None
        return self.last.value

    def insert_head(self, value):
        """ Insert new value in the front of the list. """
        new_item = Item(value)
        self.count += 1

        if self.is_empty():
            self.head = self.last = new_item
            return

        self.head.set_pred(new_item)
        self.head = new_item


    def insert_last(self, value):
        """ Insert new value after the last element of the list. """
        new_item = Item(value)
        self.count += 1

        if self.is_empty():
            self.head = self.last = new_item
            return

        new_item.set_pred(self.last)
        self.last = new_item

    def is_empty(self):
        """ Returns True if the list is empty, False otherwise. """
        return self.head == None and self.last == None

    def remove_head(self):
        """ Removes the element from the head of the list. """
        if self.is_empty():
            return None

        output = self.head.value
        has_one_element = self.head == self.last
        self.count -= 1

        if has_one_element:
            self.head = self.last = None
            return output

        self.head = self.head.succ
        self.head.pred = None
        return output

    def remove_last(self, value):
        """ Removes the last element from the list. """
        if self.is_empty():
            return None

        output = self.last.value
        has_one_element = self.head == self.last
        self.count -= 1

        if has_one_element:
            self.head = self.last = None
            return output

        self.last = self.last.pred
        self.last.succ = None
        return output

    def __len__(self):
        """ Returns the number of elements in the double linked list. """
        return self.count
