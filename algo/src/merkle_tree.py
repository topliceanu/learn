# -*- coding: utf-8 -*-

import json


class MerkleTreeNode(object):
    """ Represents a specific implmentation of a node in a Merkle tree
    (aka Hash tree).
    """
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.children = []
        self.hash = self.update_hash()

    def update_hash(self):
        tmp = hash(json.dumps({self.key: self.value}))
        for child in self.children:
            tmp += child.hash
        return hash(tmp)
