# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/string-to-integer-atoi/

max_int = pow(2, 31) - 1
min_int = -pow(2, 31)

def atoi(text):
    rest = list(text)
    (_, rest) = consume_multiple(consume_space, rest)
    (sign, rest) = consume_sign(rest)
    if len(sign) == 0:
        sign = ['+']
    (digits, _) = consume_multiple(consume_digit, rest)
    if len(digits) == 0:
        return 0
    num = to_number(sign[0], digits)
    if num > max_int:
        return max_int
    if num < min_int:
        return min_int
    return num

def consume_space(chars):
    if len(chars) > 0 and chars[0] == " ":
        return ([" "], chars[1:])
    return ([], chars)

def consume_sign(chars):
    if len(chars) > 0 and chars[0] in ['-', '+']:
        return ([chars[0]], chars[1:])
    return ([], chars)

def consume_digit(chars):
    if len(chars) > 0 and chars[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return ([int(chars[0])], chars[1:])
    return ([], chars)

def consume_multiple(parser, chars):
    out = []
    rest = chars
    while True:
        if len(rest) == 0:
            break
        (more, rest) = parser(rest)
        if len(more) == 0:
            break
        out.append(more[0])
    return (out, rest)

def to_number(sign, digits):
    out = 0
    for i in range(len(digits)):
        j = len(digits) - 1 - i
        out += digits[j] * pow(10, i)
    if sign == '-':
        return -out
    return out
