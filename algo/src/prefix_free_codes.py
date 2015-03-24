# -*- coding: utf-8 -*-

from src.graph import Graph


PARENT = 0
LEFT = 1
RIGHT = 2
SYMBOL = 3

class HuffmanCode(object):
    """ Huffman variable length prefix-free codes.

    Attrs:
        symbols: dict, format {key: frequency}
        tree: object, root of the transformation tree.
    """
    def __init__(self, symbols):
        self.symbols = symbols
        self.tree = self.build_tree()

    def build_tree(self):
        """ Builds the tree which corresponds to hoffman encoding algorithm.

        Returns:
            object, reference to the root of the encoding/decoding tree.
        """
        sorted_symbols = sorted(self.symbols.items(), key=lambda t: t[1], reverse=True)
        root = [None, None, None, None]

        while len(sorted_symbols) > 0:
            new_node = [None, None, None, sorted_symbols.pop()[0]]
            if (root[LEFT] != None and root[RIGHT] != None):
                new_root = [None, new_node, root, None]
                root[PARENT] = new_root
                new_node[PARENT] = new_root
                root = new_root
            elif root[LEFT] == None:
                root[LEFT] = new_node
                new_node[PARENT] = root
            elif root[RIGHT] == None:
                root[RIGHT] = new_node
                new_node[PARENT] = root
        return root

    def encode(self, text):
        """ Encodes given text using the hoffman tree.

        Args:
            text: str, string to be encoded.

        Returns:
            str, a string of 1s and 0s.
        """
        out = ''
        for char in list(text):
            root = self.tree
            encoded = ''
            while root[LEFT] != None and root[RIGHT] != None:
                if root[LEFT][SYMBOL] == char:
                    root = root[LEFT]
                    encoded += '0'
                else:
                    root = root[RIGHT]
                    encoded += '1'
            out += encoded
        return out

    def decode(self, encoded):
        """ Decodes encoded text into original version.

        Args:
            encoded: str, a string of 1s and 0s.

        Returns:
            str, string extracted from the encoded version.
        """
        out = ''
        pointer = self.tree
        for bit in list(encoded):
            if bit == '0':
                out += pointer[LEFT][SYMBOL]
                pointer = self.tree # Reset to the root.
            elif bit == '1':
                pointer = pointer[RIGHT]

                is_leaf = pointer[LEFT] == None and pointer[RIGHT] == None
                if is_leaf:
                    out += pointer[SYMBOL]
        return out

    # STATIc METHODS.

    @staticmethod
    def encode_text(text):
        """ Given a text, it return the optimal encoding in terms of total
        number of bits.

        Args:
            text: str, the input text.

        Returns:
            str, the encoded text represented a string of 1s and 0s.
        """
        symbol_table = HuffmanCode.extract_frequencies(text)
        hc = HuffmanCode(symbol_table)
        return hc.encode(text)

    @staticmethod
    def decode_text(symbol_table, encoded_text):
        """ Decodes a stream of 1s and 0s, encoded using a symbol table.

        Args:
            symbol_table: dict, format {symbol: probability}
            encoded_text: str, a string of 1s and 0s representing the encoded text.

        Returns:
            str, the decoded string.
        """
        hc = HuffmanCode(symbol_table)
        return hc.decode(encoded_text)

    @staticmethod
    def extract_frequencies(text):
        """ Given a text it computes the probabilities of each character.

        Args:
            text: str

        Returns:
            dict, with format {symbol: symbol_frequency}
        """
        hist = {}
        for char in list(text):
            if char in hist:
                hist[char] = 0
            hist[char] += 1

        text_len = len(text)
        for char, count in hist.iteritems():
            hist[char] = hist[char] / text_len

        return hist
