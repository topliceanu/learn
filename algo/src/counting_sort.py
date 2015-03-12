# -*- conding: utf-8 -*-

def counting_sort(numbers):
    """ Sorts the input array using the counting method.

    It's usefull when the variation between the smallest and the largest of the
    input values is not large.

    Args:
        numbers: list of integers to sort
        k: int, such that any number in numbers is between 0 and k inclusive.

    Returns:
        list of sorted numbers.
    """
    counts = {}
    max_val = 0

    # Compute histogram with number frequencies.
    for number in numbers:
        if number not in counts:
            counts[number] = 0
        counts[number] += 1
        if max_val < number:
            max_val = number

    # Perform prefix sum computation.
    total = 0
    for i in range(max_val+1):
        if i not in counts:
            continue
        oldCount = counts[i]
        counts[i] = total
        total += oldCount

    # Compute the output array.
    output = {}
    for number in numbers:
        output[counts[number]] = number
        counts[number] += 1

    return output.values()
