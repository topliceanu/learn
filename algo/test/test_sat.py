# -*- coding: utf-8 -*-

import unittest

from src.sat import two_sat, three_sat


class SatTest(unittest.TestCase):

    def test_two_sat(self):
        """ Given the following clauses:
            (x1 OR x2) AND (!x1 OR x3) AND (x3 OR x4) AND (!x2 OR !x4)
        """
        clauses = [('x1', 'x2'), ('!x1', 'x3'), ('x3', 'x4'), ('!x2', '!x4')]
        num_vars = 4
        actual = two_sat(num_vars, clauses)
        self.assertTrue(actual, 'should detect a solution')

        clauses = [('x1', 'x2'), ('x1', '!x2'), ('!x1', 'x2'), ('!x1', '!x2')]
        num_vars = 2
        actual = two_sat(num_vars, clauses)
        self.assertFalse(actual, 'should detect there is no solution')
