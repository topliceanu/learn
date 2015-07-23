def add(a, b):
    """ Adds two numbers using only bit manipulations.

    The algorithm is called Kogge-Stone adder: http://en.wikipedia.org/wiki/Kogge-Stone_adder

    Params:
        a: int, first number, can be negative
        b: int, second number, can be negative

    Returns:
        int, sum of the the two numbers
    """
    while b != 0:
        c = a & b  # Find the carry bits
        a = a ^ b # Add the bits without considering the carry
        b = c << 1 # Propagate the carry
    return a;

def is_power_of_two(a):
    """ Figures out if an int is a power of two. """
    return not ((a-1) & a)

def in_place_swap(a, b):
    """ Interchange two numbers without an extra variable.

    Based on the ideea that a^b^b = a
    """
    a = a ^ b
    b = b ^ a
    a = a ^ b
    return (a, b)

def is_even(a):
    """ Checks if the input integer is even.

    Based on the ideea that if the last bit is 0 then the number is even.
    """
    return (a & 1) == 0

def min_value(a, b):
    """ Compute min of a pair of two ints. """
    return b ^ ((a ^ b) & -(a < b))

def max_value(a, b):
    """ Compute max of a pair of two ints. """
    return a ^ ((a ^ b) & -(a < b))

def is_bit_set(a, offset):
    """ Checks whether the offset bit in a is set or not.

    Returns
        bool, True if bit in position offset in a is 1
    """
    return a & (1 << offset) != 0

def set_bit(a, order):
    """ Set the value of a bit at index <order> to be 1. """
    return a | (1 << order)

def unset_bit(a, order):
    """ Set the value of a bit at index <order> to be 0. """
    return a & ~(1 << order)

def toggle_bit(a, order):
    """ Set the value of a bit at index <order> to be the inverse of original. """
    return a ^ (1 << order)

def count_set_bits(n):
    """ Returns the number of set bits in the input. """
    count = 0
    while n != 0:
        last_bit = n & 1
        if last_bit == 1:
            count += 1
        n = n >> 1
    return count

def subsets(a):
    """ Computes all the subsets of input list.

    TODO make this work.

    Params:
        a: list, of values

    Returns:
        list, a list of lists, each list representing a subset.
    """
    n = len(a)
    out = []

    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (i << j):
                subset.append(a[j])
        out.append(subset)

    return out
