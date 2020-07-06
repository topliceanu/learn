# -*- coding: utf-8 -*-

"""
Source: https://leetcode.com/problems/zigzag-conversion/
"""

def row_gen(numRows):
    if numRows <= 1:
        yield 1
    r = 0
    increase = True
    while True:
        if increase:
            r += 1
        else:
            r -= 1
        if r == numRows:
            increase = False
        if r == 1:
            increase = True
        yield r

def convert(s, numRows):
    """ Time complexity: O(len(s)), Space complexity: O(len(s)) """
    if numRows <= 1:
        return s
    n = len(s)
    if numRows >= n:
        return s
    data = [[] for _ in range(numRows)]
    rg = row_gen(numRows)
    for i in range(n):
        r = next(rg)
        data[r-1].append(s[i])
    return "".join(map(lambda chars: "".join(chars), data))

def convert2(s, numRows):
    """ Time complexity: O(len(s)), Space complexity: O(2)

    String: P A Y P A L I S H I  R  I  N  G
    index:  0 1 2 3 4 5 6 7 8 9 10 11 12 13
    row:    1 2 3 4 3 2 1 2 3 4  3  2  1  2
    period: 2 * (numRows - 1)

    """
    if numRows <= 1:
        return s
    n = len(s)
    if numRows >= n:
        return s
    out = []
    period = 2 * (numRows - 1)
    for row in range(numRows):
        j = 0
        while j < n:
            if row == 0:
                out.append(s[j])
            elif row == numRows - 1:
                if j + row < n:
                    out.append(s[j+row])
            else:
                l, r = j-row, j+row
                if l >= 0:
                    out.append(s[l])
                if r < n:
                    out.append(s[r])
            j += period
    return "".join(out)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        convert(s, numRows)
