# -*- coding: utf-8 -*-

import unittest

from problem import levenstein, sudoku_solver

class TestProblem(unittest.TestCase):
    def test_sudoku(self):
        board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        expected = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ]
        sudoku_solver(board)
        self.assertEqual(board, expected, 'failed with board={}'.format(board))

    def test_method(self):
        tests = [
            ("foo bar", "foobar", 1),
            ("apple", "alt", 3),
            ("", "", 0),
            ("a", "a", 0),
            ("ab", "acb", 1),
        ]
        for test in tests:
            actual = levenstein(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))
