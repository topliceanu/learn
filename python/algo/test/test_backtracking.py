# -*- coding: utf-8 -*-

import unittest

from src.backtracking import QueenPuzzle, TravelingSalesman, SubsetsOfGivenSum
from src.graph import Graph


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

    def test_traveling_salesman(self):
        """ Given the following graph:
                     2
                (a)----(b)
                 | \4 / |
                 |  \/  |5
                1|  /\  |
                 | /3 \ |
                 |/    \|
                (c)----(d)
                    6
        """
        g = Graph.build(edges=[
                ('a', 'b', 2), ('a', 'd', 4), ('a', 'c', 1),
                ('b', 'd', 5), ('b', 'c', 3), ('d', 'c', 6)
            ], directed=False)
        ts = TravelingSalesman(g)
        ts.run()
        expected_min_path = ['a', 'c', 'b', 'd', 'a']
        expected_min_cost = 13
        self.assertEqual(ts.solution, expected_min_path,
            'should have computed the min path')
        self.assertEqual(ts.min_cost, expected_min_cost,
            'should have computed the min cost')

    def test_subset_of_given_sum(self):
        S = [1,2,2,3,4,5]
        N = 5
        sogs = SubsetsOfGivenSum(S, N)
        sogs.run()
        expected_solutions = [[1,2,2], [1,4], [2,3], [5]]
        self.assertItemsEqual(expected_solutions, sogs.solutions,
            'should produce the correct solution')
