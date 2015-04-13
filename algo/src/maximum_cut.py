# -*- coding: utf-8 -*-

import random

from src.graph import Graph


def maximum_cut(g):
    """ Solves the maximum cut problem using local search algorithm with
    probability of success of 50%.

    Complexity: exponential, NP-complete complexity class.

    Params:
        g: object, instance of

    Returns
        tuple, format (left_vertex_set, right_vertex_set)
            left_vertex_set: list, of vertices composing the left side of the cut.
            right_vertex_set: list, of vertices composing the right side of the cut.
    """
    # 1. Randomly split the vertices into two lists.
    vertices = g.get_vertices()
    split_point = random.randint(0, len(vertices)-1)
    left = vertices[:split_point]
    right = vertices[split_point:]

    # 2. Start searching for a better solution using local search.
    while True:
        possible_switches = []
        for v in vertices:
            # number of edges incident on v that _don't_ cross the cut (A,B)
            dv = 0
            # number of edges incident on v that _do_ cross the cut (A, B)
            cv = 0

            v_in_left = v in left
            for i in g.incident(v):
                i_in_left = i in left
                if i_in_left and v_in_left:
                    dv += 1
                elif i_in_left and not v_in_left:
                    cv += 1
                elif not i_in_left and v_in_left:
                    cv += 1
                elif not i_in_left and not v_in_left:
                    dv += 1
            if dv > cv:
                possible_switches.append(v)
        if len(possible_switches) == 0:
            break
        else:
            v = random.choice(possible_switches)
            if v in left:
                left.remove(v)
                right.append(v)
            else:
                right.remove(v)
                left.append(v)

    return (left, right)

def weighted_maximum_cut(g):
    """ """
