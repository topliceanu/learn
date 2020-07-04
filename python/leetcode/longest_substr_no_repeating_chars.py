# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def contract_left(self, s, left, right, counter, max_length):
        # We are contracting as long as there is one char in counter with more than one hit.
        # OR until we don't have a substring anymore.
        if left + 1 > right:
            return max_length
        del_char = s[left]
        if counter[del_char] == 1:
            del counter[del_char]
            return self.contract_left(s, left+1, right, counter, max_length)
        else:
            counter[del_char] -= 1
            if len(counter) > max_length:
                max_length = len(counter)
            return self.expand_right(s, left+1, right+1, counter, max_length)

    def expand_right(self, s, left, right, counter, max_length):
        # We are expending when there is no char in counter with more than one occurance.
        # Or until we reached the end of the string.
        if right == len(s):
            return self.contract_left(s, left, right, counter, max_length)
        new_char = s[right]
        if new_char in counter:
            counter[new_char] += 1
            return self.contract_left(s, left, right, counter, max_length)
        else:
            counter[new_char] = 1
            if len(counter) > max_length:
                max_length = len(counter)
            return self.expand_right(s, left, right+1, counter, max_length)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        return self.expand_right(list(s), 0, 0, {}, 0)
