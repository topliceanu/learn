import sys
sys.path.insert(0, '/vagrant/algo')

from src.heap import Heap
from src.flood_fill import scanline_fill


# 1. Implement a spell-checker.


# 2. sort a k-sorted array: sort an array which is already partially sorted,
# ie. each element is at most k positions away from it's sorted position.

def k_sorted_array(arr, k):
    """ Method sorts a k-sorted array.

    A k-sorted array is an array where each element is at most k positions away
    of it's final sorted position.

    This solution piggybacks on the heapsort algorithm

    Complexity: O(nlogk) in time

    Args:
        arr: list, of values to sort.
        k: int, the max distance any element can be from it's final sorted position.

    Returns:
        list, sorted array
    """
    n = len(arr)
    if n < k:
        k = n

    heap = Heap.heapify(arr[:k])

    out = []
    for i in range(k, n):
        min_value = heap.extract_min_and_insert(arr[i])
        out.append(min_value)

    for i in range(k):
        min_value = heap.extract_min()
        out.append(min_value)

    return out

def connected_zeros_in_array(arr):
    """ Given a matrix of 1s and 0s, find if all the 0s are connected.

    See: http://www.glassdoor.com/Interview/Given-a-matrix-of-1s-and-0s-find-if-all-the-0s-are-connected-ie-can-you-flood-fill-the-area-QTN_967859.htm

    Returns:
        bool, True if all zeroes are connected
    """
    n = len(arr)

    # find a starting point
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                break
            else:
                continue
            break
    start_point = (i, j)

    # Flood-fill all reachable zeroes with values of one.
    scanline_fill(arr, start_point, 0, 1)

    # For each line, the sum of values should be n.
    for i in range(n):
        if sum(arr[i]) != n:
            return False
    return True

# Facebook Interviews

class Node(object):
    """ A node in a tree. """

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

def binary_tree_level_order_traversal(tree):
    """ Binary Tree level order traversal, a.k.a. breadth-first search. """
    def traverse(node, level, out):
        if node == None:
            return

        if level not in out:
            out[level] = set([])
        out[level].add(node.key)

        for child in node.children:
            traverse(child, level+1, out)

    output = {}
    traverse(tree, 1, output)
    return output

# Problem source: https://www.facebook.com/Engineering/videos/vl.922576297773331/10153034510412200/?type=1
def get_nearby_words(data):
    """ When typing on a touch screen, occasionally the wrong key is registered.
    Write a function, which, give a string, returns all nearby words.

    A nearby word is composed by taking the input word and replacing one letter
    with one of it's nearby letters.

    MOCK!

    Args:
        data: str, invalid input string.
        words: list, of str, available valid words.

    Returns:
        list, of str, top valid words available closest to the input string.
    """
    def get_nearby_chars(char):
        pass

    def is_word(data):
        pass

    def permutations(data): # gi | i
        if len(data) == 0:
            return ['']

        head = data[0] # g | i
        tail = data[1:] # [i] | []
        perms = permutations(tail) # [u,i,o] | ['']
        nearby_chars = get_nearby_chars(head) # [h,g,j] | [u,i,o]

        out = []
        for nearby_char in nearby_chars: # [h,g,j]
            for perm in perms: # [u, i, o]
                out.append(nearby_char+perm)
        return out # [hu, hi, ho, gu, gi, go, ju, ji, jo]


    perms = permutations(data)
    out = []
    for p in perms:
        if is_word(p):
            out.append(p)
    return out

