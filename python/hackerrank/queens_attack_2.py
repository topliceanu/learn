#!/bin/python

# Problem: Queen's Attack II
# You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.
# Source: https://www.hackerrank.com/challenges/queens-attack-2/problem

N = 1; NE = 2; E = 3; SE = 4; S = 5; SW = 6; W = 7; NW = 8

DIRECTIONS = [N, NE, E, SE, S, SW, W, NW]

def direction(coord1: tuple[int, int], coord2: tuple[int, int]) -> tuple[int, bool]:
    (r1, c1), (r2, c2) = coord1, coord2
    if c2 == c1 and r2 > r1:
        return N, True
    elif c2 > c1 and r2 > r1 and c2 - c1 == r2 - r1:
        return NE, True
    elif c2 > c1 and r2 == r1:
        return E, True
    elif c2 > c1 and r2 < r1 and c2 - c1 == r1 - r2:
        return SE, True
    elif c2 == c1 and r2 < r1:
        return S, True
    elif c2 < c1 and r2 < r1 and c1 - c2 == r1 - r2:
        return SW, True
    elif c2 < c1 and r2 == r1:
        return W, True
    elif c2 < c1 and r2 > r1 and c1 - c2 == r2 - r1:
        return NW, True
    else:
        return N, False 

def less(direction, coord1:tuple[int, int], coord2:tuple[int, int]) -> bool:
    (r1, c1), (r2, c2) = coord1, coord2
    if direction == N:
        return r1 < r2
    elif direction == NE:
        return r1 < r2 and c1 < c2
    elif direction == E:
        return c1 < c2
    elif direction == SE:
        return r1 > r2 and c1 < c2
    elif direction == S:
        return r1 > r2
    elif direction == SW:
        return r1 > r2 and c1 > c2
    elif direction == W:
        return c1 > c2
    elif direction == NW:
        return c1 > c2 and r1 < r2
    else:
        return False

def distance(direction, coord1: tuple[int, int], coord2: tuple[int, int]) -> int:
    (r1, c1), (r2, c2) = coord1, coord2
    if direction == N:
        return abs(r2 - r1)
    elif direction == NE:
        return abs(c2 - c1)
    elif direction == E:
        return abs(c2 - c1)
    elif direction == SE:
        return abs(r1 - r2)
    elif direction == S:
        return abs(r2 - r1)
    elif direction == SW:
        return abs(c1 - c2)
    elif direction == W:
        return abs(c1 - c2)
    elif direction == NW:
        return abs(c1 - c2)
    else:
        return 0
    
def farthest(c_qoord: tuple[int, int], n: int, direction) -> tuple[int, int]:  
    r_q, c_q = c_qoord
    if direction == N:
        return (n, c_q)
    elif direction == NE:
        diff = min(n - r_q, n - c_q)
        return (r_q + diff, c_q + diff)
    elif direction == E:
        return (r_q, n)
    elif direction == SE:
        diff = min(r_q - 1, n - c_q)
        return (r_q - diff, c_q + diff)
    elif direction == S:
        return (1, c_q)
    elif direction == SW:
        diff = min(r_q - 1, c_q - 1)
        return (r_q - diff, c_q - diff)
    elif direction == W:
        return (r_q, 1)
    elif direction == NW:
        diff = min(n - r_q, c_q - 1)
        return (r_q + diff, c_q - diff)
    else:
        return (1, 1)

def prev(direction: int, coords: tuple[int, int]) -> tuple[int, int]:
    dirs = {
        N: (-1, 0),
        NE: (-1, -1),
        E: (0, -1), 
        SE: (+1, -1),
        S: (+1, 0),
        SW: (+1, +1),
        W: (0, +1),
        NW: (-1, +1),
    }
    (add_r, add_c) = dirs[direction]
    (r, c) = coords
    return (r + add_r, c + add_c)

def queens_attack_2(n: int, k: int, r_q: int, c_q: int, obstacles: list[tuple[int, int]]) -> int:
    # Complexity: O(1) space and O(k) time
    q_coord = (r_q, c_q)
    far = {}
    for d in DIRECTIONS:
        far[d] = farthest(q_coord, n, d)
    for o_coord in obstacles:
        d, in_direction = direction(q_coord, o_coord)            
        if not in_direction:
            continue
        if less(d, o_coord, far[d]):
            far[d] = prev(d, o_coord)
    out: int = 0
    for d, o_coord in far.items():
        out += distance(d, q_coord, o_coord)
    return out

def queens_attack_2_bis(n, k, r_q, c_q, obstacles):
    # More elegant solution (but O(n) space) by a user: https://www.hackerrank.com/challenges/queens-attack-2/forum/comments/1559198
    east=n-c_q
    west=c_q-1
    north=n-r_q
    south=r_q-1
    n_east=min(north,east)
    n_west=min(north,west)
    s_east=min(south,east)
    s_west=min(south,west)
    for r_o,c_o in obstacles:
        if c_o==c_q:
            if r_o>r_q:
                north=min(north,r_o-r_q-1)
            else:
                south=min(south,r_q-r_o-1)
        elif r_o==r_q:
            if c_o>c_q:
                east=min(east,c_o-c_q-1)
            else:
                west=min(west,c_q-c_o-1)
        elif abs(r_o-r_q)==abs(c_o-c_q):
            row_diff = r_o - r_q
            col_diff = c_o - c_q
            distance = abs(row_diff) - 1
            if row_diff>0 and col_diff>0:
                n_east=min(n_east,distance)
            elif row_diff>0 and col_diff<0:
                n_west=min(n_west,distance)
            elif row_diff<0 and col_diff<0:
                s_west=min(s_west,distance)
            elif row_diff<0 and col_diff>0:
                s_east=min(s_east,distance)
    max_positions = east+west+north+south+n_east+n_west+s_east+s_west

    return(max_positions)