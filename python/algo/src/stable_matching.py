# -*- coding: utf-8 -*-

import random


def stable_matching(u, v):
    """ Solves the stable matching problem using the Gale-Shapley Proposal
    algorithm.

    Given two sets of items u and v, each item in u has preferences to items in
    v, and every item in v has preferences to items in u. Compute a stable
    matching between items in u and items in v, such that there is no item left
    out, and the only reason why an item has no better option is because it's
    better options all have better options in turn.

    We assume that the cardinalities of u and v are equal.

    Created by Lloyd Shapley and David Gale.

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
    # Stores final matchings, format {u: v}
    matchings = dict(zip(v.keys(), [None]*len(v.keys())))

    # Maintains the invariant that the current set of pairs is a matching! at
    # every given time each u is matched to at most one v, and vice-versa.
    while len(u_left_unassigned) != 0:
        picked_u = random.choice(u_left_unassigned)

        # u proposes to it's first preference.
        picked_v = u[picked_u][0]

        if (matchings[picked_v] == None):
            # v doesn't have a match yet.
            matchings[picked_v] = picked_u
            u_left_unassigned.remove(picked_u)
        elif (v[picked_v].index(picked_u) < v[picked_v].index(matchings[picked_v])):
            # v prefers u to it's current match
            old_match_for_v = matchings[picked_v]
            # old_match_for_v can no longer request to be paired with v again!
            u[old_match_for_v].remove(picked_v)
            u_left_unassigned.append(old_match_for_v)
            matchings[picked_v] = picked_u
            u_left_unassigned.remove(picked_u)
        else:
            # v prefers it's existing match to u
            u[picked_u].remove(picked_v)

    return map(set, matchings.iteritems())
