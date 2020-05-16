# -*- coding: utf-8 -*-

END = 'END'


class TrieNode(object):
    """ This implementation uses recursion to simplify the algorithms
    as opposed to the Trie class below.
    """
    def __init__(self, value=None):
        self.value = value
        self.children = {}

    def insert(self, key, value):
        """ Insert the value under the given key. """
        if key == '':
            self.value = value
            return

        (head, tail) = self.split(key)
        if head not in self.children:
            self.children[head] = TrieNode()
        self.children[head].insert(tail, value)

    def lookup(self, key):
        """ Search for the value corresponding to key. """
        if key == '':
            return self.value
        (head, tail) = self.split(key)
        if head not in self.children:
            return None
        return self.children[head].lookup(tail)

    def lookup_prefix(self, prefix):
        """ Returns a list of all [(key, value)] pairs where key starts with
        prefix.

        Two phases:
        1. traverse the prefix
        2. once the prefix has been traversed, return the entire subtree.

        Args:
            prefix: str, the prefix to find all corresponding keys.
        Returns:
            list, of pairs, format [(key, value)]
        """
        if prefix == '':
            return self.traverse()

        (head, tail) = self.split(prefix)
        if head not in self.children:
            return []

        pairs = self.children[head].lookup_prefix(tail)
        pairs = map(lambda p: (head+p[0], p[1]), pairs)

        return pairs

    def delete(self, key):
        """ Removes a value associated with the given key from the trie.

        It will remove the node as well if it is not a prefix to other nodes.

        Args:
            key: string, the key corresponding to the value to remove.
        """
        if key == '': # Reached the node corresponding to the initial key.
            if len(self.children) != 0:
                self.value = None
                return False # Node is a prefix to other nodes, so no removal.
            else:
                return True # Node is not a prefix to other nodes, ok for removal.

        (head, tail) = self.split(key)
        if head not in self.children: # The key is not present in the trie.
            return False

        # Remove child node if instructed.
        should_remove = self.children[head].delete(tail)
        if should_remove == True:
            del self.children[head]

        # Instruct callee to remove node only if it has no other children.
        return len(self.children) == 0

    def traverse(self):
        """ Returns a list of key, value pairs for all it's children
        including it's own value, sorted lexicographically by key.

        Returns:
            list, of pairs, formt [(key, value)]
        """
        out = []
        if self.value != None:
            out.append(('', self.value))

        children = sorted(self.children.iteritems(), key=lambda p: p[0])
        for (letter, child) in children:
            pairs = child.traverse()
            pairs = map(lambda p: (letter+p[0], p[1]), pairs)
            out.extend(pairs)
        return out

    def split(self, key):
        """ Splits a string into the first character and the second one. """
        if len(key) == 0:
            raise Exception('Cannot extract head and tail from empty string')
        return (key[0], key[1:])


class Trie(object):
    """ Also known as prefix trees.

    In this tree structure, each node (besides the leaves) hold a letter from
    the inserted words. Some words have common prefixes so they share the nodes
    of their prefix. The leaves themselves may contain values associated with
    the key traversed so far.

    See: https://reterwebber.wordpress.com/2014/01/22/data-structure-in-python-trie/

    Attrs:
        root: object
    """
    def __init__(self):
        self.root = {}

    def insert(self, key, value=None):
        """ Insert the key string in the data structure.

        Args:
            key: str, the string to index in the trie.
            value: any, optional value to associate with the key.
        """
        current = self.root
        for letter in key:
            current.setdefault(letter, {})
            current = current[letter]
        current = current.setdefault(END, value)

    def lookup(self, key):
        """ Returns the value associated with the given key.

        Args:
            key: str

        Returns:
            any, value associated with key.
            None, if the full key is not present.
        """
        current = self.root
        for letter in key:
            if letter not in current:
                return None
            current = current[letter]
        if END not in current:
            return None
        return current[END]

    def contains(self, key):
        """ Checks if the string key is stored in the data structure.

        Params:
            key: str, the name of the key to look for.

        Returns:
            bool: True if the key is found. Note! it will return False if only
                the prefix is present.
        """
        node = self.root
        for letter in key:
            if letter not in node:
                return False
            node = node[letter]
        if END not in node:
            return False
        return True

    def with_prefix(self, prefix):
        """ Returns all keys with the given prefix.

        Params:
            prefix: str,

        Returns:
            list: of pairs, format [(key, value)] where key matches the prefix.
        """
        current = self.root
        for letter in prefix:
            if letter not in current:
                return []
            else:
                current = current[letter]
        pairs = self.traverse(current)
        return [(prefix+key, value) for (key, value) in pairs]

    def traverse(self, root=None):
        """ Returns a list of all the contained keys sorted in lexicographic
        order.

        Params:
            root: object, pointer to the root of the object to start extracting
                the sorted words.

        Return:
            list, of tuples, with forma format [(key, value)]
        """
        if root == None:
            root = self.root

        out = []
        for letter, rest in root.iteritems():
            if letter == END: # Reached a value.
                out.append(('', rest))
            else:
                pairs = self.traverse(rest)
                for (word, value) in pairs:
                    out.append((letter+word, value))
        return out

# TODO Implement a space efficient Trie in O(n).
