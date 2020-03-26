# -*- conding:utf-8 -*-

from src.binary_search_tree import BST, PARENT, KEY, LEFT, RIGHT, SIZE


# Coloring of nodes.
RED = 0x100
BLACK = 0x101

# Index of the color value in a node list.
COLOR = 5


class RedBlackTree(BST):
    """ Implements ballanced red-black trees as a subclass of
    binary search tree.

    The RB invariants are:
    1. each node is either Red or Black.
    2. root is always black
    3. never have two red nodes in a row.
    4. every path you can take from a root to a NULL (eg. when searching for a
    node which does not exist) path passes through the same number of black
    nodes.

    See: http://en.wikipedia.org/wiki/Red-black_tree for implementation.
    See: https://en.wikipedia.org/wiki/Left-leaning_red-black_tree for a
    simpler implementation.

    Each node is represented as a list with the format:
        [parent, key, left, right, size, color]
    """

    def __init__(self):
        BST.__init__(self)

    def insert(self, key):
        """ Insert key in the tree maintaining the Red-Black invariants.

        Insert using the default BST insert method and color the node in RED.

        Args:
            key: int, the value of the inserted node.
        """
        inserted_node = BST.insert(self, key)
        inserted_node.append(RED)

        self.insert_case_1(inserted_node)

    def insert_case_1(self, node):
        """ Insert case 1: inserted node is root, in which case we need to
        recolor it to BLACK to maintain invariant 2.
        """
        if node[PARENT] == None:
            node[COLOR] = BLACK
        else:
            self.insert_case_2(node)

    def insert_case_2(self, node):
        """ Insert case 2: the inserted node's parent is black, in which case
        none of the Red-Black invariants are broken.
        """
        if node[PARENT][COLOR] == BLACK:
            return
        else:
            self.insert_case_3(node)

    def insert_case_3(self, node):
        """ Insert case 3: When both parent and uncle are RED then we color
        both of them in black and the grand_parent in RED.

                GP(b)                  GP(r)
               /  \                   /  \
            U(r)   P(r)      =>    U(b)   P(b)
                     \                      \
                     N(r)                   N(r)

        Now grand_parent may violate invariants 2 or 3.
        If grand_parent is a root node (ie. invariant 2) then we are in case 1.
        If grand_parent's parent is also RED (ie. invariant 3) then we are in case 4.
        """
        uncle = self.get_sibling(node[PARENT])
        if uncle != None and uncle[COLOR] == RED:
            node[PARENT][COLOR] = BLACK
            uncle[COLOR] = BLACK
            grand_parent = self.get_grand_parent(node)
            grand_parent[COLOR] = RED
            self.insert_case_1(node)
        else:
            self.insert_case_4(node)

    def insert_case_4(self, node):
        """ Insert case 4: Described by the following two cases below.
        The solution is to employ rotations so we can employ case 5.

                GP(b)                      GP(b)
               /  \                        /  \
            P(r)   U(b)  =(left_rot)=>  N(r)   U(b)
               \                        /
               N(r)                  P(r)

               OR

                GP(b)                       GP(b)
               /   \                       /   \
             U(b)  P(r)  =(right_rot)=>  U(b)  N(r)
                    /                             \
                  N(r)                            P(r)
        """
        grand_parent = self.get_grand_parent(node)

        if node == node[PARENT][RIGHT] and node[PARENT] == grand_parent[LEFT]:
            self.rotate(node[PARENT], RIGHT)
            node = node[LEFT]

        elif node == node[PARENT][LEFT] and node[PARENT] == grand_parent[RIGHT]:
            self.rotate(node[PARENT], LEFT)
            node = node[RIGHT]

        self.insert_case_5(node)

    def insert_case_5(self, node):
        """ Insert case 5: Described by the following diagram:

                GP(b)                        P(b)
               /  \                         /  \
            P(r)   U(b)  =(left_rot)=>   N(r)   GP(r)
            /                                      \
         N(r)                                      U(b)


                GP(b)                          P(b)
               /  \                           /   \
            U(b)   P(r)   =(right_rot)=>   GP(r)  N(r)
                     \                      /
                     N(r)                 U(b)
        """
        grand_parent = self.get_grand_parent(node)
        node[PARENT][COLOR] = BLACK
        grand_parent[COLOR] = RED
        if node == node[PARENT][LEFT]:
            self.rotate(grand_parent, LEFT)
        else:
            self.rotate(grand_parent, RIGHT)


    def delete(self, key):
        """ Removes a node with a given key and maintains Red-Black invariants.
        TODO make this work!
        """
        if node[LEFT] == None and node[RIGHT] != None:
            child = node[RIGHT]
        if node[LEFT] != None and node[RIGHT] == None:
            child = node[LEFT]

        self.replace_node(node, child)
        if node[COLOR] == BLACK:
            if child[COLOR] == RED:
                child[COLOR] = BLACK
            else:
                self.delete_case_1(child)

    def delete_case_1(self, node):
        if node[PARENT] != None:
            self.delete_case_2(node)

    def delete_case_2(self, node):
        sibling = self.get_sibling(node)
        if sibling[COLOR] == RED:
            node[PARENT][COLOR] = RED
            sibling[COLOR] = BLACK
            if node == node[PARENT][LEFT]:
                self.rotate(RIGHT, node[parent])
            else:
                self.rotate(LEFT, node[parent])
        self.delete_case_3(node)

    def delete_case_3(self, node):
        sibling = self.get_sibling(node)
        if node[PARENT][COLOR] == BLACK and \
           sibling[COLOR] == BLACK and \
           sibling[LEFT][COLOR] == BLACK and \
           sibling[RIGHT][COLOR] == BLACK:
                sibling[COLOR] = RED
                self.delete_case_1(node[parent])
        else:
            self.delete_case_4(node)

    def delete_case_4(self, node):
        sibling = self.get_sibling(node)
        if node[PARENT][COLOR] == RED and \
           sibling[COLOR] == BLACK and \
           sibling[LEFT][COLOR] == BLACK and \
           sibling[RIGHT][COLOR] == BLACK:
                sibling[COLOR] = RED
                node[PARENT][COLOR] = BLACK
        else:
            self.delete_case_5(n)

    def delete_case_5(self, node):
        sibling = self.get_sibling(node)
        if sibling[COLOR] == BLACK:
            if node == node[PARENT][LEFT] and \
               sibling[RIGHT][COLOR] == BLACK and \
               sibling[LEFT][COLOR] == RED:
                    sibling[COLOR] = RED
                    sibling[LEFT][COLOR] = BLACK
            elif node == node[PARENT][RIGHT] and \
                 sibling[LEFT][COLOR] == BLACK and \
                 sibling[RIGHT][COLOR] == RED:
                    sibling[COLOR] = RED
                    sibling[RIGHT][COLOR] = BLACK
                    self.rotate(RIGHT, sibling)
        self.delete_case_6(node)

    def delete_case_6(self, node):
        sibling = self.get_sibling(node)
        sibling[COLOR] = node[PARENT][COLOR]
        node[PARENT][COLOR] = BLACK

        if (node == node[PARENT][LEFT]):
            sibling[RIGHT][COLOR] = BLACK
            self.rotate(RIGHT, node[PARENT])
        else:
            sibling[LEFT][COLOR] = BLACK
            self.rotate(LEFT, node[PARENT])

    # UTILITIES

    def get_grand_parent(self, node):
        """ Returns the parent of the parent of node. """
        if node[PARENT] is None:
            return None
        return node[PARENT][PARENT]

    def get_sibling(self, node):
        """ Returns the sibling of the node. """
        if node[PARENT] is None:
            return None

        if node[PARENT][LEFT] == node:
            return node[PARENT][RIGHT]
        else:
            return node[PARENT][LEFT]

    def replace_nodes(self, node1, node2):
        """ Replaces node1 and node2 by rewiring the pointers (parent, left
        and right) of the two nodes.

        Args:
            node1: list, structure contains a node with format:
                [PARENT, KEY, LEFT, RIGHT, SIZE]
            node2: list, structure contains a node with format:
                [PARENT, KEY, LEFT, RIGHT, SIZE]
        """
        node1[PARENT][DIRECTION1], node2[PARENT][DIRECTION2] = \
            node2[PARENT][DIRECTION2], node1[PARENT][DIRECTION1]
        node1[PARENT], node2[PARENT] = node2[PARENT], node1[PARENT]

        for direction in [LEFT, RIGHT]:
            node1[direction][PARENT], node2[direction][PARENT] = \
                node2[direction][PARENT], node1[direction][PARENT]
            node1[direction], node2[direction] = node2[direction], node1[direction]
