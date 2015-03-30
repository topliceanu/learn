# -*- coding: utf-8 -*-

END = 'END'


class Trie(object):
    """ Also known as prefix trees.

    See: https://reterwebber.wordpress.com/2014/01/22/data-structure-in-python-trie/
    for reference implementation.

    Attrs:
        root: object
    """
    def __init__(self):
        self.root = {}

    def insert(self, key):
        """ Insert the key string in the data structure. """
        current = self.root
        for letter in key:
            current.setdefault(letter, {})
            current = current[letter]
        current = current.setdefault(END, END)

    def contains(self, key):
        """ Checks if the key string is in the data structure.

        Params:
            key: str, the name of the key to look for.

        Returns:
            bool: True if the key is found. Note! it will return False if only
                the prefix is present.
        """
        current = self.root
        for letter in key:
            if letter not in current:
                return False
            current = current[letter]

        if END in current:
            return True
        return False

    def with_prefix(self, prefix):
        """ Returns all keys with the given prefix.

        Params:
            prefix: str,

        Returns:
            list: of words which match the prefix.
        """
        current = self.root
        for letter in prefix:
            if letter not in current:
                return []
            else:
                current = current[letter]
        words = self.list_sorted(current)
        return ['{prefix}{word}'.format(prefix=prefix, word=w) for w in words]

    def list_sorted(self, root=None):
        """ Returns a list of all the contained keys sorted in lexicographic
        order.

        Params:
            root: object, pointer to the root of the object to start extracting
                the sorted words.

        Return:
            list:
        """
        if root == None:
            root = self.root
        if root == END:
            return ['']

        out = []
        for letter, rest in root.iteritems():
            words = self.list_sorted(rest)
            for word in words:
                if letter == END:
                    out.append('')
                else:
                    out.append('{letter}{word}'.format(letter=letter, word=word))
        return out


class CompressedTrie(object):
    pass
