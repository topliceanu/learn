# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, left, right, target):
    if left > right:
        return -1
    mid = int((left + right) / 2)
    if nums[mid] == target:
        return mid

    # left --- target --- mid --- right
    if nums[mid] <= nums[right]:
        if target < nums[mid] or target > nums[right]:
            return search(nums, left, mid-1, target)
        else:
            return search(nums, mid+1, right, target)

    # left --- mid --- target --- right
    if nums[left] <= nums[mid]:
        if target > nums[mid] or target < nums[left]:
            return search(nums, mid+1, right, target)
        else:
            return search(nums, left, mid-1, target)

def search_rotated_array(nums, target):
    if len(nums) == 0:
        return -1
    return search(nums, 0, len(nums)-1, target)
