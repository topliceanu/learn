# -*- coding: utf-8 -*-

import math

from src.binary_search_tree import BST, KEY, LEFT, RIGHT, PARENT, SIZE


class AVLTree(BST):
    """ An implementation of a self-ballancing binary search tree

    The AVLTree invariant is that each node has to have a ballance factor in
    {-1, 0, 1}, whereby the ballance factor is calculated as the height of the
    left subtree minus the height of the right subtree.

    They are more rigidly ballaced than RedBlack trees which makes them better
    at lookups.

    Inventors: Georgy Adelson-Velsky and E.M. Landis in 1962.
    """

    def get_ballance_factor(self, node):
        """ Computes the ballance factor of a given node.

        Args:
            node: list, the node to compute ballance for, format:
                [parent, key, left, right, size]

        Returns:
            int, size(left) - size(right)
        """
        if node == None:
            return 0

        left = self.depth(node[LEFT])
        right = self.depth(node[RIGHT])

        return left - right

    def reballance(self, node):
        """ Re-ballance the tree to maintain the AVL invariant.

        To keep the tree ballanced, after normal insertion we rotate the
        inserted node up the tree until the all nodes maintain the ballance
        factor invariant. Following four cases of unballance can occur:


               GP(2)           GP(2)         N(0)
               /               /            /   \
             P(-1)     =>    N(1)     =>  P(0) GP(0)
               \             /
               N(0)        P(0)

            [case 1:       [case 2:
            left-right]    left-left]



               GP(-2)         GP(-2)            N(0)
                  \             \              /   \
                  P(1)   =>    N(-1)     =>  GP(0) P(0)
                  /               \
                N(0)              P(0)

             [case 3:          [case 4:
             right-left]       right-right]


        Complexity: O(log n)
        """
        while True:
            parent = node[PARENT]
            if parent == None:
                return
            else:
                grand_parent = parent[PARENT]
            if grand_parent == None:
                return

            parent_ballance_factor = self.get_ballance_factor(parent)
            grand_parent_ballance_factor = self.get_ballance_factor(grand_parent)

            if grand_parent_ballance_factor == 2:
                if parent_ballance_factor == -1:
                    # Case 1: left-right
                    self.rotate(parent, RIGHT)
                    self.rotate(grand_parent, LEFT)

                elif parent_ballance_factor == 0:
                    # When parent is ballanced but grand parent is not. Act as case 2.
                    self.rotate(grand_parent, LEFT)

                elif parent_ballance_factor == 1:
                    # Case 2: left-left
                    self.rotate(grand_parent, LEFT)

            elif grand_parent_ballance_factor == -2:
                if parent_ballance_factor == 1:
                    # Case 3: right-left
                    self.rotate(parent, LEFT)
                    self.rotate(grand_parent, RIGHT)

                elif parent_ballance_factor == 0:
                    # When parent is ballanced but grand parent is not. Act as case 4.
                    self.rotate(grand_parent, RIGHT)

                elif parent_ballance_factor == -1:
                    # Case 4: right-right
                    self.rotate(grand_parent, RIGHT)
            else:
                # Traverse up the ancestors.
                node = node[PARENT]

    def insert(self, key):
        """ Insert a node into the data structure.

        Args:
            key: int, the value to insert in the tree.

        Returns:
            A list representing the newly inserted node. Format:

        """
        node = BST.insert(self, key)
        self.reballance(node)
        return node

    def delete_and_reballance(self, key):
        # Node is a recently removed leaf.
        node = BST.delete(self, key)

        if node == None:
            return None

        ancestor = node
        while ancestor != None:
            ancestor = ancestor[PARENT]

            # Ignore ballanced ancestors.
            if -2 < self.get_ballance_factor(ancestor) < 2:
                continue

            if self.depth(ancestor[LEFT]) > self.depth(ancestor[RIGHT]):
                FIRST = LEFT
            else:
                FIRST = RIGHT

            if self.depth(ancestor[FIRST][LEFT]) > self.depth(ancestor[FIRST][RIGHT]):
                SECOND = LEFT
            else:
                SECOND = RIGHT

            #import pdb; pdb.set_trace()
            self.reballance(ancestor[FIRST][SECOND])

        return node
