from math import floor, ceil

def merge (left, right):
    i = 0
    j = 0
    n = len(left)
    m = len(right)
    out = []

    while i < n and j < m:
        if left[i] < right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1

    if i is n:
        for l in range(j, m):
            out.append(right[l])
    elif j is m:
        for l in range(i, n):
            out.append(left[l])

    return out


def merge_sort (arr):
    """
        Sorts out an array.
    """
    n = len(arr)
    if n is 1: # Base case.
        return arr
    else:
        left = merge_sort(arr[0:int(floor(n/2))])
        right = merge_sort(arr[int(ceil(n/2)):n])
        res = merge(left, right)
        return res


# Test
#arr = [7,2,6,3,1,8,4,9,5]
arr = [4,5,2,3,0,14,34]
print merge_sort(arr)

