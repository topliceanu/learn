# -*- coding: utf-8 -*-

def closest_pair(points):
    """ Computes the closest pair from a given set of points in a plain.

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

    Params
    points - list of tuples [(x, y)]
    """

    p = extract(points, 0)
    q = extract(points, 1)
