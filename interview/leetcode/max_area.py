# -*- coding: utf-8 -*-

#Source: https://leetcode.com/problems/container-with-most-water/solution/

def max_area(heights):
    n = len(heights)
    if n < 2:
        return 0
    i, j = 0, n-1
    max_ar = 0
    while i < j:
        cur_ar = (j - i) * min(heights[i], heights[j])
        max_ar = max(cur_ar, max_ar)
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return max_ar

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return max_are(height)

