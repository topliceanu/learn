# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/integer-to-roman/

encoding = [
    (('I', 'V', 'X'), 1),
    (('X', 'L', 'C'), 10),
    (('C', 'D', 'M'), 100),
    (('M', 'N', 'Z'), 1000),
]

def encode(digit, symbols):
    if digit == 0:
        return ''
    (low, mid, high) = symbols
    if digit <= 3:
        return ''.join([low for i in range(digit)])
    if digit == 4:
        return low + mid
    if digit >= 5 and digit <= 8:
        return mid + encode(digit-5, symbols)
    if digit == 9:
        return low + high

def integer_to_roman(number):
    if number < 0:
        raise Exception('cannot represent negative numbers')
    if number == 0:
        return ''
    for (symbols, div) in encoding:
        if number < div * 10:
            first, rest = number / div, number % div
            return encode(first, symbols) + integer_to_roman(rest)
    raise Exception("number is too large")

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return integer_to_roman(num)
