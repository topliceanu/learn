# -*- coding: utf-8 -*-

import math


def closest_pair(points):
    """ Computes the closest pair from a given set of points in 2D.

    Running time is O(nlogn) time.
    Uses divide and conquer with the following steps:
    - sort the points on x and y axes
    - split the plain in two by the x axis
    - compute closest pair for left and rigth subsets
    - join the results by computing for the worst case when the closest
    pair is split between the two subsets.
    - the stopcase is when we have three points, where you can just use the
    brute force to compute closest pair.

    The trick is in the joining of the results and computing split pairs.
    This is done in O(logn) time

    Args:
        points: list of tuples [(x, y)] representing coordonates
            of the points analyzed.

    Returns:
        A tuple of tuples representing the closest pair of points.
    """
    Px = sorted(list(points), key=lambda x: x[0])
    Py = sorted(list(points), key=lambda x: x[1])

    return closest_pair_rec(Px, Py)


def closest_pair_rec(Px, Py):
    """ Recursively compute the closest pair in both px and py sets of points.

    Args:
        px: list of tuples [(x, y)] sorted by x
        py: list of tuples [(x, y)] sorted by y

    Returns:
        A tuple with the closest pair of points format ((x1, y1), (x2, y2)).
    """
    if len(Px) < 4:
        # This is the base case.
        pairs = []
        for i in range(len(Px) -1):
            for j in range(i+1, len(Px)):
                pairs.append((Px[i], Px[j]))
        pair = min(pairs, key=lambda p: distance(p[0], p[1]))
        return pair


    # Split points in two: left and right sorted by coordinate.
    Qx = Px[len(Px)/2:]
    Rx = Px[:len(Px)/2]
    Qy = Py[len(Py)/2:]
    Ry = Py[:len(Py)/2]

    # Apply closest pair on both subsets.
    (p1, q1) = closest_pair_rec(Qx, Qy)
    (p2, q2) = closest_pair_rec(Rx, Ry)

    # Compute closest pair of subsets and split.
    tmp_pair = min([(p1, q1), (p2, q2)], key=lambda p: distance(p[0], p[1]))
    delta = distance(tmp_pair[0], tmp_pair[1])
    split_pair = closest_split_pair(Px, Py, delta)

    if split_pair is None:
        return tmp_pair
    else:
        return split_pair

def closest_split_pair(Px, Py, delta):
    """ Subroutine which checks if there is a pair of point such that one
    point is in Px, the other is in Py and the distance between them is less
    than delta.

    Returns:
        None if no split pair is discovered which w/ dist smaller than delta.
        A tuple of points (tuples) representing point w/ smallest distance.
    """
    big_x = Px[-1] # biggest element in the left of Px.
    Sy = [x for x in Px if x[0] >= big_x[0] - delta or x[0] <= big_x[0] + delta]
    best = delta
    best_pair = None
    for i in range(len(Sy) - 7):
        for j in range(7):
            if distance(Sy[i], Sy[j]) < best:
                best = distance(Sy[i], Sy[j])
                best_pair = (Sy[i], Sy[j])
    return best_pair

def distance(p, q):
    """ Computes the distance between two points p and q."""
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
