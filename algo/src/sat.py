# -*- coding: utf-8 -*-

import math
import random

from src.strongly_connected_components import scc
from src.graph import Graph


def two_sat(num_vars, clauses):
    """ Solves the constraint satisfaction (CSP) using a randomized local search.

    This problem can also be solved in liniar time using the
    Strongly-Connected-Components algorithm.

    Discovered by Christos Papadimitriou.

    Running time: O(n^2logn) which is bounded by the algorithm.

    Args:
        num_vars: int, number of variables used in the clauses
        clauses: list, of tuples, format [(first, last)]
            first: int, corresponds to the index of the variable.
                If negative it means it's negated.
            second: int, corresponds to the index of the variable.
                If negative it means it's negated.

    Return:
        tuple, format (is_satisfied, solution)
            is_satisfied: boolean, whether the constraint clauses can be satisfied.
            solution: list of booleans which satify all clauses.
    """
    num_clauses = len(clauses)
    for i in range(int(math.floor(math.log(num_vars, 2)))):
        # Assign a random value of True/False to each variable.
        solution = [random.choice([True, False]) for __ in range(num_vars)]
        for j in range(2*(num_vars**2)):
            # Check if solution passes
            (is_satisfied, failed_clauses) = check_2sat_solution(solution, clauses)
            if is_satisfied is True:
                return (True, solution)

            # Pick one clause which fails for the current solution, pick one
            # variable from that clause and flip it's value.
            pick_failed = random.choice(failed_clauses)
            pick_var = random.choice(list(pick_failed))
            var_pos = abs(pick_var) - 1
            solution[var_pos] = not solution[var_pos]

    return (False, [])

def check_2sat_solution(solution, clauses):
    """ Function checks if the proposed solution satisfies the given clauses.

    Args:
        solution: list of bools, each index corresponds to the value of index
            variable
        clauses: list, of tuples, format [(first, last)]
            first: int, corresponds to the index of the variable.
                If negative it means it's negated.
            second: int, corresponds to the index of the variable.
                If negative it means it's negated.

    Returns:
        tuple, format (is_satisfied, failed_clauses)
            is_satisfied: bool, whether or not the solution satifies all clauses.
            failed_clauses: list, of tuples, format [(first, last)]
    """
    is_satisfied = True
    failed_clauses = []
    passed_clauses = []
    for clause in clauses:
        (left, right) = clause
        left_pos = abs(left) - 1
        right_pos = abs(right) -1
        not_left = left < 0 # by convention, if index is negative, then variable is negated.
        not_right = right < 0
        test_clause = ((not_left ^ solution[left_pos]) or
                       (not_right ^ solution[right_pos]))
        if test_clause is False:
            failed_clauses.append(clause)
        is_satisfied = is_satisfied and test_clause
    return (is_satisfied, failed_clauses)

def two_sat_scc(clauses):
    """ Solves the constraint satisfaction (CSP) using Kosaraju's SCC
    detection algorithm.

    The way to model the directed graph is the following:
    Given any clause, determine the relation of implication between the two
    variables considering we want the clause to be true.
    Eg: (1,2) then !x1 => x2 and !x2 => x1

    In other words, the list of constraints is transformed into a list of
    implications between variables. We build the directed graph based on these
    implications, compute SSCs. If any SCC contains both a variable and it's
    negation than the clauses are un-satisfiable.

    Complexity: O(m+n)

    Args:
        clauses: list, of tuples, format [(first, last)]
            first: int, corresponds to the index of the variable.
                If negative it means it's negated.
            second: int, corresponds to the index of the variable.
                If negative it means it's negated.

    Return:
        boolean, whether the constraint clauses can be satisfied.
    """
    g = Graph.build(directed=True)
    for clause in clauses:
        (left, right) = clause
        g.add_edge((-left, right))
        g.add_edge((-right, left))

    connected_components = scc(g)
    for component in connected_components:
        vertices = set(component)
        for vertex in vertices:
            if -vertex in vertices:
                return False
    return True

def three_sat():
    """
    Complexity: O((3/4)^n)
    Algorithm discovered by Schoning in 2002
    """
