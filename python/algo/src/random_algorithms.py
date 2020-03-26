# -*- coding: utf-8 -*-

import random


def fisher_yates(arr):
    """ Random shuffle of input array. """
    for i in range(len(arr)):
        j = random.randrange(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def reservoir_sampling(generator, k):
    """ Pick at random k element from arr. """
    samples = []
    for index, val in generator:
        # First fill the output with all the first elements.
        if index < k:
            samples.append[val]
        else:
            # Replace elements in the output at random with decreasing probability.
            r = random.randrange(0, index)
            if r < k:
                samples[r] = value

    return samples
