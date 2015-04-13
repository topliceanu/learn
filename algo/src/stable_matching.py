# -*- coding: utf-8 -*-

import random


def stable_matching(u, v):
    """ Solves the stable matching problem using the Gale-Shapley Proposal
    algorithm.

    We assume that the cardinalities of u and v are equal.
    Created by Lloyd Shapley and David Gale
    Complexity: O(n^2)

    Params:
        u: dict, format {item: items}, for each item in u there is a list of
            items in v sorted by preference.
        v: dict, format {item: items}, for each item in v there is a list of
            items in u sorted by preference.

    Returns:
        list, of sets, format {item_from_u, item_from_v} corresponds to the
            perfect matching of items from u to items in v.
    """
    u_left_unassigned = u.keys()
    matchings = dict(zip(v.keys(), [None]*len(v.keys())))
    while len(u_left_unassigned) != 0:
        picked_u = random.choice(u_left_unassigned)
        picked_v = u[picked_u][0]
        if (matchings[picked_v] == None):
            matchings[picked_v] = picked_u
            u_left_unassigned.remove(picked_u)
        elif (v[picked_v].index(picked_u) < v[picked_v].index(matchings[picked_v])):
            old_match_for_v = matchings[picked_v]
            u[old_match_for_v].remove(picked_v)
            u_left_unassigned.append(old_match_for_v)
            matchings[picked_v] = picked_u
            u_left_unassigned.remove(picked_u)
        else:
            u[picked_u].remove(picked_v)

    return map(set, matchings.iteritems())
