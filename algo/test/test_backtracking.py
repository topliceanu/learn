# -*- coding: utf-8 -*-

import unittest

from src.backtracking import QueenPuzzle


class TestBacktracking(unittest.TestCase):

    def test_queen_puzzle_3(self):
        puzzle = QueenPuzzle(3)
        puzzle.run()
        expected_solutions = []
        self.assertEqual(puzzle.solutions, expected_solutions,
            'should not find any solutions for the three problem')

    def test_queen_puzzle_4(self):
        puzzle = QueenPuzzle(4)
        puzzle.run()
        expected_solutions = [[(0, 1), (1, 3), (2, 0), (3, 2)],
                              [(0, 2), (1, 0), (2, 3), (3, 1)]]
        self.assertItemsEqual(puzzle.solutions, expected_solutions,
            'should not find any solutions for the three problem')

    def test_queen_puzzle_8(self):
        puzzle = QueenPuzzle(8)
        puzzle.run()
        self.assertEqual(len(puzzle.solutions), 92,
            'should not find any solutions for the three problem')
