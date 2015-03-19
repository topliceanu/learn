# -*- coding:utf-8 -*-

from src.ballanced_binary_search_tree import BST


class SplayTree(BST):
    """ Just like a simple Binary Search Tree but with the added operation of
    splaying.

    Complexity for most operations: O(log n), Omega(n)

    TODO test and make sure this works!

    See: http://en.wikipedia.org/wiki/Splay_tree
    """

    def splay(self, node):
        """ The splay operation hoists the indicated node to the root.

        There are three cases where rotations are employed to hoist a node
        (let x be the input node, p be x's parent and g be x's grand parent).

        ZIG (p is root, g is None)
                (p)            (x)
               /        =>        \
             (x)                  (p)

        ZIG-ZIG (x is p's LEFT child, p is g's LEFT child and otherwise)
                 (g)           (x)
                /                \
              (p)        =>      (p)
             /                     \
           (x)                     (g)

        ZIG-ZAG (x is p's LEFT child, p is g's RIGHT child and otherwise)
                  (g)
                 /                 (x)
               (p)        =>      /   \
                 \              (p)   (g)
                 (x)

        Args:
            node: list, a representation of a node, format [PARENT, KEY, LEFT, RIGHT, SIZE]

        Returns:
            node: the splayed node with updated references which is no the root.
        """
        while node[PARENT] != None:
            # ZIG.
            if node[PARENT][PARENT] != None:
                if node[PARENT][LEFT] == node:
                    self.rotate(LEFT, node[PARENT])
                else:
                    self.rotate(RIGHT, node[PARENT])
            # ZIG-ZIG.
            elif node[PARENT][LEFT] == node and node[PARENT][PARENT][LEFT] == node[PARENT]:
                self.rotate(LEFT, node[PARENT][PARENT])
                self.rotate(LEFT, node[PARENT])
            # ZIG-ZIG.
            elif node[PARENT][RIGHT] == node and node[PARENT][PARENT][RIGHT] == node[PARENT]:
                self.rotate(RIGHT, node[PARENT][PARENT])
                self.rotate(RIGHT, node[PARENT])
            # ZIG-ZAG.
            elif node[PARENT][LEFT] == node and node[PARENT][PARENT][RIGHT] == node[PARENT]:
                self.rotate(LEFT, node[PARENT])
                self.rotate(RIGHT, node[PARENT])
            # ZIG-ZAG.
            else:
                self.rotate(RIGHT, node[PARENT])
                self.rotate(LEFT, node[PARENT])
        return node

    def insert(self, key):
        """ After regular BST insert, the new node is hoisted to the root. """
        node = BST.insert(self, key)
        return self.splay(node)

    def delete(self, key):
        """ After regular BST delete, the former node's parent is hoisted to
        the root.
        """
        node = BST.delete(self, key)
        return self.splay(node[PARENT])

    def search(self, key):
        """ After a successful search operation the returned node is hoisted
        to the root before being returned.
        """
        node = BST.search(self, key)
        return self.splay(node)

    def join(self, other_tree):
        """ Join other_tree with the current tree. The conditions is that any
        element in other_tree is larger than any element in current tree.

        Args:
            other_tree: object, instance of src.ballanced_search_tree.BST
        """
        current_max = self.get_max()
        if current_max > other_tree.get_min():
            raise Exception('The tree to join must have strictly larger items '
                            'than current trees items')
        root = self.splay(current_max)
        root[LEFT] = other_tree.root


    def split(self, key):
        """ Splits the current tree into two subtrees, the left one containing
        all elements smaller than key, the right one containing all elements
        larger than key.

        Args:
            key: int

        Returns
            list, with format [left_subtree, right_subtree]
        """
        root = self.search(key)
        return [root[LEFT], root[RIGHT]]
