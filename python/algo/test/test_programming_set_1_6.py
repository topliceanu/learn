# -*- coding: utf-8 -*-

"""
## Question 1.

Download the text file [./Sum.txt]

The goal of this problem is to implement a variant of the 2-SUM algorithm
(covered in the Week 6 lecture on hash table applications).

The file contains 1 million integers, both positive and negative (there might
be some repetitions!).This is your array of integers, with the ith row of the
file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval
[-10000,10000] (inclusive) such that there are distinct numbers x,y in the
input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line
addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your
own hash table for it. For example, you could compare performance under the
chaining and open addressing approaches to resolving collisions.
"""

#import os
#
#from src.hash_table import two_sum_problem_sort, two_sum_problem_hash
#from src.heap import Median
#
#
#numbers = []
#with open('{base}/test/Sum.txt'.format(base=os.getcwd())) as f:
#    for line in f:
#        numbers.append(int(line))
#
#count = 0
#
#for t in range(-10000, 10000):
#    results = two_sum_problem_hash(numbers, t, distinct=True)
#    if len(results) > 0:
#        count += 1
#
#print '>>>>>>>>', count # should be 427


"""
## Question 2.

Download the text file [./Median.txt]

The goal of this problem is to implement the "Median Maintenance" algorithm
(covered in the Week 5 lecture on heap applications). The text file contains
a list of the integers from 1 to 10000 in unsorted order; you should treat
this as a stream of numbers, arriving one by one. Letting xi denote the ith
number of the file, the kth median mk is defined as the median of the numbers
x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among
x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000
(i.e., only the last 4 digits). That is, you should compute
(m1+m2+m3+⋯+m10000)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and
search-tree-based implementations of the algorithm.
"""

#sum_medians = 0
#median_maintenance = Median()
#
#with open('{base}/test/Median.txt'.format(base=os.getcwd())) as f:
#    for line in f:
#        new_median = median_maintenance.add(int(line))
#        #print '>>>', len(median_maintenance.h_low), map(abs, reversed(median_maintenance.h_low[:2])), new_median, median_maintenance.h_high[:2], len(median_maintenance.h_high)
#        sum_medians += new_median
#
#print '>>>>>>>>>', sum_medians % 10000 # should be 1213
