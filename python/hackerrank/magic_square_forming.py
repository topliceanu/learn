#!/bin/python

# Source: https://www.hackerrank.com/challenges/magic-square-forming/problem (you need to be logged in!)

import math
import os
import random
import re
import sys

def is_magic_square(arr):
    return \
        arr[0] + arr[1] + arr[2] == \
        arr[3] + arr[4] + arr[5] == \
        arr[6] + arr[7] + arr[8] == \
        arr[0] + arr[3] + arr[6] == \
        arr[1] + arr[4] + arr[7] == \
        arr[2] + arr[5] + arr[8] == \
        arr[0] + arr[4] + arr[8] == \
        arr[2] + arr[4] + arr[6]

def generate_magic_squares_rec(so_far, solutions):
    if len(so_far) == 9:
        if is_magic_square(so_far):
            solutions.append(so_far[:])
        return
    for i in range(1, 10):
        if i in so_far:
            continue
        advanced = so_far[:]
        advanced.append(i)
        generate_magic_squares_rec(advanced, solutions)

def generate_magic_squares():
    solutions = []
    generate_magic_squares_rec([], solutions)
    return solutions

def mat_diff(s1, s2):
    diff = 0
    for i in range(9):
        diff += abs(s1[i] - s2[i])
    return diff

def to_arr(mat):
    return mat[0] + mat[1] + mat[2]

def to_mat(arr):
    if arr == None or len(arr) > 9:
        return []
    return [ arr[0:3], arr[3:6], arr[6:] ]

all_magic_squares = generate_magic_squares()

def closest_magic_square(mat):
    global all_magic_squares
    s = to_arr(mat)
    closest_square = None
    smallest_diff = float('inf')
    for magic_square in all_magic_squares:
        current_diff = mat_diff(s, magic_square)
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            closest_square = magic_square
        if smallest_diff == 0:
            break
    return smallest_diff, to_mat(closest_square)

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    diff, mat = closest_magic_square(s)
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in xrange(3):
        s.append(map(int, raw_input().rstrip().split()))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
