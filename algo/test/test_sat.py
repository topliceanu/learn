# -*- coding: utf-8 -*-

import unittest

from src.sat import two_sat, three_sat


class SatTest(unittest.TestCase):

    def test_two_sat(self):
        """ Given the following clauses:
            (x1 OR x2) AND (!x1 OR x3) AND (x3 OR x4) AND (!x2 OR !x4)

        These are encoded using the following format:
        [(1, 2) (-1, 3) (3, 4), (-2, -4)
        """
        clauses = [(1, 2), (-1, 3), (3, 4), (-2, -4)]
        num_vars = 4
        actual = two_sat(num_vars, clauses)
        self.assertTrue(actual, 'should detect a solution')

        clauses = [(1, 2), (1, -2), (-1, 2), (-1, -2)]
        num_vars = 2
        actual = two_sat(num_vars, clauses)
        self.assertFalse(actual, 'should detect there is no solution')
