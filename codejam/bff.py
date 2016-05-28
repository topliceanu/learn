#-*- coding: utf-8 -*-

import os
import copy

in_file = '{base}/bff_small.in'.format(base=os.getcwd())
out_file = '{base}/bff_small.out'.format(base=os.getcwd())

def bff(initial):
  # Build bffs hash.
  bffs = {}
  for child, his_bff in enumerate(initial):
    bffs[child+1] = int(his_bff)

  so_far = {}
  for child in bffs.keys():
    so_far[child] = set([child, bffs[child]])
  lasts = copy.copy(bffs)

  count = 0
  while count < 10:
    count += 1
    if len(so_far) == 0:
      return count

    for child in so_far.keys():
      last = lasts[child]
      his_bff = bffs[last]
      if his_bff not in so_far[child]:
        so_far[child].add(his_bff)
        lasts[child] = his_bff
      else:
        del so_far[child]
        del lasts[child]

# Read from/Write into files.
num_tests = 0
tests = []

# Read and Write from files
with open(in_file, 'r') as f:
    num_tests = int(f.readline())
    for __ in range(num_tests):
        num_children = int(f.readline())
        children = f.readline()[:-1].split(' ')
        tests.append(children[:num_children])

# Read from input.
with open(out_file, 'w') as f:
  for index, initial in enumerate(tests):
    result = bff(initial)
    f.write('Case #{index}: {result}{eol}'.format(index=index+1, result=result, eol=os.linesep))
