# -*- coding:utf-8 -*-

"""
Download the text file here. [./KargerMinCut.txt]

The file contains the adjacency list representation of a simple undirected graph.
There are 200 vertices labeled 1 to 200. The first column in the file represents
the vertex label, and the particular row (other entries except the first column)
tells all the vertices that the vertex is adjacent to. So for example, the 6th
row looks like : "6 155 56 52 120 ......". This just means that the vertex with
label 6 is adjacent to (i.e., shares an edge with) the vertices with labels
155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the
min cut problem and use it on the above graph to compute the min cut (i.e.,
the minimum-possible number of crossing edges). (HINT: Note that you'll have to
figure out an implementation of edge contractions. Initially, you might want to
do this naively, creating a new graph from the old every time there's an edge
contraction. But you should also think about more efficient implementations.)
(WARNING: As per the video lectures, please make sure to run the algorithm many
times with different random seeds, and remember the smallest cut that you ever
find.) Write your numeric answer in the space provided. So e.g., if your answer
is 5, just type 5 in the space provided.
"""

#import os
#
#from src.graph import Graph
#from src.minimum_cut import minimum_cut
#
#
#g = Graph(directed=False)
#
#with open('{base}/test/KargerMinCut.txt'.format(base=os.getcwd()), 'r') as f:
#    for line in f:
#        vertices = line.split()
#        for i in range(1, len(vertices)):
#            g.add_edge((vertices[0], vertices[i]))
#
#cuts = minimum_cut(g, 1000)
#print '>>>>>>>>>', cuts, len(cuts)
