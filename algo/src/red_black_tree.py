# -*- conding:utf-8 -*-

from src.ballanced_binary_search_tree import BST, PARENT, KEY, LEFT, RIGHT, SIZE


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
        """ Removes a node with a given key. """
        # TODO implement this deletion.
        return BST.delete(self, key)


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







    #def insert(self, key):
    #    """ Insert a key in the RB tree preserving the invariants.

    #    Args:
    #        key: int, the identifier of the node to insert.

    #    Returns:
    #        List representing the newly inserted node.
    #    """
    #    inserted_node = BST.insert(self, key)

    #    # If the inserted node is root, we're done.
    #    if inserted_node is self.root:
    #        inserted_node[COLOR] = BLACK
    #        return inserted_node

    #    # By default the inserted node is red.
    #    inserted_node[COLOR] = RED

    #    # If the parent of the inserted node is black, we're done.
    #    parent = inserted_node[PARENT]
    #    if parent[COLOR] == BLACK:
    #        return inserted_node

    #    # If the parent if RED we'be broken the third invariant.
    #    self.fix_double_red(inserted_node)
    #    return inserted_node

    #def fix_double_red(self, node):
    #    """ This method fixes the case when node and it's parent are both red.

    #    When parent node is red, the grand-parent node is necessarely black.
    #    Then it depends on the color of the uncle, ie the sibling of the
    #    parent of the inserted node.

    #    There are two cases:
    #    1. uncle is also red.
    #    2. uncle is black.

    #    Args:
    #        node: list, representing the node which is violating the `double
    #              consecutive reds` invariant in an existing RB tree.
    #    """
    #    parent = node[PARENT]
    #    grand_parent = self.get_grand_parent(node)
    #    uncle = self.get_sibling(parent)

    #    if parent[COLOR] == uncle[COLOR] == RED:
    #        self.recolor(parent) # from RED to BLACK.
    #        self.recolor(uncle) # from RED to BLACK
    #        self.recolor(grand_parent) # grand_parent is BLACK because of invariant 3, recolor it to RED.

    #        # Grand_parent being RED may violate invariant 2
    #        if grand_parent == self.root:
    #            self.recolor(grand_parent) # Turn from RED to BLACK.
    #            return

    #        grand_uncle = self.get_sibling(grand_parent)
    #        if grand_uncle[COLOR] == grand_parent[COLOR] == RED: # violates invariant 3.
    #            self.fix_double_red(grand_parent)
    #            return

    #    if parent[COLOR] == RED and uncle[COLOR] == BLACK:



    #    ## First case.
    #    #if uncle[COLOR] == RED:
    #    #    self.recolor(grand_parent) # Recolor to red.
    #    #    self.recolor(parent) # Recolor to black.
    #    #    self.recolor(uncle) # Recolor to black.

    #    #    if grand_parent == self.root:
    #    #        self.recolor(grand_parent)
    #    #        return

    #    #    grand_grand_parent = grand_parent[PARENT]
    #    #    if grand_grand_parent[COLOR] == RED:
    #    #        self.fix_double_red(grand_parent)
    #    #        return

    #    #if uncle[COLOR] == BLACK:
    #    #    pass





#class SplayTree(BST):
#    """ Adds to the base default Ballanced Search Tree a splaying method which
#    promotes frequently accessed nodes closer to the root.
#    """
#
#class BTree(object): - important for databases
#    pass
#
#class BPlusTree(object): - important for databases.
#    pass
#
#class AVLTree(BST):
#    """ Implements a ballanced binary tree using the AVL method.
#
#    AVL Trees maintain a measurement called the 'ballance factor' for each
#    node in the tree. This is computed as such:
#        height(left_subtree) - height(right_subtree)
#    If this value is not in {-1, 0, 1} then rotations are required.
#    """

