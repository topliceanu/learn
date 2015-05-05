# -*- coding: utf-8 -*-

import unittest

from src.sat import two_sat, two_sat_scc, three_sat


class SatTest(unittest.TestCase):

    def test_two_sat(self):
        """ Given the following clauses:
            (x1 OR x2) AND (!x1 OR x3) AND (x3 OR x4) AND (!x2 OR !x4)

        These are encoded using the following format:
        [(1, 2) (-1, 3) (3, 4), (-2, -4)
        """
        clauses = [(1, 2), (-1, 3), (3, 4), (-2, -4)]
        num_vars = 4
        (is_satisfied, _) = two_sat(num_vars, clauses)
        self.assertTrue(is_satisfied, 'should detect a solution')

        clauses = [(1, 2), (1, -2), (-1, 2), (-1, -2)]
        num_vars = 2
        (is_satisfied, _) = two_sat(num_vars, clauses)
        self.assertFalse(is_satisfied, 'should detect there is no solution')

    def test_two_sat_larger(self):
        clauses = [(1, 2), (2, 3), (3, 4), (1, 4),
                   (4, 5), (6, 7), (7, 8), (1, -8)]
        (is_satisfied, _) = two_sat(8, clauses)
        self.assertTrue(is_satisfied, 'should find a satifiable solution')

        clauses = [(1, 2), (-1, 2), (1, -2), (-1, -2),
                   (4, 5), (6, 7), (7, 8), (1, -8)]
        (is_satisfied, _) = two_sat(8, clauses)
        self.assertFalse(is_satisfied, 'should not find a satifiable solution')

    def test_two_sat_scc(self):
        clauses = [(1, 2), (-1, 3), (3, 4), (-2, -4)]
        is_satisfiable = two_sat_scc(clauses)
        self.assertTrue(is_satisfiable, 'there exists a valid solution')

        clauses = [(1, 2), (1, -2), (-1, 2), (-1, -2)]
        is_satisfiable = two_sat_scc(clauses)
        self.assertFalse(is_satisfiable, 'there doesnt exist a valid solution')

        clauses = [(1, 2), (2, 3), (3, 4), (1, 4),
                   (4, 5), (6, 7), (7, 8), (1, -8)]
        is_satisfiable = two_sat_scc(clauses)
        self.assertTrue(is_satisfiable, 'there exists a valid solution')

        clauses = [(1, 2), (-1, 2), (1, -2), (-1, -2),
                   (4, 5), (6, 7), (7, 8), (1, -8)]
        is_satisfiable = two_sat_scc(clauses)
        self.assertFalse(is_satisfiable, 'there doesnt exist a valid solution')
