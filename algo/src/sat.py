# -*- coding: utf-8 -*-

import math
import random


def two_sat(num_vars, clauses):
    """ Solves the constraint satisfaction (CSP) using a randomized local search.

    This problem can also be solved in liniar time using the
    Strongly-Connected-Components algorithm.

    Discovered by Christos Papadimitriou.

    Running time: O(n^2logn) which is bounded by the algorithm.

    Params:
        num_vars: int, number of variables used in the clauses
        clauses: list, of tuples, format [(first, last)]

    Return:
        boolean, whether the constraint clauses can be satisfied.
    """
    def check(solution, clauses):
        out = []
        for clause in clauses:
            (left, right) = clause
            left_pos = int(left[-1:])-1
            right_pos = int(right[-1:])-1
            not_left = left[:1] == '!'
            not_right = right[:1] == '!'
            test = ((not_left ^ solution[left_pos]) or
                    (not_right ^ solution[right_pos]))
            out.append(test)
        return out

    num_clauses = len(clauses)
    for i in range(int(math.floor(math.log(num_vars, 2)))):
        # Assign a random value of True/False to each variable.
        solution = [random.choice([True, False]) for __ in range(num_vars)]
        for j in range(2*(num_vars**2)):
            # Check if solution passes
            checks = check(solution, clauses)
            all_pass = reduce(lambda x,y: x and y, checks, True)
            if all_pass is True:
                return True

            # Pick one clause which fails for the current solution, pick one
            # variable from that clause and flip it's value.
            failed = [clauses[i] for i, v in enumerate(checks) if v is False]
            pick_failed = random.choice(failed)
            pick_var = random.choice(list(pick_failed))
            var_pos = int(pick_var[-1:]) - 1
            solution[var_pos] = not solution[var_pos]

    return False

def three_sat():
    """
    Complexity: O((3/4)^n)
    Discovered by Schoning in 2002
    """
