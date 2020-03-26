# -*- coding: utf-8 -*-

import os


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

#from src.clustering import cluster_graph
#from src.graph import Graph
#
#
#g = Graph.build(directed=False)
#
#with open('{base}/test/Clustering.txt'.format(base=os.getcwd()), 'r') as f:
#    for line in f:
#        [tail, head, value] = map(int, line.split())
#        g.add_edge((tail, head, value))
#
#(clusters, distances) = cluster_graph(g, 4)
#print '>>>>', clusters
#print '>>>>', distances # max distance is 1162

"""
In this question your task is again to run the clustering algorithm from
lecture, but on a MUCH bigger graph. So big, in fact, that the distances
(i.e., edge costs) are only defined implicitly, rather than being provided as
an explicit list.

The data set is here. The format is:
[# of nodes] [# of bits for each node's label]
[first bit of node 1] ... [last bit of node 1]
[first bit of node 2] ... [last bit of node 2]
...

For example, the third line of the file
    "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1"
denotes the 24 bits associated with node #2.

The distance between two nodes u and v in this problem is defined as the
Hamming distance--- the number of differing bits --- between the two nodes'
labels. For example, the Hamming distance between the 24-bit label of node #2
above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3
(since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of k such that there is a
k-clustering with spacing at least 3? That is, how many clusters are needed
to ensure that no pair of nodes with all but 2 bits in common get split into
different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably
can't write it out explicitly, let alone sort the edges by cost. So you will
have to be a little creative to complete this part of the question. For
example, is there some way you can identify the smallest distances without
explicitly looking at every pair of nodes?
"""

## The key idea in this solution: instead of O(n^2) checks between each two nodes,
## we compute all the possible distances of max 2 bits and check each node at a
## time.
#
#from src.union_find import UnionFind
#
#nodes = set()
#uf = UnionFind()
#
##with open('{base}/test/ClusteringBig.10000.txt'.format(base=os.getcwd()), 'r') as f: # solution is 9116
##with open('{base}/test/ClusteringBig.20000.txt'.format(base=os.getcwd()), 'r') as f: # solution is 16508
##with open('{base}/test/ClusteringBig.30000.txt'.format(base=os.getcwd()), 'r') as f: # solution is 22177
#with open('{base}/test/ClusteringBig.txt'.format(base=os.getcwd()), 'r') as f:
#    for line in f:
#        node = int(''.join(line.split()), 2)
#        nodes.add(node)
#        uf.make_set(node)
#
#distances = set() # holds all Humming distances of 1 and 2.
#base = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
#
#for i in range(24):
#    distance = base[:]
#    distance[i] = '1'
#    distances.add(int(''.join(distance),2))
#
#for i in range(24):
#    for j in range(24):
#        if i != j:
#            distance = base[:]
#            distance[i] = '1'
#            distance[j] = '1'
#            distances.add(int(''.join(distance),2))
#distances = list(distances)
#
#for node in nodes:
#    for distance in distances:
#        neighbour = node ^ distance
#        if neighbour in nodes and uf.find(node) != uf.find(neighbour):
#            uf.union(node, neighbour)
#
#print '>>>>', len(set(uf.leader.values())) # 6945
