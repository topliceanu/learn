# -*- coding: utf-8 -*-

"""
In this programming problem and the next you'll code up the clustering
algorithm from lecture for computing a max-spacing k-clustering. Use the text
file [./Clustering.txt]. This file describes a distance function (equivalently,
a complete graph with edge costs). It has the following format:

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]
[edge 2 node 1] [edge 2 node 2] [edge 2 cost]
...

There is one edge (i,j) for each choice of 1≤i<j≤n, where n is the number of
nodes. For example, the third line of the file is "1 3 5250", indicating that
the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3))
is 5250. You can assume that distances are positive, but you should NOT assume
that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on
this data set, where the target number k of clusters is set to 4. What is the
maximum spacing of a 4-clustering?

ADVICE: If you're not getting the correct answer, try debugging your algorithm
using some small test cases. And then post them to the discussion forum!
"""

import os

from src.clustering import single_link, cluster_k_means
from src.graph import Graph


g = Graph.build(edges=[], directed=False)

with open('{base}/test/Clustering.txt'.format(base=os.getcwd()), 'r') as f:
    for line in f:
        [tail, head, value] = line.split()
        g.add_edge((int(tail), int(head), int(value)))
