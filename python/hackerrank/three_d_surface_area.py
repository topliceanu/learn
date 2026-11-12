

def three_d_surface_area(A: list[list[int]]):
    h, w = len(A), len(A[0])
    area:int = 0
    # bottom and top
    for i in range(0, h):
        for j in range(0, w):
            if A[i][j] != 0:
                area += 1 + 1
    # front
    for i in range (0, h):
        prev = 0
        for j in range(0, w):
            if a[i][j] != prev:
                area += abs(prev-a[i][j])
                prev = a[i][j]
        area += prev
    # back
    for i in range(0, h):
        prev = 0
        for j in range(w-1, -1, -1):
            if a[i][j] != prev:
                area += abs(prev-a[i][j])
                prev = a[i][j]
        area += prev
    # left
    for j in range(0, w):
        prev = 0
        for i in range(0, h):
            if a[i][j] != prev:
                area += abs(prev-a[i][j])
                prev = a[i][j]
        area += prev
    # right
    for j in range(0, w):
        prev = 0
        for i in range(h-1, -1, -1):
            if a[i][j] != prev:
                area += abs(prev-a[i][j])
                prev = a[i][j]
        area += prev

    return area

