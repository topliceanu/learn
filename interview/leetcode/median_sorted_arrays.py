# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/median-of-two-sorted-arrays/
# O(logn) solution: https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46


def median_sorted_arrays(nums1, nums2):
    n1, n2 = len(nums1), len(nums2)
    med = (n1 + n2 + 1) / 2
    i, j, k = 0, 0, 0
    while i < n1 and j < n2:
        if nums1[i] <= nums2[j]:
            i += 1
            k += 1
            if k == med:
                return nums1[i]
        else:
            j += 1
            k += 1
            if k == med:
                return nums2[j]
