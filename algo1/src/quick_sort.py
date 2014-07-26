import random


def pick_pivot(l, r):
    """ Picks a pivot element at random from the 25-75% input percentile.

    Params:
    l - left most index to pick as pivot
    r - right most index to pick as pivot

    Return:
    int - a randon number between l and r
    """
    return random.randint(l, r)

def partition(arr, l, r):
    """ Arranges all elements smaller than p to the left and all
    elements larger than p to the right.

    Params:
    arr - list of elements in an array.
    l - left most position and position of the pivot.
    r - right most position to sort.

    Return:
    The partitioned array.
    """
    pos = l # pos denotes the position of the pivot.
    i = pos + 1
    for j in range(pos+1, r):
        if arr[j] < arr[pos]:
            (arr[i], arr[j]) = (arr[j], arr[i])
            i += 1
    # Finally move the pivot from the first position into it's correct order.
    (arr[i-1], arr[pos]) = (arr[pos], arr[i-1])
    return arr, (i - 1)

def quick_sort(arr, l, r):
    """ Sorts the input array using the 'quick sort' method.

    Params:
    arr - a list of elements.
    l - left most index of the array
    r - right most index of the array

    Returns:
    A list of sorted elements.
    """
    if (l - r + 1) == 1:
        return arr

    # Pick a pivot and make sure it's in the first position of the array.
    p = pick_pivot(l, r)
    (arr[l], arr[p]) = (arr[p], arr[l])

    # Partition the array in place and return the final position of the pivot.
    (arr, pos) = partition(arr, l, r)

    # Recurse on the two positions.
    quick_sort(arr, l, pos)
    quick_sort(arr, pos+1, r)
