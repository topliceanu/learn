# -*- coding: utf-8 -*-

class VectorClock(object):

    def __init__(self):
        self.value = None
        self.revisions = []
        pass

    def update(self, new_value, revision_owner):
        self.value = new_value

        for rev in self.revisions:
            if rev[0] == revision_owner:
                rev[1] += 1
                return

        self.revisions.append([revision_owner, 1])
