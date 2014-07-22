def pick_pivot(arr, l, r):
    """ Pick a pivot element
    """
    (arr[0], 0)

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
    return arr

def quick_sort(arr, l, r):
    """ Sorts the input array using the 'quick sort' method.

        Params:
        arr - a list of elements.
        l - left most index of the array
        r - right most index of the array

        Returns:
        A list of sorted elements.
    """
    if n == 1:
        return arr
    (p, pos) = pick_pivot(arr, l, r)
    (left, right) = partition(arr, pos)
    quick_sort(left, len(left))
    quick_sort(right, len(right))
