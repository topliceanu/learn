#!/bin/python

# Problem: bigger is greater
# Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria: 
# It must be greater than the original word; It must be the smallest word that meets the first condition
# Source: https://www.hackerrank.com/challenges/bigger-is-greater/problem

def bigger_is_greater(w):
    # The following is an implementation of the Narayana Panditha's algorithm.
    # A proof produced by Gemini: https://share.google/aimode/CpED4MeZun7uVQECb
    # Step 1. find the rightmost ascent.
    w = list(w)
    k = len(w)-2
    while k >= 0 and w[k] >= w[k+1]:
        k -= 1
    if k < 0:
        return "no answer"
    # Step 2. Find the rightmost element larger than w[k]
    i = len(w) - 1
    while w[i] <= w[k]: 
        i -= 1
    # Step 3: swap pivot with successor.
    w[i], w[k] = w[k], w[i]
    # Step 4: reverse the tail.
    w[k+1:] = reversed(w[k+1:])
    return "".join(w)
    
    