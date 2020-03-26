# -*- coding: utf-8 -*-


def flood_fill(space, point, target, replacement):
    """ This method implements the flood fill algorithm.

    Args:
        space: list of lists, the array of points where to go. space is modified in-place.
        start_point: tuple, a point, format (x, y)
        target: int, only execute on the current point if it has the target value.
        replacement: int, replace the value stored in the start_point with replacement
    """
    n = len(space)
    (x, y) = point

    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if space[x][y] == replacement:
        return

    if space[x][y] != target:
        return

    space[x][y] = replacement

    top = (x-1, y)
    bottom = (x+1, y)
    left = (x, y-1)
    right = (x, y+1)

    if x-1 >= 0:
        flood_fill(space, (x-1, y), target, replacement)
    if x+1 < n:
        flood_fill(space, (x+1, y), target, replacement)
    if y-1 >= 0:
        flood_fill(space, (x, y-1), target, replacement)
    if y+1 < n:
        flood_fill(space, (x, y+1), target, replacement)

def scanline_fill(space, point, target, replacement):
    """ Optimized version of flood-fill, for which at every iteration attempts
    to fill an entire line starting from the given point.

    Args:
        space: list of lists, the array of points where to go. space is modified in-place.
        start_point: tuple, a point, format (x, y)
        target: int, only execute on the current point if it has the target value.
        replacement: int, replace the value stored in the start_point with replacement
    """
    n = len(space)
    (x, y) = point

    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if space[x][y] == replacement:
        return

    if space[x][y] != target:
        return

    queue = []

    z = y
    while z < n and space[x][z] == target:
        space[x][z] = replacement
        if x+1 < n:
            queue.append((x+1, z))
        if x-1 >= 0:
            queue.append((x-1, z))
        z += 1

    t = y - 1
    while t >= 0 and space[x][t] == target:
        space[x][t] = replacement
        if x+1 < n:
            queue.append((x+1, t))
        if x-1 >= 0:
            queue.append((x-1, t))
        t -= 1

    for p in queue:
        scanline_fill(space, p, target, replacement)
