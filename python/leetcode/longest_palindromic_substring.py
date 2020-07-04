# Source: https://leetcode.com/problems/longest-palindromic-substring/

def maximum(l, r):
    li, lj, lok = l
    ri, rj, rok = r
    if lok and rok:
        if lj - li > rj -ri:
            return li, lj, True
        else:
            return ri, rj, True
    if lok:
        return li, lj, True
    if rok:
        return ri, rj, True
    return li, lj, False

def grow(s, i, j):
    print(">>>", i, j)
    if i < 0 or j >= len(s) or s[i] != s[j]:
        return i, j, False
    left = grow(s, i-1, j)
    right = grow(s, i, j+1)
    both  = grow(s, i-1, j+1)
    print("-", left, right, both)
    mi, mj, mok = maximum(both, maximum(left, right))
    print("=", mi, mj, mok)
    if mok:
        return mi, mj, True
    return i, j, True

def longest_palindrome1(s):
    """ first attempt. this is not correct! """
    min_j = 0
    max_k = 0
    for i in range(len(s)):
        (j, k, ok) = grow(s, i, i)
        if not ok:
            continue
        if k - j > max_k - min_j:
            min_j = j
            max_k = k
    return s[min_j:max_k+1]

def longest_palindrome2(s):
    """ correct version """
    if len(s) <= 1:
        return s
    # always match first character
    min_i = 0
    max_j = 0
    cache = [0] * len(s)
    for i in range(len(s) - 1, -1, -1):
        new_cache = [0] * len(s)
        new_cache[i] = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j] and (i+1 >= j-1 or cache[j-1] == 1):
                new_cache[j] = 1
                if j - i > max_j - min_i:
                    max_j = j
                    min_i = i
        cache = new_cache
    return s[min_i:max_j+1]

def longest_palindrome3(s):
    """ less memory """
    if len(s) <= 1:
        return s
    # always match first character
    min_i = 0
    max_j = 0
    cache = [0] * len(s)
    prev = 0
    for i in range(len(s) - 1, -1, -1):
        prev = cache[i]
        cache[i] = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j] and (i+1 >= j-1 or prev == 1):
                prev = cache[j]
                cache[j] = 1
                if j - i > max_j - min_i:
                    max_j = j
                    min_i = i
            else:
                prev = cache[j]
                cache[j] = 0
    return s[min_i:max_j+1]

def longest_palindrome4(s):
    """ Manacher's algorithm: https://www.hackerrank.com/topics/manachers-algorithm
        O(n) time and O(1) space.
    """
    se = "#"+"#".join(list(s))+"#"


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return longest_palindrome(s)
