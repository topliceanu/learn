#/bin/python3

from typing import List, Set, Dict, Tuple

def knapsack_0_1(capacity: int, weights: List[int], values: List[int]) -> List[int]:
    n:int = len(weights)
    m:List[List[int]] = [[0] * (capacity+1)] * (n+1)
    for i in range(1, n+1):
        w_i, v_i = weights[i-1], values[i-1]
        for j in range(1, capacity+1):
            if w_i > j:
                m[i][j] = m[i-1][j]
            else:
                m[i][j] = max(m[i-1][j], m[i-1][j-w_i]+v_i)

    out:List[int] = [0] * n
    i, j = n, capacity
    while i >=0 and j >= 0:
        w_i = weights[i-1]
        if w_i <= j and m[i][j] > m[i-1][j]:
            out[i-1] = 1
            j -= w_i 
        i -= 1
    return out