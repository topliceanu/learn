# -*- coding: utf-8 -*-

import math


def convex_hull_graham(points):
    """ Given a set of points this function finds their convex hull wrapper
    using a Graham scan.

    Developed by Roland Graham in 1972

    Complexity: O(nlogn), n - number of points.

    See: Cormen, Introduction to Algorithms

    Args:
        points: list of pairs, format [(x, y)]

    Returns:
        list of pairs, of points composing the hull. Format [(x, y)]
    """
    n = len(points)
    stack = []
    sorted_points_y = sorted(points, key=lambda p: p[1])

    start_point = sorted_points_y[0]
    stack.append(start_point)

    def angle(p0, p1, p2):
        """ Compute the angle given by three points, the tip of the angle and
        other two points.

        Args:
            p0: pair on floats, format (x, y)
            p1: pair of floats, format (x, y)
            p2: pair of floats, format (x, y)

        Returns:
            number, between [0, 2*pi] the angle in radians between the segments
                (p0, p1) and (p0, p2) counted relevant to p1.
        """
        p01 = math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
        p02 = math.sqrt((p0[0] - p2[0])**2 + (p0[1] - p2[1])**2)
        p12 = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        rad = math.acos((p01**2 + p02**2 - p12**2)/(2 * p01 * p02))
        return rad

    sorted_points_angle = sorted(sorted_points_y[1:], cmp=lambda p, q: angle(start_point, p, q))
    stack.concat(sorted_points_angle[0:1])

    for i in range(3, n - 3):
        while angle(stack[-1], stack[-2], sorted_points_angle[i]) <= 1:
            stack.pop()
        stack.append(sorted_points_angle[i])

    return stack

def convex_hull_jarvis(points):
    """ Computes the convex hull of a given set of points using the
    "gift wrapping" method or the "Jarvis march".

    Complexity: O(nh), n - numer of points;
                       h - number of edges in the hull.

    See: Cormen, Introduction to Algorithms

    Args:
        points: list of pairs, format [(x, y)]

    Returns:
        list of pairs, of points composing the hull. Format [(x, y)]
    """
