# -*- coding: utf-8 -*-

import math
import os


in_file = '{base}/infinite_house_pancakes_small.in'.format(base=os.getcwd())
out_file = '{base}/infinite_house_pancakes_small.out'.format(base=os.getcwd())
#in_file = '{base}/infinite_house_pancakes_large.in'.format(base=os.getcwd())
#out_file = '{base}/infinite_house_pancakes_large.out'.format(base=os.getcwd())


with open(in_file, 'r') as f:
    num_tests = int(f.readline())
    tests = []
    for __ in range(num_tests):
        num_diners = int(f.readline())
        pancakes = f.readline().split()
        tests.append(map(int, pancakes[:num_diners+1]))

with open(out_file, 'w') as f:
    for index, pancakes in enumerate(tests):
        tmax = max(pancakes)
        tmaxes = [tmax]
        num_splits = 0

        while sum(pancakes) != len(pancakes):
            max_pancake = max(pancakes)
            pancakes.remove(max_pancake)
            pancakes.append(int(math.floor(float(max_pancake)/2)))
            pancakes.append(int(math.ceil(float(max_pancake)/2)))
            num_splits += 1
            tmax = max(pancakes) + num_splits
            tmaxes.append(tmax)

        num_minutes = min(tmaxes)

        f.write('Case #{index}: {num_minutes}{eol}'.format(index=index+1,
                                   num_minutes=num_minutes, eol=os.linesep))
