# -*- coding: utf-8 -*-


class MultiMap(object):
    """ Implements a multimap datastructure using a dict where values are lists.

    Attrs:
        table: dict, format {key:[values]}
    """

    def __init__(self):
        self.table = {}

    def set(self, key, value):
        """ Adds a new value to the given key. """
        if key not in self.table:
            self.table[key] = []
        self.table.append(value)

    def get(self, key):
        """ Returns the values corresponding to key.

        Returns:
            list, the values corresponding to key.
        """
        if key not in self.table:
            raise Exception('Key {k} not present'.format(k=key))
        return self.table[key]

    def remove(self, key, value=None):
        """ Removes a key (or a key/value pair) from the data structure.

        Args:
            key: str
            value: mixed, if value is present it will look for that value and
                remove it. If, after removal the list associated with key is
                empty, it will remove the key as well. If value is None, it
                will remove the entire key.
        """
        if key not in self.table:
            return
        if value == None:
            del self.table[key]
            return
        if value not in self.table[key]:
            return
        self.table[key].remove(value)
        if len(self.table[key]) == 0:
            del self.table[key]
