# -*- coding: utf-8 -*-

"""
In this assignment you will implement one or more algorithms for the all-pairs
shortest-path problem. Here are data files describing three graphs:
[./Graph1.txt], [./Graph2.txt], [./Graph3.txt]

The first line indicates the number of vertices and edges, respectively.
Each subsequent line describes an edge (the first two numbers are its tail
and head, respectively) and its length (the third number). NOTE: some of the
edge lengths are negative. NOTE: These graphs may or may not have
negative-cost cycles.

Your task is to compute the "shortest shortest path". Precisely, you must
first identify which, if any, of the three graphs have no negative cycles.
For each such graph, you should compute all-pairs shortest paths and remember
the smallest one (i.e., compute minu,v∈Vd(u,v), where d(u,v) denotes the
shortest-path distance from u to v).

If each of the three graphs has a negative-cost cycle, then enter "NULL" in
the box below. If exactly one graph has no negative-cost cycles, then enter
the length of its shortest shortest path in the box below. If two or more of
the graphs have no negative-cost cycles, then enter the smallest of the lengths
of their shortest shortest paths in the box below.

OPTIONAL: You can use whatever algorithm you like to solve this question. If
you have extra time, try comparing the performance of different all-pairs
shortest-path algorithms!

OPTIONAL: If you want a bigger data set to play with, try computing the
shortest shortest path for this graph [./GraphLarge.txt]
"""

import os

from src.all_pairs_shortest_paths import dijkstra, roy_floyd_warshall, johnson
from src.graph import Graph


def read_graph(file_name):
    """ Reads graph adjacency matrix from the given file. """
    g = Graph.build(directed=True)
    with open('{base}/test/{f}'.format(base=os.getcwd(), f=file_name), 'r') as f:
        [num_vertices, num_edges] = map(int, f.readline().split())
        for __ in range(num_edges):
            [tail, head, value] = map(int, f.readline().split())
            g.add_edge((tail, head, value))
    return g


g1 = read_graph('Graph1.txt')
#g2 = read_graph('Graph2.txt')
#g3 = read_graph('Graph3.txt')


#o11 = johnson(g1)
o12 = roy_floyd_warshall(g1)


