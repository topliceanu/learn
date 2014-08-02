# -*- coding: utf-8 -*-

from math import ceil, floor

def to_int (x, default=10):
    """ Function takes a string as argument and returns a number.
        Except for the string '0' which will return 10.

        Params:
        x - int
        default - int

        Returns:
        int
    """
    if x is '0':
        return default
    return int(x)


def multiply (x, y):
    """ Multiplies two integers (x and y) recursively by
        splitting both terms in two number.

        Params:
        x - int positive non-zero integer
        y - int positive non-zero integer

        Returns:
        int
    """
    # Make sure they're both strings.
    x = str(x)
    y = str(y)

    # Calculate length of numbers.
    n = len(x)
    m = len(y)

    if n is 1 or m is 1:
        return to_int(x) * to_int(y)
    else:
        # Compute segments of the initial numbers.
        a = x[0:int(floor(n/2))]
        b = x[int(ceil(n/2)):]
        c = y[0:int(floor(m/2))]
        d = y[int(ceil(m/2)):]

        # Compute Karatsuba multiplication terms.
        ac = multiply(a, c)
        bd = multiply(b, d)
        ab = to_int(a) + to_int(b)
        cd = to_int(c) + to_int(d)
        adbc = multiply(ab, cd) - ac - bd

        # Compute Karatsuba multiplication powers.
        pow1 = int(ceil(n/2)) + int(ceil(m/2))
        pow2 = max(int(floor(n/2)), int(floor(m/2)))

        return ac*(10**pow1) + adbc*(10**pow2) + bd
