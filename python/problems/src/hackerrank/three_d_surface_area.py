#!/bin/python

# Problem: 3D surface area
# Source: https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true
def three_d_surface_area(A: list[list[int]]) -> int :
    h, w = len(A), len(A[0])
    area:int = 0
    # bottom and top
    for i in range(0, h):
        for j in range(0, w):
            if A[i][j] != 0:
                area += 1 + 1
    # front and back.
    for i in range (0, h):
        prev = 0
        for j in range(0, w):
            area += abs(prev-A[i][j])
            prev = A[i][j]
        area += prev
    # left and right.
    for j in range(0, w):
        prev = 0
        for i in range(0, h):
            area += abs(prev-A[i][j])
            prev = A[i][j]
        area += prev
    return area

