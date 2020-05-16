# -*- coding: utf8 -*-

def is_unique(sentence):
    """ 1.1 Is Unique: Implement an algorithm to determine if a string has
    all unique characters. What if you cannot use additional data structures?
    Complexity: O(n) time, O(n) space
    """
    h = set([])
    for c in sentence:
        if c in h:
            return False
        h.add(c)
    return True

def is_unique_no_ds(sentence):
    """ Complexity: O(n) time, O(1) space """
    x = 0
    for c in sentence:
        if x & (1 << ord(c)) != 0:
            return False
        x += 1 << ord(c)
    return True

def check_permutation(str1, str2):
    """ 1.2 Check Permutation: Given two strings, write a method to decide if
    one is a permutation of the other.
    Complexity: O(n) time, O(n) space
    """
    h = {}
    for c in str1:
        if c not in h:
            h[c] = 0
        h[c] += 1
    for c in str2:
        if c not in h:
            return False
        h[c] -= 1
    for (_, count) in h.items():
        if count != 0:
            return False
    return True

def check_permutation_sort(str1, str2):
    """Complexity: O(nlogn) time, O(1) space"""
    str1 = sorted(str1)
    str2 = sorted(str2)
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

def urlify(sentence):
    """ 1.3 URLify: Write a method to replace all spaces in a string with '%20'.
    You may assume that the string has sufficient space at the end to hold the
    additional characters, and that you are given the "true" length of the string.
    EXAMPLE
    Input: "Mr John Smith"
    Output: "Mr%20John%20Smith"

    Complexity: O(n) time, O(1) space
    """
    sentence = list(sentence)
    length = len(sentence)

    count_spaces = 0
    for c in sentence:
        if c == ' ':
            count_spaces += 1

    sentence.extend([' '] * count_spaces * 2)
    pos = length - 1 + count_spaces * 2
    for i in range(length - 1, -1, -1):
        if sentence[i] != ' ':
            sentence[pos] = sentence[i]
            pos -= 1
        else:
            sentence[pos] = '0'
            sentence[pos-1] = '2'
            sentence[pos-2] = '%'
            pos -= 3
    return "".join(sentence)

def palindrome_permutation(sentence):
    """ 1.4 Palindrome Permutation: Given a string, write a function to check
    if it is a permutation of a palin­drome. A palindrome is a word or
    phrase that is the same forwards and backwards. A permutation is a
    rearrangement of letters. The palindrome does not need to be limited to
    just dictionary words.

    EXAMPLE
    Input: Tact Coa
    Output: True (permutations: "taco cat", "atco eta", etc.)

    Complexity: O(n) in time, O(n) in space
    """
    sentence = sentence.lower().replace(" ", "")
    char_counts = {}
    for c in sentence:
        if c not in char_counts:
            char_counts[c] = 0
        char_counts[c] += 1
    has_odd_count = False
    for (c, cnt) in char_counts.items():
        if cnt % 2 != 0:
            if has_odd_count:
                return False
            else:
                has_odd_count = True
    return True

def palindrome_permutation_no_ds(sentence):
    """ Complexity: O(nlogn) in time, O(1) in space """
    sentence = sorted(list(sentence.lower().replace(" ", "")))
    has_odd_count = False
    char_count = 1
    i = 1
    while i < len(sentence):
        if sentence[i] == sentence[i-1]:
            char_count += 1
        else:
            if char_count % 2 != 0:
                if has_odd_count:
                    return False
                else:
                    has_odd_count = True
            char_count = 1
        i += 1
    if char_count % 2 != 0 and has_odd_count == True:
        return False
    return True

def one_away(str1, str2):
    """ 1.5 One Away: There are three types of edits that can be performed on strings:
    insert a character, remove a character, or replace a character.
    Given two strings, write a function to check if they are
    one edit (or zero edits) away.
    EXAMPLE
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false
    pale, ple -> true

    Complexity: O(n) time, O(1) space
    """
    if len(str1) == len(str2):
        # substitution
        already_one_substitution = False
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if not already_one_substitution:
                    already_one_substitution = True
                else:
                    return False
        return True
    elif len(str1) == len(str2) - 1:
        # addition
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                j += 1
            if j > i + 1:
                return False
        return True
    elif len(str1) == len(str2) + 1:
        # deletion
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                i += 1
            if i > j + 1:
                return False
        return True
    else:
        return False

def compression(sentence):
    """ 1.6 String Compression: Implement a method to perform basic string
    compression using the counts of repeated characters.
    For example, the string aabcccccaaa would become a2blc5a3.
    If the "compressed" string would not become smaller than the original string,
    your method should return the original string.
    You can assume the string has only uppercase and lowercase letters (a - z).
    """
    if (len(sentence) in [0, 1, 2]):
        return sentence
    sentence = list(sentence)
    output = []
    i = 1
    j = 1 # counts the length of continuous character so far
    while i < len(sentence):
        if sentence[i] == sentence[i-1]:
            j += 1
        else:
            output.extend([sentence[i-1], str(j)])
            j = 1
        i += 1
    output.extend([sentence[i-1], str(j)])
    if len(output) >= len(sentence):
        return ''.join(sentence)
    return ''.join(output)

def rotate_matrix(mat):
    """ 1.7 Rotate Matrix: Given an image represented by an NxN matrix,
    where each pixel in the image is 4 bytes, write a method to rotate the
    image by 90 degrees. Can you do this in place?
    """
    n = len(mat)
    for i in range(n/2):
        for j in range(i, n-1-i):
            #print
            #print (i,j), '<-', (n-1-j,i)
            #print (n-1-j,i), '<-', (n-1-i,n-1-j)
            #print (n-1-i,n-1-j), '<-', (j,n-1-i)
            #print (j,n-1-i), '<-', (i, j)
            #print
            tmp = mat[i][j]
            mat[i][j] = mat[n-1-j][i]
            mat[n-1-j][i] = mat[n-1-i][n-1-j]
            mat[n-1-i][n-1-j] = mat[j][n-1-i]
            mat[j][n-1-i] = tmp
    return mat

def zero_matrix(mat):
    """ 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN
    matrix is 0, its entire row and column are set to 0.
    """
    n = len(mat)
    m = len(mat[0])
    rows = set([])
    columns = set([])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                rows.add(i)
                columns.add(j)
    for i in range(n):
        for j in range(m):
            if i in rows or j in columns:
                mat[i][j] = 0
    return mat

def is_string_rotation(s1, s2):
    """ 1.9 String Rotation: Assume you have a method isSubstringwhich checks
    if one word is a substring of another. Given two strings, sl and s2, write
    code to check if s2 is a rotation of s1 using only one call to isSubstring
    (e.g., "waterbottle" is a rotation of"erbottlewat").
    """
    return s1 in s2 + s2
