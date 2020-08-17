# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/median-of-two-sorted-arrays/

def median_sorted_arrays(nums1, l1, r1, nums2, l2, r2):
    s1, s2 = r1 - l1, r2 - l2
    if s1 <= 1 and s2 <= 1:
        if s1 + s2 == 1:
            return nums1[r1] if s1 == 1 else nums2[r2]
        else: # n + m == 2
            return (nums1[r1] + nums2[r2])/2
    if s1 == 0:
        return nums2[l2 + (s2+1)/2]
    if s2 == 0:
        return nums1[l1 + (s1+1)/2]

    m1, m2 = (s1+1)/2, (s2+1)/2
    target = m1 + m2

    lv1, rv1, lv2, rv2 = nums1[l1], nums1[r1], nums2[l2], nums2[r2]

    if lv1 < rv1 < lv2 < rv2:
        if s1 < target:
            return median_sorted_arrays(nums1, 0, 0, nums2, l2, l2 + (target - s1))
    elif lv1 < lv2 < rv1 < rv2:
        pass
    elif lv1 < lv2 < rv2 < rv1:
        pass
    elif lv2 < lv1 < rv2 < rv1:
        pass
    elif lv2 < rv2 < lv1 < rv1:
        pass


#def median_sorted_arrays(nums1, l1, r1, nums2, l2, r2):
#    n, m = r1 - l1 + 1, r2 - l2 + 1
#    if n <= 1 and m <= 1:
#        if n + m == 1:
#            return nums1[r1] if n == 1 else nums2[r2]
#        else: # n + m == 2
#            return (nums1[r1] + nums2[r2])/2
#
#    a, b, c, d = nums1[l1], nums1[r1], nums2[l2], nums2[r2]
#    m1, m2 = (n+1)/2, (m+1)/2
#    #e, f = nums1[m1], nums2[m2]
#
#    if c < d < a < b:
#        return median_sorted_arrays(nums2, m2, r2, nums1, l1, m1)
#    elif c < a < d < b:
#        pass
#    elif c < a < b < d:
#        pass
#    elif a < c < d < b:
#        pass
#    elif a < c < b < d:
#        pass
#    elif a < b < c < d:
#        return median_sorted_arrays(nums1, m1, r1, nums2, l2, m2)
#
