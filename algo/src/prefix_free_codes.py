# -*- coding: utf-8 -*-

from heapq import heappop, heappush, heapify

from src.graph import Graph


class Node(object):
    """ Represents a node in the Huffman code tree. """
    def __init__(self, symbol, probability, parent=None, left=None, right=None):
        self.symbol = symbol
        self.probability = probability
        self.parent = parent
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left == None and self.right == None

    def __cmp__(self, other):
        if isinstance(other, Node):
            return cmp(self.symbol, other.symbol)
        return -1

class Huffman(object):
    """ Huffman variable length prefix-free codes.

    See: https://en.wikipedia.org/wiki/Huffman_coding

    Attrs:
        symbols: dict, format {key: frequency}
        leaves: dict, format {key: node} holds tree leafs indexed by symbol.
            Useful when encoding an input string.
        root: object, root of the transformation tree.
            Usefull when decoding an input list of bits.
    """
    def __init__(self, symbols):
        self.symbols = symbols
        self.leaves = {}
        self.root = None
        self.build_tree()

    def make_node(self, symbol, probability, parent=None, left=None, right=None):
        return Node(symbol, probability, parent, left, right)

    def build_tree(self):
        """ Builds the Hoffman encoding tree using a heap. """
        h = []
        for (symbol, probability) in self.symbols.iteritems():
            node = self.make_node(symbol, probability)
            self.leaves[symbol] = node
            h.append((probability, node))
        heapify(h)

        while len(h) >= 2:
            [_, last] = heappop(h)
            [_, second_last] = heappop(h)

            join_probability = last.probability + second_last.probability
            join_symbol = last.symbol + second_last.symbol
            join_node = self.make_node(join_symbol, join_probability, None, last, second_last)

            last.parent = join_node
            second_last.parent = join_node
            heappush(h, (join_probability, join_node))

        self.root = h[0][1]

    def encode(self, text):
        """ Encodes given text using the hoffman tree.

        Args:
            text: str, string to be encoded.

        Returns:
            str, a string of 1s and 0s.
        """
        out = ''
        for symbol in text:
            code = ''
            node = self.leaves[symbol]
            while node != None:
                if node.parent == None:
                    break
                if node.parent.left == node:
                    code = '1' + code
                else:
                    code = '0' + code
                node = node.parent
            out += code
        return out

    def decode(self, encoded):
        """ Decodes encoded text into original version by traversing the
        hoffman tree.

        Args:
            encoded: str, a string of 1s and 0s.

        Returns:
            str, string extracted from the encoded version.
        """
        out = ''
        node = self.root
        for bit in list(encoded):
            if bit == '0':
                node = node.right
            elif bit == '1':
                node = node.left

            if node.is_leaf():
                out += node.symbol
                node = self.root
        return out

    def to_string(self):
        """ String representation of the current huffman encode/decode tree. """
        def traverse(node, count):
            if node == None:
                return

            name = node.symbol if node.symbol != None else count

            if node.left != None:
                left_name = node.left.symbol if node.left.symbol else count + 1
                print '{val}-L->{left}'.format(val=name, left=left_name)

            if node.right != None:
                right_name = node.right.symbol if node.right.symbol else count + 2
                print '{val}-R->{left}'.format(val=name, left=right_name)

            traverse(node.left, count + 1)
            traverse(node.right, count + 2)
        traverse(self.root, 0)

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
        symbol_table = Huffman.extract_frequencies(text)
        hc = Huffman(symbol_table)
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
        hc = Huffman(symbol_table)
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
            if char not in hist:
                hist[char] = 0
            hist[char] += 1

        text_len = len(text)
        for char, count in hist.iteritems():
            hist[char] = float(hist[char]) / float(text_len)

        return hist
