#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if a <= 0 or b <=0 or c <=0:
        raise TriangleError('At least one side is smaller or equal than 0')

    s = sorted([a,b,c])
    if s[2] >= s[0] + s[1]:
        raise TriangleError('The sides cannot compose a triangle')

    if a == b and b == c:
        return 'equilateral'
    elif a == b or a == c or b == c:
        return 'isosceles'
    else:
        return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