def match(text, pattern):
    """ Given a string and a pattern, where:
    '.' - matches any single character.
    '*' - matches zero or more of the preceding element.
    Find the first substring matching this pattern.

    Tests:
    >>> match('alex', 'le')
    le
    >>> match('alexandra', 'al.*a') # an
    alexa
    >>> match('alexandru', 'al.*a.dru*')
    alexandru
    >>> match('alex', '.')
    'a'
    >>> match('alex', '.*')
    'alex'
    >>> match('aleex', 'e*')
    'ee'
    >>> match('alex', 'alex*')
    'alex'
    >>> match('alex', '*alex')
    Error
    >>> match('alex', 'alex.')
    ''
    >>> match('alex', '**')
    Error
    """

    END = '$'

    class Automaton(object):
        """ Builds a new automaton for matching strings. """
        def __init__(self, pattern):
            self.start = {}

            state = self.start
            symbols = self.extract_symbols(pattern)
            for (index, symbol) in enumerate(symbols):
                if len(symbol) == 1:
                    state[symbol] = {}
                    state = state[symbol]
                else:
                    [x, y, z] = symbol
                    state[x] = state
                    if z != None:
                        state[z] = {}
                        state = state[z]
            state[END] = None


        def extract_symbols(self, pattern):
            """ Returns: list, of string, format ([A-z.]|([A-z.]\*[A-z]) """
            out = []
            i = 0
            while i < len(pattern):
                c = pattern[i]
                n = pattern[i+1] if i+1 < len(pattern) else None
                nn = pattern[i+2] if i+2 < len(pattern) else None
                if c == '*' and i == 0:
                    raise Exception('Pattern does not support * in first position')
                if c == '*' and n == '*':
                    raise Exception('Pattern does not support successive *')
                if n == '*':
                    out.append([c, n, nn])
                    i += 3
                else:
                    out.append(c)
                    i += 1
            return out

        def check(self, text, index):
            """ Checks if the string matches the automaton. """
            text += END
            state = self.start
            while index < len(text):
                char = text[index]
                index += 1
                if char in state:
                    state = state[char]
                elif '.' in state:
                    state = state['.']
                else:
                    return False
            return True

    a = Automaton(pattern)
    for i in range(len(text)):
        is_match = a.check(text, i)
        if is_match == True:
            return True
    return False

def same_fringe(tree1, tree2):
    """ Detect is the given two trees have the same fringe. A fringe is a list
    of leaves sorted from left to right.
    """
    def is_leaf(node):
        return len(node['children']) == 0

    def in_order_traversal(node):
        if node == None:
            return []

        if is_leaf(node):
            return [node['key']]

        leaves = []
        for child in node['children']:
            leaves.extend(in_order_traversal(child))

        return leaves

    leaves1 = in_order_traversal(tree1)
    leaves2 = in_order_traversal(tree2)
    return leaves1 == leaves2

# Facebook Phone Interview.

def is_anagram(s1, s2):
    """ Figures out if the two strings are anagrams.

    Complexity: O(n)

    Args:
        s1: str
        s2: str

    Returns:
        boolean, True if s1 is an anagram of s2.
    """
    letters = {}
    for c in s1:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    for c in s2:
         if c in letters:
             letters[c] -= 1
             if letters[c] == 0:
                 del letters[c]
         else:
             return False

    return len(letters) == 0

def find_anagrams_slow(needle, haystack):
    """ Finds anagrams of needle in the haystack string.

    Complexity: O(n^2) , where n - length of haystack.

    Args:
        needle: str
        haystack: str

    Returns:
        boolean, True if haystack contains anagrams of needle.
    """
    n = len(needle)
    m = len(haystack)
    for i in range(m-n+1): # O(n)
        sub_haystack = haystack[i:n]  # O(1)
        if is_anagram(sub_haystack, needle): # O(n)
            return True
    return False

def delta(s1, s2):
    """ Find the difference in characters between s1 and s2.

    Complexity: O(n), n - length of s1 or s2 (they have the same length).

    Returns:
        dict, format {extra:[], missing:[]}
            extra: list, letters in s2 but not in s1
            missing: list, letters in s1 but not in s2
    """
    letters = {}
    for c in s1:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1

    extra = [] # letters which are in s2 but not in s1
    for c in s2:
        if c not in letters:
            extra.append(c)
        else:
            letters[c] -=1

    missing = [] # letters which are in s1 but not in s2
    for (letter, count) in letters.iteritems():
        if count > 0:
            missing.append(letter)

    return {'extra': extra, 'missing': missing}

def find_anagrams_fast(needle, haystack):
    """ Finds anagrams of needle in the haystack string.

    Complexity: O(n) , where n - length of haystack.

    Args:
        needle: str
        haystack: str

    Returns:
        boolean, True if haystack contains anagrams of needle.
    """
    n = len(needle)
    m = len(haystack)

    #import pdb; pdb.set_trace()
    sub_haystack = haystack[:n]
    __ = delta(needle, sub_haystack)
    extra = __['extra']
    missing = __['missing']
    if len(extra) == 0:
        return True

    for i in range(n, m):
        j = i - n
        if haystack[j] in extra:
            extra.remove(haystack[j])
        if haystack[i] in missing:
            missing.remove(haystack[i])
        if haystack[j] in needle:
            missing.append(haystack[j])
        if haystack[i] not in needle:
            extra.append(haystack[i])
        if len(extra) == 0:
            return True

    return False
