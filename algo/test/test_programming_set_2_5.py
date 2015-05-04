# -*- coding: utf-8 -*-

""" In this assignment you will implement one or more algorithms for the
traveling salesman problem, such as the dynamic programming algorithm covered
in the video lectures. The data file describing a TSP instance is [./Tsp.txt]
The first line indicates the number of cities. Each city is a point in the
plane, and each subsequent line indicates the x- and y-coordinates of a single
city.

The distance between two cities is defined as the Euclidean distance, that is,
two cities at locations (x,y) and (z,w) have distance sqrt((x−z)^2+(y−w)^2),
between them.

In the box below, type in the minimum cost of a traveling salesman tour for
this instance, rounded down to the nearest integer.

OPTIONAL: If you want bigger data sets to play with, check out the TSP instances
from around the world here. The smallest data set (Western Sahara) has 29
cities, and most of the data sets are much bigger than that. What's the largest
of these data sets that you're able to solve --- using dynamic programming or,
if you like, a completely different method?

HINT: You might experiment with ways to reduce the data set size. For example,
trying plotting the points. Can you infer any structure of the optimal solution?
Can you use that structure to speed up your algorithm?
"""


import math
import os

from src.graph import Graph
from src.traveling_salesman import traveling_salesman


nodes = []

with open('{base}/test/Tsp.txt'.format(base=os.getcwd()), 'r') as f:
    num_cities = int(f.readline())

    for i in range(num_cities):
        coords = map(float, f.readline().split())
        nodes.append((str(i), coords[0], coords[1]))

def distance(i, j):
    return float(math.sqrt((i[1] - j[1])**2 + (i[2] - j[2])**2))

g = Graph(directed=False)
for i in nodes:
    for j in nodes:
        if i == j:
            continue
        edge = (i[0], j[0], distance(i,j))
        g.add_edge(edge)

(min_cost, min_path) = traveling_salesman(g)
print '>>>>', min_cost
