from math import ceil, floor

def to_int (x, default=10):
    """
        Function takes a string as argument and returns a number.
        Except for the string '0' which will return 10.
    """
    if x is '0':
        return default
    return int(x)


def multiply (x, y):
    """
        Multiplies x and y recursively by splitting both terms in two number.
        @param {Int} x, x positive non-zero integer
        @param {Int} y, y positive non-zero integer
        @return {Int}
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
        b = x[int(ceil(n/2)):n]
        c = y[0:int(floor(m/2))]
        d = y[int(ceil(m/2)):m]

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


# Test
# import pdb; pdb.set_trace();

#x = 12
#y = 13
#print "%s * %s; actual %s; expected %s" % (x, y, multiply(x, y), x*y)

#x = 12
#y = 10
#print "%s * %s; actual %s; expected %s" % (x, y, multiply(x, y), x*y)

#x = 5678
#y = 1234
#print "%s * %s; actual %s; expected %s" % (x, y, multiply(x, y), x*y)
