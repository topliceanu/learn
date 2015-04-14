# -*- coding: utf-8 -*-

import math
import os


in_file = '{base}/ominous_omino_small.in'.format(base=os.getcwd())
out_file = '{base}/ominous_omino_small.out'.format(base=os.getcwd())
#in_file = '{base}/ominous_omino_large.in'.format(base=os.getcwd())
#out_file = '{base}/ominous_omino_large.out'.format(base=os.getcwd())


with open(in_file, 'r') as f:
    num_tests = int(f.readline())
    tests = []
    for __ in range(num_tests):
        [x, r, c] = map(int, f.readline().split()[:3])
        tests.append((x, r, c))

bounds = {
    4: [(2,2), (3,2), (4,1)],
    3: [(1,3), (2,2)],
    2: [(2,1)],
    1: [(1,1)]
}

with open(out_file, 'w') as f:
    for index, test in enumerate(tests):
        (x, r, c) = test
        winner = 'GABRIEL'

        if r * c % x != 0:
            winner = 'RICHARD'
        else:
            overbounded = False
            for bound in bounds[x]:
                (w, h) = bound
                if (r < w and c > h) or (r > w and c < h):
                    overbounded = True

            if overbounded == True:
                winner = 'RICHARD'

        f.write('Case #{index}: {winner}{eol}'.format(index=index+1,
                                   winner=winner, eol=os.linesep))
