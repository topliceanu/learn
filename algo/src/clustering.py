# -*- coding: utf8 -*-

import random

from src.union_find import UnionFind
from src.closest_pair import closest_pair


def single_link(points, k, distance):
    """ Clusters a group of elements into subgroups using an optimization
    approach, ie. define a objective function and optimize.

    This greedy method of clustering is called `single-link clustering`, and is
    similar to Kruskel's MST algorithm, with the exception that the iteration
    stops when the number of clusters needed is reached.

    Args:
        points: list of coordinates for points, format (x:int, y:int, name:str)
        k: int, number of clusters to create.
        distance: function, determins the distance between two points.

    Returns:
        A dicts with format {cluster_leader: [list of points in cluster]}.
    """
    cloned_points = points[:]
    union_find = UnionFind()
    for point in points:
        union_find.make_set(point)

    def modified_distance(p1, p2):
        """ Hack which modifies the distance between two points to be +inf
        when these two points are in the same cluster.
        """
        if union_find.find(p1) == union_find.find(p2):
            dist = float('inf')
        else:
            dist = distance(p1, p2)
        return dist

    numClusters = len(points)

    while numClusters > k:
        (p, q) = closest_pair(points, distance=modified_distance)
        if p == q:
            continue

        union_find.union(p, q)
        numClusters -= 1

    out = {}
    for point in cloned_points:
        leader = union_find.find(point)
        if leader not in out:
            out[leader] = []
        out[leader].append(point)
    return out

def cluster_graph(g, k):
    """ Clusters the input graph using the greedy single link method.

    Args:
        g: object, instance of src.graph.Graph
        k: int, number of clusters to create

    Returns:
        tuple, format (clusters, distances)
            clusters: dict, format {cluster_lead_vertex: [list_of_vertexes_in_cluster]}
            distance: dict, format {(cluster1, cluster2): distance_between_cluster1_and_cluster2}
    """
    union_find = UnionFind()
    vertices = g.get_vertices()
    for vertex in vertices:
        union_find.make_set(vertex)

    edges = sorted(g.get_edges(), key=lambda e: e[2], reverse=True) # sort by length
    numClusters = len(vertices)

    # Cluster the nodes in the union_find data structure.
    while numClusters > k:
        while True:
            edge = edges.pop()
            (head, tail, cost) = edge
            if union_find.find(head) != union_find.find(tail):
                break

        union_find.union(head, tail)
        numClusters -= 1

    # Format the clusters for output.
    clusters = {}
    for vertex in vertices:
        leader = union_find.find(vertex)
        if leader not in clusters:
            clusters[leader] = []
        clusters[leader].append(vertex)


    # Computes spacing between clusters, ie. the minimum distance between two
    # nodes in different clusters.
    distances = {}
    for i in clusters.keys():
        for j in clusters.keys():
            if i != j:
                distances[tuple(sorted([i, j]))] = float('inf')

    edges = sorted(g.get_edges(), key=lambda e: e[2], reverse=True)
    for edge in edges:
        (tail, head, distance) = edge
        lead_tail = union_find.find(tail)
        lead_head = union_find.find(head)
        if lead_tail != lead_head and \
           distances[tuple(sorted([lead_tail, lead_head]))] > distance:
            distances[tuple(sorted([lead_tail, lead_head]))] = distance

    return (clusters, distances)

def cluster_k_means(points, k, distance, num_iterations=10):
    """ Clusters a group of points into k groups given a distance function
    between two points.

    Algorithm:
    1. initialization: pick k points at random and set them as initial means
       of the clusters.
    2. for each point compute the distance to the current means and assign
       it to the cluster who's mean is closest.
    3. for each clusters, compute the mean of all points in the cluster
    4. repeat 2 and 3 until convergence, ie. until global error falls under
       a specified threshold.

    Args:
        points: list of tuples, format (x, y) where x and y are the coordinates.
        k: int, number of clusters to generate.
        distance: function, computes distance between two points.
        num_iterations: int, the number of iterations before stopping.

    Returns:
        A dicts with format {cluster_leader: [list of points in cluster]}.
    """

    # Initialization.
    means = random.sample(points, k)
    clusters = dict((mean, [mean]) for mean in means)

    for __ in range(num_iterations):
        new_means = []
        for mean, cluster_points in clusters.iteritems():
            new_mean_x = (sum(x for (x, __, __) in cluster_points))/len(cluster_points)
            new_mean_y = (sum(y for (__, y, __) in cluster_points))/len(cluster_points)
            new_means.append((new_mean_x, new_mean_y))

        clusters = dict((mean, []) for mean in new_means)
        means = new_means

        for point in points:
            min_dist = float('inf')
            new_mean = None
            for mean in means:
                dist = distance(point, mean)
                if min_dist > dist:
                    min_dist = dist
                    new_mean = mean
            clusters[new_mean].append(point)

    return clusters
