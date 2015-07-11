# -*- coding: utf-8 -*-

from heapq import heappop, heappush, heapify

from src.graph import Graph


PARENT = 0
LEFT = 1
RIGHT = 2
SYMBOL = 3


class HuffmanCode(object):
    """ Huffman variable length prefix-free codes.

    Attrs:
        symbols: dict, format {key: frequency}
        nodes: dict, format {key: node} holds tree nodes indexed by symbol.
        tree: object, root of the transformation tree.
    """
    def __init__(self, symbols):
        self.symbols = symbols
        self.nodes = {}
        self.tree = self.build_tree()

    def build_tree(self):
        """ Builds the Hoffman encoding tree using a heap. """
        h = []
        for (symbol, probability) in self.symbols.iteritems():
            node = [None, None, None, symbol]
            self.nodes[symbol] = node
            h.append((probability, node))
        heapify(h)

        while len(h) >= 2:
            last = heappop(h)
            second_last = heappop(h)
            join_probability = last[0] + second_last[0]
            join_node = [None, last[1], second_last[1], None]
            last[1][PARENT] = join_node
            second_last[1][PARENT] = join_node
            heappush(h, (join_probability, join_node))

        return h[0][1]

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
            node = self.nodes[symbol]
            while node != None:
                parent = node[PARENT]
                if parent == None:
                    break
                if parent[LEFT] == node:
                    code = '1' + code
                else:
                    code = '0' + code
                node = parent
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
        pointer = self.tree
        for bit in list(encoded):
            if bit == '0':
                pointer = pointer[RIGHT]
            elif bit == '1':
                pointer = pointer[LEFT]

            is_leaf = pointer[LEFT] == None and \
                      pointer[RIGHT] == None and \
                      pointer[SYMBOL] != None
            if is_leaf:
                out += pointer[SYMBOL]
                pointer = self.tree
        return out

    def to_string(self):
        """ String representation of the current huffman encode/decode tree. """
        def traverse(node, count):
            if node == None:
                return

            name = node[SYMBOL] if node[SYMBOL] != None else count

            if node[LEFT] != None:
                left_name = node[LEFT][SYMBOL] if node[LEFT][SYMBOL] else count+1
                print '{val}-L->{left}'.format(val=name, left=left_name)

            if node[RIGHT] != None:
                right_name = node[RIGHT][SYMBOL] if node[RIGHT][SYMBOL] else count+2
                print '{val}-R->{left}'.format(val=name, left=right_name)

            traverse(node[LEFT], count+1)
            traverse(node[RIGHT], count+2)
        traverse(self.tree, 0)

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
            if char not in hist:
                hist[char] = 0
            hist[char] += 1

        text_len = len(text)
        for char, count in hist.iteritems():
            hist[char] = float(hist[char]) / float(text_len)

        return hist
