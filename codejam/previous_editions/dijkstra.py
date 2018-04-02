# -*- coding: utf-8 -*-

import math
import os


in_file = '{base}/dijkstra_small.in'.format(base=os.getcwd())
out_file = '{base}/dijkstra_small.out'.format(base=os.getcwd())
#in_file = '{base}/dijkstra_large.in'.format(base=os.getcwd())
#out_file = '{base}/dijkstra_large.out'.format(base=os.getcwd())


with open(in_file, 'r') as f:
    num_tests = int(f.readline())
    tests = []
    for __ in range(num_tests):
        [l, x] = map(int, f.readline().split())
        s = f.readline()[:l]
        tests.append(s*x)

mult = {
    '1': {
        '1': '1',
        'i': 'i',
        'j': 'j',
        'k': 'k'
    },
    'i': {
        '1': 'i',
        'i': '1', # -1
        'j': 'k',
        'k': 'j' # -j
    },
    'j': {
        '1': 'j',
        'i': 'k', # -k
        'j': '1', # -1
        'k': 'i'
    },
    'k': {
        '1': 'k',
        'i': 'j',
        'j': 'i', # -i
        'k': '1' # -1
    }
}
sign = {
    '1': {
        '1': 0,
        'i': 0,
        'j': 0,
        'k': 0
    },
    'i': {
        '1': 0,
        'i': 1,
        'j': 0,
        'k': 1
    },
    'j': {
        '1': 0,
        'i': 1,
        'j': 1,
        'k': 0
    },
    'k': {
        '1': 0,
        'i': 0,
        'j': 1,
        'k': 1
    }
}

# Precompute all the ways to obtain
cache = {}

def compute(s):
    """ Returns (value of computation, sign=1 if minus, 0 if plus) """
    val = '1'
    count_sign = 0
    for c in s:
        val = mult[val][c]
        count_sign += sign[val][c]
    return (val, count_sign%2)

with open(out_file, 'w') as f:
    for index, test in enumerate(tests):
        n = len(test)
        answer = 'NO'
        for x in range(1, n-2):
            for y in range(x+1, n-1):
                i = compute(test[:x])
                j = compute(test[x:y])
                k = compute(test[y:])
                if i == 'i' and j == 'j' and k == 'k':
                    answer = 'YES'

        f.write('Case #{index}: {answer}{eol}'.format(index=index+1,
                                       answer=answer, eol=os.linesep))
