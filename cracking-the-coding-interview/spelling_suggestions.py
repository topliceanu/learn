# -*- conding: utf-8 -*-

class TrieNode(object):
    def __init__(self):
        self.key = None
        self.children = {}

    def insert(self, key):
        if key == '':
            return
        head, tail = key[0], key[1:]
        if head not in self.children:
            tn = TrieNode()
            tn.key = head
            self.children[head] = tn
            tn.insert(tail)
        else:
            self.children[head].insert(tail)

    def traverse(self, prefix):
        """ Returns [] if the prefix is not in the tree.
        Computes a list of works from the dictionary with the same prefix.
        """
        node = self.advance(prefix)
        if node == None:
            return []
        words = node.collect()
        return [ prefix + word for word in words ]

    def advance(self, prefix):
        if len(prefix) == 1:
            return self
        head, tail = prefix[0], prefix[1:]
        if head in self.children:
            return self.advance(tail)
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

def spelling_suggestions(dictionary, prefix):
    dict_trie = TrieNode()
    for word in dictionary:
        dict_trie.insert(word)
    return dict_trie.traverse(prefix)
