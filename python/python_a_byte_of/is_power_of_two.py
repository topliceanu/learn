def is_power_of_two(x):
    """ Checks whether the input is the power of 2. """
    return x & (x-1) == 0
