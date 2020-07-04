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
    """ Manacher's algorithm. O(n) time and O(n) space.
    @see https://cp-algorithms.com/string/manacher.html
    """
    n = len(s)
    if n <= 1:
        return s
    l, r = 0, -1
    p = [0] * n
    max_i = 0
    if n % 2 == 1:
        for i in range(n):
            k = 1
            if i < r:
                k = min(p[l+r-i], r-i+1)
            while 0 <= i-k and i+k < n and s[i-k] == s[i+k]:
                k += 1
            p[i] = k-1
            if i + p[i] > r:
                l = i - p[i]
                r = i + p[i]
            if p[i] > p[max_i]:
                max_i = i
        return s[max_i - p[max_i] : max_i + p[max_i] + 1]
    else:
        for i in range(n):
            k = 0
            if i < r:
                k = min(p[l+r-i+1], r-i+1)
            while 0 <= i-k-1 and i+k < n and s[i-k-1] == s[i+k]:
                k += 1
            p[i] = k-1
            if i + p[i] > r:
                l = i - p[i] - 1
                r = i + p[i]
            if p[i] > p[max_i]:
                max_i = i
        return s[max_i - p[max_i] - 1 : max_i + p[max_i] + 1]

def expand(s, c, r=0):
    """ Expands the palindrome in s centered in c starting with starting radius of r.
    Returns the radius of the largest palindrome in s centered in c.
    """
    while c-r >= 0 and c+r < len(s) and s[c+r] == s[c-r]:
        r += 1
    return r - 1

class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return longest_palindrome4(s)
