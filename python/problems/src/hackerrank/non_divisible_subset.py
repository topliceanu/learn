#/bin/python3

# Problem: Non-divisible subset
# Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S is not evenly divisible by k.
# Source: https://www.hackerrank.com/challenges/non-divisible-subset/problem

def non_divisible_subset(s, k):
    L = [] 
    for num in s: 
        L.append(num % k) 
    d = {} 
    for num in L: 
        if num not in d: 
            d[num] = 1 
        else: 
            d[num] += 1 
    max_arr = 0 
    if 0 in d: 
        max_arr += 1 
    count = 1 
    while count <= k//2: 
        if 2*count == k: 
            max_arr +=1 
        elif count in d and (k - count) in d: 
            max_arr += max(d[count], d[k - count]) 
        elif count in d: 
            max_arr += d[count] 
        elif (k - count) in d: 
            max_arr += d[k - count] 
        else: 
            pass
        count += 1 
    return max_arr 

    # Simple solution: Combination of n take k+; for every combination, select any 2 numbers and check they are not divisible by k. Return the largest k.