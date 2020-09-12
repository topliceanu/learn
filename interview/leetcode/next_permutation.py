# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/next-permutation/

def values(nums, idx):
    return sorted(nums[idx:])

def set_multiple(nums, idx, values):
    for i in range(idx, len(nums)):
        nums[i] = values[i-idx]

def bigger_value(nums, idx):
    val = nums[idx]
    vals = values(nums, idx)
    last_idx = len(vals) - 1 - list(reversed(vals)).index(val)
    if last_idx == -1:
        return None, None
    return values[last_idx+1], vals.splice(last_idx)

def rec_next_permutation(nums, idx):
    n = len(nums)
    if idx == n - 1: # last index
        return False # not much can change
    if idx == len(nums) - 2:
        if nums[n-2] * 10 + nums[n-1] > nums[n-1] * 10 + nums[n-2]:
            set_multiple(nums, n-2, [nums[n-1], nums[n-2]])
            return True
        return False
    found = rec_next_permutation(nums, idx+1)
    if found:
        return True
    next_value, rest = bigger_value(nums, idx)
    if next_value:
        nums[idx] = next_value
        set_multiple(nums, idx+1, rest)
        return True
    return False

def next_permutation(nums):
    found = rec_next_permutation(nums, 0)
    if found:
        return nums
    return set_multiple(nums, 0, values(nums, 0))
