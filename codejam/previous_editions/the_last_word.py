#-*- coding: utf-8 -*-

import os

in_file = '{base}/the_last_word_large.in'.format(base=os.getcwd())
out_file = '{base}/the_last_word_large.out'.format(base=os.getcwd())

def last_word(initial):
    out = [initial[0]]
    for index in range(1, len(initial)):
        if out[0] <= initial[index]:
            out.insert(0, initial[index])
        else:
            out.append(initial[index])
    return ''.join(out)

# Read from/Write into files.
num_tests = 0
tests = []

# Read and Write from files
with open(in_file, 'r') as f:
    num_tests = int(f.readline())
    for __ in range(num_tests):
        tests.append(f.readline()[:-1])

# Read from input.
with open(out_file, 'w') as f:
  for index, initial in enumerate(tests):
    result = last_word(initial)
    f.write('Case #{index}: {result}{eol}'.format(index=index+1, result=result, eol=os.linesep))
