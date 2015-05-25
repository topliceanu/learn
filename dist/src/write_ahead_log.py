# -*- coding: utf-8 -*-

import json


class WAL(object):
    """ Implements write-ahead logging functionality. """

    def __init__(self, redo_path, undo_path):
        self.redo_path = redo_path
        self.undo_path = undo_path
        self.transaction_counter = 0

    def create(self, new_object):
        """ Called when a new object is created. """

    def update(self):
        """ Called when an existing object is udpated. """
        pass

    def delete(self):
        """ Called when an existing object is removed. """
        pass
