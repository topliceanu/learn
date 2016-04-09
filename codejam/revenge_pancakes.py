#-*- coding: utf-8 -*-

import os

in_file = '{base}/B-large.in'.format(base=os.getcwd())
out_file = '{base}/B-large.out'.format(base=os.getcwd())

HAPPY = '+'
BLANK = '-'

def count_flips(pancakes):
  if pancakes[0] == HAPPY:
    prev_count_happy = 0
    prev_count_blank = 1
  else:
    prev_count_happy = 1
    prev_count_blank = 0

  for pancake in pancakes[1:]:
    if pancake == HAPPY:
      new_count_happy = min(prev_count_happy, prev_count_blank + 1)
      new_count_blank = min(prev_count_blank + 2, prev_count_happy + 1)
    else:
      new_count_happy = min(prev_count_happy + 2, prev_count_blank + 1)
      new_count_blank = min(prev_count_blank, prev_count_happy + 1)
    prev_count_happy = new_count_happy
    prev_count_blank = new_count_blank

  return prev_count_happy

# Read from/Write into files.
num_tests = 0
tests = []

with open(in_file, 'r') as f:
    num_tests = int(f.readline())
    for __ in range(num_tests):
      tests.append(f.readline()[:-1])

with open(out_file, 'w') as f:
  for index, value in enumerate(tests):
    result = count_flips(value)
    f.write('Case #{index}: {result}{eol}'.format(index=index+1, result=result, eol=os.linesep))
