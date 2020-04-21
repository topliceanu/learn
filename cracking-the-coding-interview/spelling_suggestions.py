# -*- conding: utf-8 -*-

class TrieNode(object):
    def __init__(self, key=None, isWord=False):
        self.key = key
        self.isWord = isWord
        self.children = {}

    def insert(self, key):
        """ Inserts an new key in the current node's subtree.
        Args:
            key, string
        """
        if key == '':
            self.isWord = True
            return
        head, tail = key[0], key[1:]
        if head not in self.children:
            self.children[head] = TrieNode(head)
        self.children[head].insert(tail)

    def advance(self, path):
        """ Returns the node that results from traversing path from current node.
        Args:
            path, string
        Returns:
            object, instance of spelling_suggestion.TrieNode
        """
        if path == '':
            return self
        head, tail = path[0], path[1:]
        if head in self.children:
            return self.children[head].advance(tail)
        return None

    def collect(self):
        if len(self.children) == 0 and self.key != None: # I'm a leaf
            return [ self.key ]
        if self.key == None: # I'm a root
            prefix = ''
        else:
            prefix = self.key
        words = []
        for _, child in self.children.items():
            postfixes = child.collect()
            with_key = [ prefix + p for p in postfixes ]
            words += with_key
        return words

    def traverse(self, prefix):
        """ Returns [] if the prefix is not in the tree.
        Computes a list of words from the dictionary with the same prefix.
        """
        node = self.advance(prefix)
        if node == None:
            return []
        words = node.collect()
        return [ prefix + word for word in words ]

def spelling_suggestions(dictionary, prefix):
    dict_trie = TrieNode()
    for word in dictionary:
        dict_trie.insert(word)
    return dict_trie.traverse(prefix)
