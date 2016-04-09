#-*- coding: utf-8 -*-

import os

in_file = '{base}/counting_sheep_small.in'.format(base=os.getcwd())
out_file = '{base}/counting_sheep_small.out'.format(base=os.getcwd())

def has_all_digits(s):
  return s == set(range(10))

def get_digits(num):
  return set([int(i) for i in str(num)])

def count_digits(initial):
  seen_so_far = get_digits(initial)
  previous = initial
  while True:
    current = previous + initial
    if current == previous:
      return 'INSOMNIA'

    seen_so_far = seen_so_far | get_digits(current)
    if has_all_digits(seen_so_far):
      return current

    previous = current

num_tests = 0
tests = []

## Read and Write from files
#with open(in_file, 'r') as f:
#    num_tests = int(f.readline())
#    for __ in range(num_tests):
#        tests.append(int(f.readline()))
#
## Read from input.
#with open(out_file, 'w') as f:
#  for index, initial in enumerate(tests):
#    result = count_digits(initial)
#    f.write('Case #{index}: {result}{eol}'.format(index=index+1, result=result, eol=os.linesep))

## Test cases.
#tests = [0,1,2,11,46,132,8,7,89,182,86,188,124,103,18,81,200,160,69,183,30,91,163,166,75,172,156,50,196,149,178,194,5,25,158,120,170,90,109,101,112,116,34,3,187,12,113,37,85,36,60,24,84,22,106,197,152,143,165,40,108,41,177,193,10,199,28,77,4,65,45,63,6,93,9,53,144,73,180,21,48,167,171,145,61,14,111,192,29,125,128,38,174,154,179,176,20,162,155,67]
#results = ['INSOMNIA',10,90,110,506,792,96,70,801,910,946,940,2356,721,90,729,9000,2560,345,1098,270,910,1304,5478,900,1892,936,900,980,1043,890,970,90,900,790,1560,1190,450,545,909,896,1276,918,30,1309,156,904,370,680,396,900,456,924,198,954,1970,912,1001,2475,920,972,369,1239,1930,90,1990,476,539,92,715,360,504,90,930,90,424,1296,730,900,189,576,1169,1197,1160,549,238,1110,960,203,9000,896,190,870,924,1253,1936,900,1458,1085,469]
#
#for index, test in enumerate(tests):
#  actual = count_digits(test)
#  expected = results[index]
#  if actual != expected:
#    text = "For input {test} expected {expected} but got {actual}"\
#      .format(test=test, expected=expected, actual=actual)
#    raise Exception(text)
#  else:
#    print "{a} -> {b} -> {times}".format(a=test,b=actual,times=float(actual)/test if expected != 'INSOMNIA' else 'N/A')
#print 'All ok'
