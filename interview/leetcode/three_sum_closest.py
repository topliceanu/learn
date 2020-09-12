# -*- coding: utf-8 -*-

# Source https://leetcode.com/problems/3sum-closest/

def three_sum_closest(nums, target):
    n = len(nums)
    if n < 3:
        raise Exception('expected at least a three element array')

    nums.sort()
    closest = nums[0] + nums[1] + nums[2]

    for i in range(n-2):
        a = nums[i]

        j = i+1
        k = n-1
        while j < k:
            b = nums[j]
            c = nums[k]
            s = a + b + c
            if target == s:
                return s
            elif target > s:
                if target > 0:
                    j += 1
                else:
                    k -= 1
            else: # target < s:
                if target > 0:
                    k -= 1
                else:
                    j += 1
            if abs(target - closest) > abs(target - s):
                closest = s

    return closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return three_sum_closest(nums, target)
