# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/3sum/

def equal(ls, i, j):
    return ls[i][0] == ls[j][0] and ls[i][1] == ls[j][1] and ls[i][2] == ls[j][2]

def three_sum(nums, total):
    nums.sort()
    out = []
    n = len(nums)

    for i in range(n - 2):
        a = nums[i]
        j = i + 1
        k = n - 1
        while j < k:
            b = nums[j]
            c = nums[k]
            if a + b + c == total:
                out.append((a, b, c))
                j += 1
            elif a + b + c < total:
                j += 1
            else:
                k -= 1

    filtered = []
    for i in range(len(out)):
        found = False
        for j in range(i+1, len(out)):
            if equal(out, i, j):
                found = True
        if not found:
            filtered.append(out[i])

    return filtered

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return three_sum(nums, 0)
