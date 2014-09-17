# -*- coding: utf8 -*-

class UnionFind(object):
    """ Data structure which allows constant time checks to get the leader of
    a given element. Also called disjoined-set or merge-find.

    Reference implementations:
    https://www.ics.uci.edu/~eppstein/PADS/UnionFind.py
    Pseudo code borrowed from:
    http://en.wikipedia.org/wiki/Disjoint-set_data_structure

    Attributes:
        leader: dict, a hash of format {item: leader}, maintaining the leader
                for all items inserted.
        rank: dict, a hash of format {item: rank}, stores the depth of the
              tree whose root this item is.
    """

    def __init__(self):
        self.leader = {}
        self.rank = {}

    def __len__(self):
        """ Method returns the number of elements stored in the structure. """
        return len(self.leader)

    def make_set(self, item):
        """ Adds a new item to the data structure.

        Args:
            item: hashable data structure.

        Returns:
            The leader of the current set which is itself.
        """
        self.leader[item] = item
        self.rank[item] = 0
        return item

    def find(self, item):
        """ Returns an item of the set which is the leader of the input item.

        This method also applies the optimization known as `path compression`

        Args:
            item: hashable data structure.

        Returns:
            A leader for the given input item.
        """
        if item not in self.leader:
            return self.make_set(item)
        if item != self.leader[item]:
            self.leader[item] = self.find(self.leader[item])
        return self.leader[item]


    def union(self, item1, item2):
        """ Merges two sets toghether ie. both sets will have the same leader.

        Each set is represented by one of it's containing element.
        As an optimization, this method will reuse the `union by rank` method:
        update the set containing the least elements of the two. To do this
        we maintian a rank for each node which is the depth of the tree whose
        head this item is.

        Args:
            item1: hashable data structure.
            item2: hashable data structure.

        Returns:
            The leader of the joined set.
        """
        root1 = self.find(item1)
        root2 = self.find(item2)

        if root1 == root2:
            return root1

        if self.rank[root1] > self.rank[root2]:
            self.leader[root2] = root1
            return root1

        if self.rank[root1] < self.rank[root2]:
            self.leader[root1] = root2
            return root2

        self.rank[root1] += 1
        self.leader[root2] = root1
        return root1
