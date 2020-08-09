# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

mapping = {
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

def letter_combinations(digits):
    """ @param {str} digits """

    def rec_comb(digits):
        if len(digits) == 0:
            return []
        first, rest = digits[0], digits[1:]
        if first not in mapping:
            raise Exception('{} not in {}'.format(first, mapping))
        mappings = mapping[first]
        if len(mappings) == 0:
            return rec_comb(rest)
        rest_comb = rec_comb(rest)
        if len(rest_comb) == 0:
            rest_comb = [ "" ]
        output = []
        for ch in mappings:
            for comb in rest_comb:
                output.append(ch+comb)
        return output

    return rec_comb(list(digits))

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return letter_combinations(digits)
