# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/3sum/

def three_sum(nums, total):
    nums.sort()
    out = set([])
    n = len(nums)

    for i in range(n-2):
        j = i + 1
        k = n - 1
        a = nums[i]
        while j < k:
            b = nums[j]
            c = nums[k]
            if a + b + c == total:
                out.add((a, b, c))
                j += 1
                k -= 1
            elif a + b + c < total:
                j += 1
            else:
                k -= 1
    return list(out)

def three_sum_old(nums, total):
    nums.sort()
    out = []
    n = len(nums)

    i = 0
    while i < n-2:
        if nums[i] == nums[i+1]:
            i += 1
            continue
        a = nums[i]

        j = i + 1
        k = n - 1

        while j < k:
            if nums[j] == nums[j+1]:
                j += 1
                continue
            if nums[k] == nums[k-1]:
                k -= 1
                continue

            b = nums[j]
            c = nums[k]
            print i, j, k
            if a + b + c == total:
                out.append((a, b, c))
                j += 1
                k -= 1
            elif a + b + c < total:
                j += 1
            else:
                k -= 1

        i += 1

    return out

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return three_sum(nums, 0)
