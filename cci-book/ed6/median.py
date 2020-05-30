# -*- coding: utf-8 -*-

from heap import insert, extract_index


class Median(object):
    """Data structure to maintain the median of a list."""
    def __init__(self):
        self.lower_max = []
        self.upper_min = []
        self.median = None

    def insert(self, val):
        insert(self.upper_min, val)
        self._reballance()
        if len(self.lower_max) >= len(self.upper_min):
            self.median = - self.lower_max[0]
        else:
            self.median = self.upper_min[0]

    def _reballance(self):
        if len(self.lower_max) > len(self.upper_min) + 1:
            val = extract_index(self.lower_max, 0)
            insert(self.upper_min, - val)
        if len(self.upper_min) > len(self.lower_max) + 1:
            val = extract_index(self.upper_min, 0)
            insert(self.lower_max, - val)
