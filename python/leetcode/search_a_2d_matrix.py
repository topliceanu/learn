# -*- coding: utf-8 -*-

"""
Source: https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
"""
def search(mat, target, l1, l2, c1, c2):
    if l1 > l2 or c1 > c2:
        return False
    if l2 - l1 == 0 and c2 - c1 == 0:
        return mat[l1][c1] == target
    lmid = (l1+l2)/2
    cmid = (c1+c2)/2
    if target == mat[lmid][cmid]:
        return True
    if target < mat[lmid][cmid]:
        return \
            search(mat, target, l1, lmid, c1, cmid) or \
            search(mat, target, l1, lmid-1, cmid+1, c2) or \
            search(mat, target, lmid+1, l2, c1, cmid-1)
    if target > mat[lmid][cmid]:
        return \
            search(mat, target, l1, lmid, cmid+1, c2) or \
            search(mat, target, lmid+1, l2, cmid+1, c2) or \
            search(mat, target, lmid+1, l2, c1, cmid)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        return search(matrix, target, 0, m-1, 0, n-1)
