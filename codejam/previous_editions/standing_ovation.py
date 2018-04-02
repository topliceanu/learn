# -*- coding:utf-8 -*-

import os


in_file = '{base}/standing_ovation_large.in'.format(base=os.getcwd())
out_file = '{base}/standing_ovation_large.out'.format(base=os.getcwd())


with open(in_file, 'r') as f:
    num_tests = int(f.readline())
    tests = []
    for __ in range(num_tests):
        line = f.readline().split()
        smax = int(line[0])+1
        digits = line[1][:smax]
        tests.append(digits)


with open(out_file, 'w') as f:
    for index, digits in enumerate(tests):
        add_friends = 0
        standing = 0
        for waiting_for, num_users in enumerate(digits):
            num_users = int(num_users)
            if num_users > 0:
                if standing >= waiting_for:
                    standing += num_users
                else:
                    add_friends += waiting_for - standing
                    standing = waiting_for + num_users

        f.write('Case #{index}: {add}{eol}'.format(index=index+1,
                                   add=add_friends, eol=os.linesep))
