# -*- coding: utf-8 -*-

# Source: https://leetcode.com/problems/generate-parentheses/

def generate_parantheses(n):
    # Space complexity: O(n)
    # Time complexity: O(n!)
    if n == 0:
        return ['']
    out = set([])
    for c in range(n):
        left = generate_parantheses(c)
        right = generate_parantheses(n-1-c)
        for l in left:
            for r in right:
                out.add('('+l+')'+r)
    return list(out)
