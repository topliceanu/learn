# -*- coding: utf-8 -*

import random


def randomized_primality_test(n, k):
    """ Checks if n is a prime number using probabilitic methods.

    In particular, this function uses Fermat's primality test.
    See http://en.wikipedia.org/wiki/Fermat_primality_test for a description
    of the method.

    Args:
        n: int, number to test for primality
        k: int, number of times to run the test to make a decision.

    Returns:
        bool
    """
    for __ in range(k):
        a = random.randint(2, n-1)
        if a**(n-1) % n != 1:
            return False # n is not prime!
    return True # n is prime
