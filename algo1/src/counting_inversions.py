from math import floor, ceil

def sort_and_count_split_inversions (left, right):
    """
        This function counts the number of inversions accross left and right.
        An inversion is any pair (i,j), i from left and j from right, where i > j.

        @param {Array} left - sorted array
        @param {Array} right - sorted array
        @return [{Array}, {Number}] - sorted array and invertion counter
    """
    n = len(left)
    m = len(right)
    out = []
    i = 0
    j = 0
    count = 0

    while i < n and j < m:
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
            # Count an inversion when an element in the right array
            # is larger the the one in the left array.
            count += n - i
    if i is n:
        while j < m:
            out.append(right[j])
            j += 1
    if j is m:
        while i < n:
            out.append(left[i])
            i += 1
    return [out, count]


def sort_and_count_inversions (arr):
    """
        This function is a divide an conquer routine that recursively splits the
        input array in two halves counting the inversions them summing them up.

        @param {Array} arr
        @return {Array}
    """
    n = len(arr)
    # Base case.
    if n is 1:
        return [arr, 0]
    else:
        # Split the input array in two.
        left = arr[0:int(floor(n/2))]
        right = arr[int(ceil(n/2)):n]

        # Count inversions in each of the smaller arrays.
        [left_sorted, left_count] = sort_and_count_inversions(left)
        [right_sorted, right_count] = sort_and_count_inversions(right)

        # Count inversions only across the arrays.
        [arr_sorted, split_count] = sort_and_count_split_inversions(left_sorted, right_sorted)

        # Sum them all up.
        count = left_count + right_count + split_count
        return [arr_sorted, count]


# Test
arr = [1, 3, 5, 2, 4, 6]
print sort_and_count_inversions(arr)
