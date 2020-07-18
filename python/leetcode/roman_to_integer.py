# -*- coding: utf-8 -*-

# Source https://leetcode.com/problems/roman-to-integer/

values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

pred = {
    'I': None,
    'V': 'I',
    'X': 'I',
    'L': 'X',
    'C': 'X',
    'D': 'C',
    'M': 'C',
}

def roman_to_integer(roman):
    if len(roman) == 0:
        return 0
    total = 0
    for i in range(len(roman)):
        cur_l = roman[i]
        cur_v = values[cur_l]
        if i+1 < len(roman):
            next_l = roman[i+1]
            next_v = values[next_l]
            if next_v <= cur_v:
                total += cur_v
            elif pred[next_l] == cur_l:
                total -= cur_v
            else:
                return None # invalid roman numeral
        else:
            total += cur_v
    return total

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return roman_to_int(s)
