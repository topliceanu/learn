def total (initial, *positionals, **keywords):
    """ Simply sums up all the passed numbers. """
    count = initial
    for n in positionals:
        count += n
    for n in keywords:
        count += keywords[n]
    return count

print(__name__)
