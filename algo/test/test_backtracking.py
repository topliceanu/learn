# -*- coding: utf-8 -*-

import unittest

from src.backtracking import QueenPuzzle


class TestBacktracking(unittest.TestCase):

    def test_queen_puzle(self):
        # TODO fix this!
        puzzle = QueenPuzzle(3)
        puzzle.run()
        solutions = puzzle.get_solutions()
        print '>>>>>>>>', solutions
