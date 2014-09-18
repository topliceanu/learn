# -*- coding: utf8 -*-

from src.union_find import UnionFind
from src.closest_pair import closest_pair


def cluster(points, k, distance):
    """ Clusters a group of elements into subgroups using an optimization
    approach, ie. define a objective function and optimize.

    The method of clustering is called `single-link clustering`, same as
    Kruskel's MST algorithm, with the exception that the iteration stops
    when the number of clusters needed is reached.

    Args:
        points: list of coordinates for points.
        k: int, number of clusters to create.
        distance: function, determins the distance between two points.

    Returns:
        A dicts with format {point, cluster_name}.
    """

    union_find = UnionFind()
    for point in points:
        union_find.make_set(point)

    numClusters = len(points)

    while numClusters > k:
        (p, q) = closest_pair(points)
        union_find.union(p, q)
        points.remove(q)
        numClusters -= 1

    return union_find.leader
