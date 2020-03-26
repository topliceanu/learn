# Implements the HyperLogLog algorithm.
# See: http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40671.pdf

import hashlib
import math


class HyperLogLog(object):
    def __init__(self, p, hash_func):
        self.p = p
        self.h = hashlib.new(hash_func)
        self.m = 2**self.p
        self.M = [0]*self.m

    def add(self, value):
        """ Refine the cardinality estimate by passing yet another value
        through the hash function.
        """
        x = self.h(value)
        [idx, w] = split(x, self.p)
        self.M[idx] = max(self.M[idx], self.ro(w))

    def get_cardinality(self):
        """ Return an estimate of the cardinality of the input set so far
        using a stocastic correction algorithm.
        """
        E = self.alpha_m(self.m) * (self.m ** 2) * sum([2 ** (-Mj) for Mj in self.M])
        if E < (5 / 2) * self.m:
            V = sum([1 for i in self.M if i == 0])
            if V != 0:
                return self.linear_counting(self.m, V)
        elif E > (1 / 30) * (2 ** 32):
            return -(2 ** 32) * math.log(1 - (E / (2 ** 32)))
        return E

    def ro(self, hash_value):
        """ Returns the number of leading zeros for the hash_value. """

    def split(self, value, precision):
        """ Splits the binary representation of value into first precision bits
        and the rest of the bits.
        """

    def alpha_m(self):
        """ Correction algorithm. """
        if m <= 16:
            return 0.673
        elif m <= 32:
            return 0.697
        elif m <= 64:
            return 0.709
        else:
            return 0.7213/(1+1.079/m)

    def linear_counting(self, m, V):
        return m * math.log(m/V)
