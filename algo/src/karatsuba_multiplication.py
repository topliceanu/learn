# -*- coding: utf-8 -*-

from math import ceil, floor


def multiply (x, y):
    """ Multiplies two integers (x and y) recursively by
    splitting both terms in two number.

    NOTE! The difference between the two numbers should be of at most one order
    of magnitude! Otherwise this algorithm will not work.

    Params:
        x: int, positive non-zero integer
        y: int, positive non-zero integer

    Returns:
        int, value of x*y
    """
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = int(ceil(float(n)/2))

    # Compute segments of the initial numbers.
    a = int(floor(x / 10**m))
    b = int(x % (10**m))
    c = int(floor(y / 10**m))
    d = int(y % (10**m))

    # Compute Karatsuba multiplication terms.
    ac = multiply(a, c)
    bd = multiply(b, d)
    abcd = multiply((a+b), (c+d))
    adbc = abcd - ac - bd

    # Return Karatsuba multiplication result.
    return int(ac*(10**(m*2)) + adbc*(10**m) + bd)
